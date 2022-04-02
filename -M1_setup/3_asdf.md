# asdf
# zshrc
# asdf: ruby, python, nodejs
# asdf: yarn


# Install asdf
- manage multiple runtime versions: gvm, nvm, rbenv, pyenv

```sh
brew install asdf   # Install asdf version manager
which asdf          # install check

# asdf commands
  # http://asdf-vm.com/manage/commands.html
asdf plugin list                        # List installed plugins
asdf plugin list all                    # List all plugins
asdf plugin add <name>                  # Install plugin

asdf install <name> <version>           # Install a specific ver of a package
asdf install <name> latest[:<version>]  # Install latest stable ver beginning w/ str
asdf list <name>                        # List installed versions of package
asdf list all <name>                    # List all versions of a package
asdf current                            # Show current ver being used for all packages
asdf current <name>                     # Display current ver for package
asdf where <name> [<version>]           # Display install path
asdf which <command>                    # Display path to executable
```

# Modify zshrc
```s
# asdf version manager
. /opt/homebrew/opt/asdf/libexec/asdf.sh
# Created by `pipx` on 2022-03-24 19:09:54
export PATH="$PATH:/Users/highwind/.local/bin"
```

# Install ruby, python, nodejs
```sh
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

# Nodejs
brew install gpg          # install GnuPG to verify authenticity of package
asdf plugin add nodejs    # install nodejs plugin
asdf local nodejs latest  # installs latest nodejs version locally

# Install i386 versions
izsh  # switch to i386 mode (Rosetta)
asdf install ruby 2.5.1 # 2.6.6
asdf install python 2.7.18
mzsh  # switch back to arm64 mode

asdf plugin add awsebcli
# ...to be continued
```

# Install Yarn
```sh
yarn --version    # Check if yarn already installed

# Install yarn via asdf
asdf plugin add yarn
asdf install yarn latest

#  Install yarn via npm
npm install --global yarn
npm list -g # list global packages
```