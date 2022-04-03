# rbenv
# Bundler

# rbenv: ruby version manager (Compass)
https://github.com/rbenv/rbenv
```sh
# Uninstall rbenv
  # Disable rbenv temporarily 
    # Zsh: remove `rbenv init` line
rbenv uninstall -f 2.7.5 # uninstall version (if ruby-build installed)
rm -rf `rbenv root` # uninstall completely
brew uninstall rbenv # remmove from brew

# Install rbenv, ruby-build
  # build-from-source specifies exact architecture of your machine
brew install rbenv ruby-build --build-from-source
RUBY_CFLAGS="-Wno-error=implicit-function-declaration" rbenv install 2.6.6

```s
# Add rbenv to PATH in Zsh (after homebrew line):
eval "$(rbenv init - zsh)"
```
```sh
# MacOS comes with 'system ruby' pre-installed (2.6.8)
rbenv global 2.6.6  # set global ruby version
ruby -v             # ruby version
```

# Bundler
```sh
# Install bundler
gem install bundler:1.16.1
```


