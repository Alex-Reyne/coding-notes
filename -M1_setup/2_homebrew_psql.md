# Homebrew
# Brew: Additional Packages

# Homebrew
https://brew.sh/
https://github.com/homebrew/install
```sh
# Uninstall homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
sudo rm -rf /opt/homebrew/ # remove residual files
  # Zsh: remove homebrew lines

# Install homebrew
  # M1: /opt/homebrew
  # macOS/intel: /usr/local/homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```sh
```s
# Add Homebrew to PATH in Zsh
  # skip if using Oh-my-zsh setup
eval "$(/opt/homebrew/bin/brew shellenv)"
```
```sh
# Check brew installed
which brew    # => /opt/homebrew/bin/brew
brew -v       # brew version
brew list     # See installed brew packages
brew leaves   # See top-level packages
brew cleanup  # remove broken links
brew doctor   # self-diagnosis tool
brew update   # run after brew doctor to download new formulae
```

# Brew: Additional Packages (Compass)
```sh
# Install libpq, postgresql
  # build-from-source specifies exact architecture of your machine
brew install libpq postgres --build-from-source
```
```sh
# Zsh: for compilers to find libpq you may need to set:
#  export LDFLAGS="-L/opt/homebrew/opt/libpq/lib"
#  export CPPFLAGS="-I/opt/homebrew/opt/libpq/include"
```
