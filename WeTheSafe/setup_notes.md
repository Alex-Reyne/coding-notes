# Dependencies
- Ruby 2.5.1, Rails 5.1.7, Bundler 1.17.3, pg 0.21.0

```sh
brew install rbenv

izsh # run in i386 mode (Rosetta)
rbenv install 2.5.1
rbenv global 2.5.1
mzsh # return to arm64 mode (M1)
echo "gem: --no-document" > ~/.gemrc # turn off local doc generation


# Gemfile lock specifies bundler -v < 2.0
gem install bundler
gem install bundler -v 1.17.3
bundle install --path vendor/bundle # resolves 'your user account isn't allowed to install to system RubyGems'

brew install postgresql
brew install openssl libffi # resolves 'error ... installing pg ...'


mzsh
rben install 2.7.5
rbenv global 2.7.5
gem install rails
gem install rails -v 5.1.7


# error resurfaced: 'installing pg...'
brew install libpqxx
# error: Unable to find PostgreSQL client library.

# PSQL for M1: psql doesn't start automatically for M1
# have to start server
brew services start postgresql
rm /opt/homebrew/var/postgres/postmaster.pid
brew services restart postgresql

# Tried
gem update --system 3.2.3
brew unlink openssl && brew link openssl --force
sudo xcodebuild -license accept # agree to Xcode license before installation
brew install gpg2 # GPG keys for signing and ssh authentication
brew update
brew install --build-from-source postgresql
brew install yaml
brew install libxml2 # for nokogiri support
gem install nokogiri -- --use-system-libraries
gem install pg -v '0.21.0' -- --with-cflags="-Wno-error=implicit-function-declaration"

# To try
gem uninstall pg
bundle install --without production

brew install v8
gem install libv8 -v '3.16.14.3' -- --with-system-v8


# from compass
RUBY_CFLAGS="-Wno-error=implicit-function-declaration" rbenv install 2.6.6


# Command i need to get working
gem install pg
gem install pg -v 0.21.0
# Operation not permitted @ apply2files - /Users/highwind/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/pg-1.3.4/.appveyor.yml


# can use this in the future
ARCHFLAGS="-arch x86_64" <command>
```



