
# Users must be able to choose a variant if applicable
- search for variant

SECTION > main-collection-product-grid.liquid
- lists product cards
  SNIPPET > card-product.liquid
  - {{ card_product.featured_media }} => jpg url
  - {{ card_product.media }} => array of all jpg urls
  - {{ card_product.selected_or_first_available_variant }} => ProductVariantDrop
  - {{ card_product.variants }} => ProductVariantDrop...
    {% for variant in card_product.variants %}
      {{ variant.title }}: 
      {{ variant.inventory_quantity }}
      {{ variant | json }} => prints complete dump
    {% endfor %}

188: div id="ProductInfo-{{ section.id }}"
316-340: when 'variant_picker'
342-?: <variant-selects>

SECTION > main-product.liquid
- product page
- 394-432: 'Add to cart' form button
  <product-form></product-form>


# WHAT I NEED TO DO
- Just follow main-product.liquid page
- everything i need is in div "product__info-wrapper grid__item"
- move the thing into card-product snippet
ProductInfo-template--15180695142556__main


products/new-balance-ms327lu1-rain-cloud
color: violet, green, black, lightblue, red, blue
size: 7, 8, 9


# Objects

product.selected_variant
- returns the variant object of the selected variant
<!-- URL = myshop.myshopify.com/products/shirt?variant=124746062 -->
{{ product.selected_variant.id }}
<!-- Output: 124746062 -->
product.selected_or_first_available_variant

product.tags
- Returns an array of all of the product's tags. The tags are returned in alphabetical order.
{% for tag in product.tags %}
  {{ tag }}
{% endfor %}




# Theme tags

## Render
- Renders a snippet from the snippets folder of a theme
- you don't need to write the file's .liquid extension
{% render 'snippet-name' %}
- When a snippet is rendered, the code inside it does not automatically have access to the variables assigned using variable tags within the snippet's parent template. Similarly, variables assigned within the snippet can't be accessed by the code outside of the snippet.

### Passing variables to a snippet
- Variables assigned using variable tags can be passed to a snippet by listing them as parameters on the render tag:
{% assign my_variable = 'apples' %}
{% render 'name', my_variable: my_variable, my_other_variable: 'oranges' %}
#### The with parameter
- A single object can be passed to a snippet by using the with and as parameters:
{% assign featured_product = all_products['product_handle'] %}
{% render 'product' with featured_product as product %}
#### The for parameter
- A snippet can be rendered once for each value of an enumerable object by using the for and as parameters:
{% assign variants = product.variants %}
{% render 'variant' for variants as variant %}


## Paginate
- splits products, blog articles, and search results across multiple pages
- 'by' parameter followed by an integer betweeen 1 and 50
  - tells paginate tag how many results should output per page
{% paginate collection.products by 5 %}
  {% for product in collection.products %}
    <!--show product details here -->
  {% endfor %}
{% endpaginate %}


