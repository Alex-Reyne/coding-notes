# M1 Setup Instructions

# NVM: Node version manager
# Node

# NVM: Node version manager (Compass)
```sh
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
```
```s
# Add to zprofile
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```
```sh
# Check nvm installed
nvm -v    # nvm version
nvm list  # list nvm versions
```

# Node (Compass)
```sh
# Install Node
nvm install 15.4.0
# Check node installed
node -v # node version
```

