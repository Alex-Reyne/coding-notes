# Deploy to Heroku w/ M1
- medium.com/geekculture/deploy-to-heroku-from-a-macbook-m1-heroku-cli-or-githubactions-868bc3a50935
- levelup.gitconnected.com/deploy-pern-fullstack-app-on-heroku-and-netlify-automatic-deploy-9b61ac6a254e

# Install Heroku CLI
```sh
# Requires: node > v10, npm, git
izsh # Switch to i386/intel arch
brew tap heroku/brew && brew install heroku
heroku --version
heroku login
heroku apps
```

# Create Heroku App & Setup PSQL DB
```sh
# Create Heroku App
heroku create <app_name> # => https://<app_name>.herokuapp.com

# Setup Heroku PSQL DB
heroku addons:create heroku-postgresql:hobby-dev -a <app_name> # sets a DATABASE_URL env variable
  # ex. postgresql-shaped-36240
heroku addons # check new addon created
```
# Connect to Heroku PSQL DB
```sh
# Method 1: Connect manually
psql --host=ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com --port=5432 --username=xxxxxxxxx --password --dbname=xxxxxxxx
  # Input password from <app_name> > Resources > Heroku Postgres > Settings > View Credentials

# Method 2: Use Heroku CLI
heroku pg:psql <database_name> --app <app_name>
  # heroku pg:psql postgresql-shaped-36240 --app akd-pern-todo
  heroku pg:psql -a <app_name>
    # heroku pg:psql -a akd-pern-todo

# Create tables in PSQL DB
# ex.
CREATE TABLE todo(
  todo_id SERIAL PRIMARY KEY,
  description VARCHAR(255)
);
# Or if existing database.sql file, upload: 
cat database.sql | heroku pg:psql -a <app_name>
```

# Deploy PERN app to Heroku

## Manual Config Steps
- How to Deploy a PERN application on Heroku:  youtu.be/ZJxUOOND5_A
- make sure .git is located in root dir
- package.json must be located inside root dir (as instructions for heroku)
- if project created with 2 folders (client, server), extract server into root dir
- create .env file with env vars
  - update db.js with process.env vars
- Edit server package.json
```sh
# Edit "scripts"
  # Remove: "start": "./node_modules/.bin/nodemon -L index.js",
  # Add
    "start": "node index.js",
    "heroku-postbuild": "cd client && npm install && npm run build",
      # will install dependencies in client folder, and create build folder
```
- Edit client package.json
```sh
# add to bottom of package.json
"proxy": "http://localhost:5000"
```
- if updating proxy, and still points to old port, reset cache & reinstall client packages
  - delete client node_modules and package-lock.json
  - `npm install`
- Update server package.json to specify versions to heroku
```sh
"engines":{
  "node": "15.14.0",
  "npm": "7.7.6"
},
```

## Run Heroku App Locally
```sh
heroku local web
  # if error msg: something is already running on port 5000
  # System Preferences > Sharing > Airplay Receiver > Disable
  # or try running on different port
    heroku local -p 7000
```

## Deploy Heoku App
```sh
# Deploy server (cd to root folder of project)
heroku git:remote -a <app_name>
git push heroku main
# if error, try
  git push --force heroku main
# Ensure at least 1 instance of app is running
heroku ps:scale web=1 
heroku open # Open app in browser

heroku logs -t # display live logs
```

# Order of Heroku runs scripts
1. heroku-prebuild script (runs before dependencies are installed)
2. npm install (read package.json and see what depencies need to be installed)
3. heroku-postbuild script (run after depencies are installed)
4. Run start script (where node server.js happens)
