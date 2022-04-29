# PERN Setup
- Project Setup with PERN Stack
  - youtube.com/watch?v=ldYcgPKEZC8&ab_channel=freeCodeCamp.org

# Setup Local Project
## Server Folder
```sh
mkdir server
cd server
# Initialize package.json file
npm init -y

# Install Packages
npm i express pg cors dotenv
  # dotenv to load env vars from .env to process.env
  # --save not needed; default installed as dependencies since npm 5.0.0
npm i --save-dev nodemon
# Add under package.json > "scripts"
  "start": "./node_modules/.bin/nodemon -L index.js",
    # -L flag for using nodemon with files in shared filesystem in vagrant
# Run server
node index.js # Will not auto-restart server
npm start     # Runs nodemon to auto-restart server
```

## Client Folder - Create React App
```sh
# Install React Client
npx create-react-app <app_name> # client
  # don't install globally to ensure npx uses latest version
cd <app_name>
# Remove git - Optional
  rm -rf .git
npm start
```

## Create PSQL DB and Connect to Server
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
