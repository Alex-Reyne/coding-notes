

# Install Command Line Tools
```sh
# Check if already installed
xcode-select-p # should output: /Library/Developer/CommandLineTools
# Check if gcc and clang installed
gcc -v
clang -v

# Install command line tools
xcode-select --install # will return error if already installed
```

# Install Yarn
```sh
# Check if yarn already installed
yarn --version
#  Install yarn via npm
npm install --global yarn
npm list -g # list global packages

```

# Install rbenv (ruby version manager)
```sh
# Check if rbenv already installed
rbenv

# Check LHL notes
```

# Install ruby
```sh
# Check if ruby already installed
ruby -v
# Install ruby
rbenv install 2.6.6 # Install ruby version
```

# Install Rails 6
```sh
# Check if bundler installed
bundle -v

# Check list of local gems installed
gem list

# Install rails
gem install rails # defaults to v 6.1.5
# Check if rails installed
gem list rails
rails -v
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
