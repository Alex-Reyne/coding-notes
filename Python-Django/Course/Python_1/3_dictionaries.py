# DICTIONARIES - python's form of hash tables (objects in JS)
# allow us to create a 'mapping' with key-value pairs
# don't retain order

# Basics
my_dict = {'key1':'value1','key2':123,'key3':{'123':[1,2,'grabMe']}}
print(my_dict) # {'key1': 'value1', 'key2': 123, 'key3': {'123': [1, 2, 'grabMe']}}
print(my_dict['key1']) # value1
print(my_dict['key2']) # 123
print(my_dict['key3']) # {'123': [1, 2, 'grabMe']}
print(my_dict['key3']['123']) # [1, 2, 'grabMe']
print(my_dict['key3']['123'][2]) # grabMe
print(my_dict['key3']['123'][2].upper()) # GRABME

my_stuff = {'lunch':'pizza','bfast':'eggs'}
print(my_stuff) # {'lunch': 'pizza', 'bfast': 'eggs'}
my_stuff['lunch'] = 'burger' # re-assign key to new value
print(my_stuff) # {'lunch': 'burger', 'bfast': 'eggs'}
print(my_stuff['lunch']) # burger
my_stuff['dinner'] = 'pasta' # add KV pair
print(my_stuff) # {'lunch': 'burger', 'bfast': 'eggs', 'dinner': 'pasta'}

# note: in python, don't have ability to add methods to dictionaries unlike JS objects
