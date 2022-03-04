# Theme Architecture
1. Layout file: base of the theme used to repeat elements like headers & footers
2. Template: controls what's displayed on page
  - JSON templates act only as wrapper for sections
  - Liquid templates contain code
3. Sections: Reusable, customizable modules of content that merchants can add to JSON templates
4. Blocks: Reusable, customizable modules of content that can be added to sections, removed, and reordered
5. Snippets: reusable snippets of code that can be referenced using the 'render' tag

## Layouts
- Layouts are the base of the theme, through which all templates are rendered
- Located in the `layout` directory
- a good place for repeatable elements like <head> element, headers, footers
- can edit the default `theme.liquid` layout, or create multiple custom layout files

## Templates
- Templates control what's rendered on each type of page in a theme.
- Located in `templates` directory
- can use 2 different file types in theme: JSON or Liquid
  - to use sections in a template, use JSON template
  - JSON templates provide more flexibility for merchants to add, remove, reorder sections
- template types range from:
  - 404, article, blog, cart, collection, 
  - customers/[account, activate_account, addresses, login, order, register, reset_password],
  - gift_card.liquid (must be liquid template), index, list-collections,
  - page, password, product, robots.txt.liquid (must be liquid template), search

## Sections
- Sections are Liquid files that allow you to create reusable modules of content to be customized
- can include blocks which allow merchants to add, remove, reorder content
- Locatedc in the `sections` directory

