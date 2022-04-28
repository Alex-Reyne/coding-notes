# M1 Mac Development Environment - homebrew, zsh
- setup M1 dev environment w/o using 2nd rosetta terminal
- creates separate aliases (mzsh, izsh) to install to different paths
- install homebrew in separate modes

# Zsh: modify
```s
alias mzsh="arch -arm64 zsh"
alias izsh="arch -x86_64 zsh"
alias brewr="arch -x86_64 /usr/local/bin/brew $@
```
```sh
# Alias commands
mzsh  # M1/arm64 alias to install to /opt/homebrew/bin/brew
izsh  # Rosetta/intel/i386 alias to install to /usr/local/homebrew/bin/brew
brewr # run non-native version of homebrew; use brewr in place of brew
which brew
  # arm64 => /opt/homebrew/bin/brew
  # i386 => /usr/local/Homebrew/bin/brew
```

# Rosetta 2
```sh
# Install Rosetta 2
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```

# Xcode CLT
```sh
xcode-select --install
```