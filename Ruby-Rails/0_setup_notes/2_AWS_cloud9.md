# AWS
# Cloud9 IDE


# Setup AWS
- Create AWS account
- Services > Developer Tools > Cloud9 IDE
- Create new environment
  - Platform: Ubuntu Server

# Cloud9 IDE
- Installed by default: 
  - ruby 2.6.3, rails 5, rvm, bundler, node
```sh
ruby -v           # => ruby 2.6.3p62
rvm list rubies   # ruby 2.6.3 set to current && default
node --version    # check node ver

# Yarn - install using ubuntu platform
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn
yarn --version    # check yarn ver

# Bundler
gem list bundler    # check bundler ver; default 1.17.2
gem update bundler  # updates bundler ver
```

# Cloud9 - rails 5 & 6
```sh
# Rails 6
gem list rails      # check rails ver; default 5.0.0
gem install rails -v 6.0.2.1
rails -v            # confirm rails ver
rails new test_app
rails s

# Click Preview > Preview Running Application => blocked host
# Need to add line to environment configuration
  # ex. config.hosts << "xxxxxx.xxx.cloud9.us-west-x.amazonaws.com"
# test_app > config > environments > development.rb
  # add to bottom of file before 'end'
# restart server
# Preview
# if broken image icon, Pop Out into New Window

# Rails 5
cd ~/environment
mkdir rails_5_apps
cd rails_5_apps
gem install rails -v 5.2.0
gem list rails # verify 5.2.0 installed
rails _5.2.0_ new test_app_5
cd test_app_5
rails s

```
