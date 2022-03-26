# Command Line Tools
# Yarn
# Ruby Version Manager
# Ruby
# Gems: Bundler, webpacker
# Rails


# Install Command Line Tools
```sh
# Check if already installed
xcode-select -p # should output: /Library/Developer/CommandLineTools
# Check if gcc and clang installed
gcc -v
clang -v
# Install command line tools
xcode-select --install # will return error if already installed
```

# Install Yarn
```sh
yarn --version            # Check if yarn already installed
npm install --global yarn # Install yarn via npm
npm list -g               # list global packages
```

# Install Ruby Version Manager: asdf, rvm, or rbenv
```sh
# Check M1_DevEnv_Setup folder
```

# Install Ruby
```sh
ruby -v                 # Check global version of ruby installed
asdf list ruby          # Check ruby versions already installed
asdf install ruby 2.6.3 # Install ruby version (2.6.3 for course)
asdf global ruby 2.6.3  # Set global ruby ver
# if issues, may have to reinstall homebrew
```

# Install Gems: Bundler, webpacker
```sh
bundle -v             # Check if bundler installed
gem install bundler
gem install webpacker
gem environment       # Check gem installation directory
```

# Install Rails 6
```sh
gem install rails             # Install rails; defaults to latest stable ver
gem install rails -v 6.0.2.1  # Install rails ver (6.0.2.1 for course)
gem list                      # Check list of local gems installed
gem list rails                # Check if rails installed
rails -v                      # Check rails ver
```



# Create new rails project
```sh
# Create new directory for rails 6 projects
mkdir <new_project_name> # rails_6_projects
cd <new_project_name>
# Create new rails application
rails new <new_app_name> # new_test_app_6

# Start rails server app
rails s
# Visit web page in browser
localhost:3000
```

# Install Rails 5
```sh
# Create new directory for rails 5 projects
mkdir <new_project_name> # rails_5_projects
cd <new_project_name>

# Check old version of rails is installed
gem install # rails (5.2.4.1)


# use this version to create a new rails app
rails _<rails_version>_ new <new_app_name> # _5.2.4.1_ test_app_5

```
