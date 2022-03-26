# Install asdf
- manage multiple runtime versions: gvm, nvm, rbenv, pyenv

```sh
brew install asdf         # Install asdf version manager
which asdf                # install check

# Ruby
asdf plugin add ruby      # install ruby plugin
asdf install ruby latest  # install latest ruby
asdf list ruby            # show versions installed
asdf global ruby 3.1.1    # set global ruby version
asdf local ruby 3.1.1     # set local ruby version
ruby --version            # check ruby version

# Python
asdf plugin add python      # install python plugin
asdf install python 3.7.10  # install python version
asdf list python            # show versions installed
asdf global python 3.7.10   # set global python version
asdf local python 3.7.10    # set local python version
python -- version           # check python version

# Install i386 versions
izsh # switch to i386 mode (Rosetta)
asdf install ruby 2.5.1 # 2.6.6
asdf install python 2.7.18

# Nodejs
asdf plugin add nodejs    # install nodejs plugin
asdf local nodejs latest  # installs latest nodejs version locally

# asdf commands
  # http://asdf-vm.com/manage/commands.html
asdf plugin list                        # List installed plugins
asdf plugin list all                    # List all plugins
asdf install <name> <version>           # Install a specific ver of a package
asdf install <name> latest[:<version>]  # Install latest stable ver beginning w/ str
asdf current                            # Show current ver being used for all packages
asdf current <name>                     # Display current ver for package


asdf plugin add awsebcli
```

# Modify zshrc
```s
# asdf version manager
. /opt/homebrew/opt/asdf/libexec/asdf.sh
# Created by `pipx` on 2022-03-24 19:09:54
export PATH="$PATH:/Users/highwind/.local/bin"
```

# Install Yarn
```sh
# Check if yarn already installed
yarn --version
#  Install yarn via npm
npm install --global yarn
npm list -g # list global packages
```