# pyenv
# build issues

# pyenv
https://github.com/pyenv/pyenv

```sh
# Uninstall pyenv
  # Disable pyenv temporarily 
    # Zsh: remove `pyenv` line
pyenv uninstall -f 2.7.8 # uninstall version
rm -rf $(pyenv root) # uninstall completely
brew uninstall pyenv # remmove from brew

# Install pyenv
brew update
brew install pyenv
brew upgrade pyenv
```
```s
# add pyenv to PATH in Zsh
eval "$(pyenv init --path)" # >> ~/.zprofile
eval "$(pyenv init -)"      # >> ~/.zshrc
```
```sh
# Install python build dependencies before installing new python version
brew install openssl readline sqlite3 xz zlib

# MacOS Monterey 12.3.1 removes system Python 2.7
  # Restore Python 2.7 w/ manual install
  # https://www.python.org/downloads/release/python-2718/

# Install python version
pyenv install 3.10.1
# Build successes
  # mzsh: 3.7.13, 3.10.1
  # izsh: 2.7.10
pyenv rehash # run after installing a new version

# Install python3 w/ brew
brew install python # => installs 3.9.12

# Check python install
pyenv root # => /Users/highwind/.pyenv
which python      # => /usr/bin/python
which python3     # => /usr/bin/python3 || /Library/Frameworks/Python.framework/Versions/2.7/bin/python
python3 --version # => Python 3.8.9
```

# build issues
```sh
# Fix old package permissions
sudo chown -R $USER /usr/local/bin/*
# pyenv doctor
git clone https://github.com/pyenv/pyenv-doctor.git "$(pyenv root)/plugins/pyenv-doctor"
pyenv doctor
# update system software
softwareupdate --all --install --force
```