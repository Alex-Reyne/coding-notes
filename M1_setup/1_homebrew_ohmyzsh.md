# Homebrew
# oh-my-zsh
# oh-my-zsh theme
# zshrc


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

# Install oh-my-zsh
```sh
# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

# Create oh-my-zsh theme
```s
# dir: ~/.oh-my-zsh/themes/joshdholtz.zsh-theme
PROMPT="%(?:%{$fg_bold[green]%}➜ $(arch) :%{$fg_bold[red]%}➜ )"
PROMPT+=' %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)'
ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}git:(%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"
```

# Modify zshrc
```s
export ZSH="$HOME/.oh-my-zsh"
# joshdholtz theme shows arch type in the prompt
ZSH_THEME="joshdholtz"
RPROMPT='%F{white}%T%f'
plugins=(git)
source $ZSH/oh-my-zsh.sh

# M1 and Rosetta
alias mzsh="arch -arm64 zsh"
alias izsh="arch -x86_64 zsh"

# Separate homebrew PATHs
if [ "$(uname -p)" = "i386" ]; then
  echo "Running in i386 mode (Rosetta)"
  eval "$(/usr/local/homebrew/bin/brew shellenv)"
  alias brew='/usr/local/homebrew/bin/brew'
else
  echo "Running in ARM mode (M1)"
  eval "$(/opt/homebrew/bin/brew shellenv)"
  alias brew='/opt/homebrew/bin/brew'
fi
```


