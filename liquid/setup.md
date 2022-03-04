```sh

# Install Shopify Theme Kit
brew tap shopify/shopify
brew install themekit

# Obtain theme's ID
theme get --list --password=[your-password] --store="[your-store.myshopify.com]"

# Create new dir for theme, cd into it
# Download theme and create config.yml file to connect theme w/ local version in local dir
theme get --password=[your-password] --store="[your-store.myshopify.com]" --themeid=[your-theme-id]

# Push updates to theme
theme watch # instructs Theme Kit to watch for changes in local files, and automatically pushes changes to theme in connected Shopify Store

# See changes, use themekit command 'open'
theme open --env=production # opens http://your-store.myshopify.com?preview_theme_id=[your-theme-id]
theme open --env=development


```

