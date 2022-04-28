
# MERN Setup
- Project Setup with MERN Stack
  - www.mongodb.com/languages/mern-stack-tutorial

```sh
mkdir mern
cd mern

# Install npx
npm install -g npx
which npx # ~/.nvm/versions/node/v15.14.0/bin/npx

# Current local versions
npm -v  # 7.7.6
node -v # v15.14.0
npm list -g --depth 0 # show globally installed npm packages

# Create React App - client
npx create-react-app client

# Create server folder & init package.json
mkdir server
cd server
npm init -y

# Install dependencies
npm install mongodb express cors dotenv
  # mongodb - DB driver that allows Node.js apps to connect to DB
  # express - web framework for Node.js
  # cors - Node.js package that allows cross origin resource sharing
  # dotenv - module to load env vars from .env to process.env file
```