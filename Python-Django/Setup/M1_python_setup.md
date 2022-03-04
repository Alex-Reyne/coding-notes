
- M1 notes
  - Python 3.7 and below will not be supported on Apple Silicon
  - to install older versions (Python 3.x.x) on M1...


Check Python
```sh
type -a python # python is /usr/bin/python
which python # /usr/bin/python
python --version # Python 2.7.16
```

Install pyenv
```sh

# Method 1
brew install pyenv

# Method 2 (if method 1 doesn't work)
# Clone pyenv repo into home folder
git clone https://github.com/pyenv/pyenv.git ~/.pyenv 
cd ~/.pyenv && src/configure && make -C src
open ~/.zshrc
# edit .zshrc file with the following lines
  export PYENV_ROOT="$HOME/.pyenv" 
  export PATH="$PYENV_ROOT/bin:$PATH" 
  eval "$(pyenv init --path)" 
  eval "$(pyenv init -)"
# Quit terminal, reopen
```

Recheck system
```sh
arch # arm64
which brew # /opt/homebrew/bin/brew
brew --version # Homebrew 3.1.11 
pyenv --version # pyenv 2.0.1-3-g1706436f
```

Install python build dependencies
```sh
brew install openssl readline sqlite3 xz zlib
```

Install python version
```sh
pyenv install 3.9.4

pyenv install --patch 3.8.6 <<(curl -sSL https://raw.githubusercontent.com/Homebrew/formula-patches/113aa84/python/3.8.3.patch\?full_index\=1)

pyenv install 3.7.10
```

Post-install verification
```sh
pyenv versions
# * system (set by /Users/squademy/.pyenv/version)
#   3.7.10
#   3.8.6 
#   3.9.4

# Set global python version
pyenv global x.x.x # Python 3.8.6
```

Verify pyenv shims is activated on the PATH
```sh
type -a python
# python is /Users/highwind/.pyenv/shims/python
# python is /usr/bin/python

which python # /Users/squademy/.pyenv/shims/python
```