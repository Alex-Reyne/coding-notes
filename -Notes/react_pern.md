# PERN Setup
- Project Setup with PERN Stack
  - youtube.com/watch?v=ldYcgPKEZC8&ab_channel=freeCodeCamp.org

```sh
mkdir server
cd server

# Initialize package.json file
npm init -y

# Install Packages
npm i express pg cors
  # --save not needed; installed as dependencies by default since npm 5.0.0
npm i --save-dev nodemon
# Add under package.json > "scripts"
  "start": "./node_modules/.bin/nodemon -L index.js",
    # -L flag for using nodemon with files in shared filesystem in vagrant
# Install dotenv to load env vars from .env to process.env
npm i dotenv

# Run server
node index.js # Will not auto-restart server
npm start     # Runs nodemon to auto-restart server
```

# Create PSQL DB and Connect to Server
```sh
# Create psql db
psql
CREATE DATABASE perntodo;
\c perntodo
CREATE TABLE todo(
  todo_id SERIAL PRIMARY KEY,
  description VARCHAR(255)
);
```

# Create React App Client
```sh
# Install React Client
npx create-react-app <app_name> # client
  # don't install globally to ensure npx uses latest version
cd <app_name>
# Remove git - Optional
  rm -rf .git
npm start
```


# Deploy PERN application on Heroku
- How to Deploy a PERN application on Heroku
  - youtu.be/ZJxUOOND5_A
- make sure .git is located in root dir
- must have package.json inside root dir (instructions for heroku)
- if originally structured with 2 folders (client, server), extract contents of server into root dir, and delete empty server folder
- create .env file with env vars
- update db.js with env vars
- update package.json of server
```sh
# replace "scripts"
# remove: "start": "./node_modules/.bin/nodemon -L index.js",
# Add
"start": "node index.js",
"heroku-postbuild": "cd client && npm install && npm run build",
  # will install dependencies in client folder, and create build folder
```

# Order Heroku runs scripts
1. heroku-prebuild script (runs before depencies are installed)
2. npm install (read package.json and see what depencies need to be installed)
3. heroku-postbuild script (run after depencies are installed)
4. Run start script (where node server.js happens)

- edit package.json inside client folder
```sh
# add to bottom of package.json
"proxy": "http://localhost:8000"
```

# Reset Cache - Reinstall client packages
- delete client node_modules and package-lock.json
- npm install

- update server package.json
```sh
"engines":{
  "node": "15.14.0",
  "npm": "7.7.6"
},
```
```sh
cat database.sql | heroku pg:psql -a akd-pern-todo
heroku git:remote -a akd-pern-todo
git push heroku main
# if error, try
  git push --force heroku main
heroku open
```


# Deploy to Heroku w/ M1
- medium.com/geekculture/deploy-to-heroku-from-a-macbook-m1-heroku-cli-or-githubactions-868bc3a50935
- levelup.gitconnected.com/deploy-pern-fullstack-app-on-heroku-and-netlify-automatic-deploy-9b61ac6a254e
```sh
# Requires: node > v10, npm, git
# Install Heroku CLI with brew using i386/intel arch
izsh
brew tap heroku/brew && brew install heroku

heroku --version
heroku login
heroku apps

# Create Heroku App
heroku create <app_name>
  # https://<app_name>.herokuapp.com

# Setup Heroku Postgres Database
heroku addons:create heroku-postgresql:hobby-dev -a <app_name>
  # sets a DATABASE_URL environment variable
  # => Created postgresql-shaped-36240 as DATABASE_URL

heroku addons # check new addon created

# Log into Heroku database
heroku pg:psql <database-name> --app <app_name>
  # heroku pg:psql postgresql-shaped-36240 --app akd-pern-todo
heroku pg:psql -a <app_name>
  # heroku pg:psql -a akd-pern-todo

# Create tables in Postgres database
# ex.
CREATE TABLE todo(
  todo_id SERIAL PRIMARY KEY,
  description VARCHAR(255)
);

# Run App Locally
heroku local web
# .... not working
# something is already running on port 5000
heroku local -p 7000
#...

# Deploy server (cd to root folder of project)
heroku git:remote -a <app_name>
  # heroku git:remote -a akd-pern-todo
# Push code
git subtree push --prefix server heroku main

# Define Procfile
  # <process type>: <command>
    # web: npm start

# Ensure at least 1 instance of app is running
heroku ps:scale web=1 
# Open app in browser
heroku open


```
