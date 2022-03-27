# Ruby
# Gems: Bundler, Webpacker
# Rails 5 & 6


# Install Ruby
```sh
ruby -v                 # Check global version of ruby installed
asdf list ruby          # Check ruby versions already installed
asdf install ruby 2.6.3 # Install ruby version (2.6.3 for course)
asdf global ruby 2.6.3  # Set global ruby ver
# if issues, may have to reinstall homebrew
```

# Install Gems: Bundler, Webpacker
```sh
bundle -v             # Check if bundler installed
gem install bundler
gem install webpacker
gem environment       # Check gem installation directory
```

# Install Rails 5 & 6
```sh
gem install rails             # Install rails; defaults to latest stable ver
gem install rails -v 6.0.2.1  # Install rails ver (6.0.2.1 for course)
gem install rails -v 5.2.4.1  # Install rails ver (5.2.4.1 for course)
gem list                      # Check list of local gems installed
gem list rails                # Check if rails installed
rails -v                      # Check set rails ver
```

# Create new rails projects
```sh
# Create Rails 6 project
mkdir <new_project_name>                    # Create new rails proj dir
  mkdir rails_6_projects
cd rails_6_projects
rails _<rails_version>_ new <new_app_name>  # Create new rails app
  rails _6.0.2.1_ new test_app_6
rails new <new_app_name>                    # Create new rails app
  rails new test_app_6
  # delete .git folder if already inside git repo
rails s                                     # Start rails server app

# Visit web page in browser
localhost:3000

# Create Rails 5 project
# new directory for rails 5 projects
mkdir rails_5_projects
cd rails_5_projects
rails _5.2.4.1_ new test_app_5
```
