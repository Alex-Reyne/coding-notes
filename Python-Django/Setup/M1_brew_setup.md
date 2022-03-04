

```sh
# Open terminal window (zsh)
# Run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# if installation errors, try installing again

# Create .zshrc in home dir (if not created yet)
touch .zshrc
# Open .zshrc if already created
open ~/.zshrc

# add to end of .zshrc
export PATH=/opt/homebrew/bin:$PATH

# Run following command to make this available
source ~/.zshrc

# Run following command to confirm working
brew help
which brew


```