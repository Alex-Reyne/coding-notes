# M1 Mac Development Environment - homebrew, zsh, Ruby, and Python
https://www.joshholtz.com/blog/2021/10/27/joshs-m1-development-environemnt.html
- setup M1 dev environment w/o having to create 2nd terminal icon using rosetta


# Install/Reinstall Homebrew
```sh
# Uninstall homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

# Check brew uninstalled
which brew  # => brew not found
brew -v

# Install homebrew
  # M1: /opt/homebrew
  # macOS/intel: /usr/local
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/highwind/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Check brew installed
which brew    # => /opt/homebrew/bin/brew
brew list     # See installed brew packages
brew leaves   # See top-level packages
```

# Install asdf
- manages multiple runtime versions: gvm, nvm, rbenv, pyenv
```sh
brew install asdf
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
asdf install ruby 2.5.1
asdf install python 2.7.18

# Nodejs
asdf plugin add nodejs    # install nodejs plugin
asdf local nodejs latest  # installs latest nodejs version locally

# asdf commands
  # http://asdf-vm.com/manage/commands.html
asdf plugin list                        # List installed plugins
asdf install <name> <version>           # Install a specific ver of a package
asdf install <name> latest[:<version>]  # Install latest stable ver beginning w/ str
asdf current                            # Show current ver being used for all packages
asdf current <name>                     # Display current ver for package



asdf plugin add awsebcli

```

