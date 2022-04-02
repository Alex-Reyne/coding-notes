# M1 Setup Instructions

# rbenv
# Bundler

# rbenv: ruby version manager (Compass)
```sh
# MacOS comes with 'system ruby' pre-installed (2.6.8)
# Install rbenv
RUBY_CFLAGS="-Wno-error=implicit-function-declaration" rbenv install 2.6.6
```
```s
# Add rbenv to PATH in Zsh, after homebrew line
eval "$(/opt/homebrew/bin/brew shellenv)"
```
```sh
rbenv global 2.6.6  # set global ruby version
ruby -v             # ruby version
```

# Bundler
```sh
# Install bundler
gem install bundler:1.16.1
```


