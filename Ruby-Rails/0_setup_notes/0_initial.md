# Command Line Tools
# Ruby Version Manager
# Yarn


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

# Install Ruby Version Manager: asdf, rvm, or rbenv
```sh
# Check M1_DevEnv_Setup folder
```

# Install Yarn
```sh
# Check M1_DevEnv_Setup folder
yarn --version            # Check if yarn already installed
npm install --global yarn # Install yarn via npm
npm list -g               # list global packages
```

