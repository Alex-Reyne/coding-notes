# Comment

# Naming Conventions
  # Variable, Function, Method: function, my_function
  # CONSTANT: CONSTANT, MY_CONSTANT
  # Class: Model, MyClass
  # module: module.py, my_module.py

# NUMBERS
print(1+1) # 2
a = 10
print(a) # 10
print(a+a) # 20
a = a*5
print(a) # 50
my_income = 100 # int type
tax_rate = 0.1 # floating type
my_taxes = my_income * tax_rate
print(my_taxes) # 10.0 results in floating type
print() # blank line

# STRINGS
# Basics
'hello'
"hello"
" I'm a dog " # use "" to escape single '
mystring = 'abcdefg'
print(mystring) # abcdefg
print(mystring[0]) # a
print(mystring[-1]) # g
print()
# Slicing
print(mystring[2:]) # cdefg; start from index all the way to end
print(mystring[:3]) # abc; up to but not including index
print(mystring[2:5]) # cde; slice starting from, up to but not including
print(mystring[:]) # abcdefg; grabs entire string
print(mystring[::]) # abcdefg; grabs entire string
print(mystring[::1]) # abcdefg; set step size 1
print(mystring[::2]) # aceg; set step size 2, skips every other index
print()
# strings are immutable, so can't reassign index.
# i.e. mystring[0] = 'x' will result in TypeError
# Methods
x = mystring.upper()
print(x) # ABCDEFG
x = mystring.lower()
print(x) # abcdefg
x = mystring.capitalize()
print(x) # Abcdefg
x = mystring.split()
print(x) # ['abcdefg']
mystring = 'Hello World'
x = mystring.split() # splits on space by default
print(x) # ['Hello', 'World']
x = mystring.split('e')
print(x) # ['H', 'llo World']
print()
# Print Formatting
x = "Insert string here: {}".format("INSERT ME") # string interpolation
print(x) # Insert string here: INSERT ME
x = "Item One: {} Item Two: {}".format("dog", "cat")
print(x) # Item One: dog Item Two: cat
x = "Item One: {y} Item Two: {x}".format(x ="dog",y ="cat")
print(x) # Item One: cat Item Two: dog


