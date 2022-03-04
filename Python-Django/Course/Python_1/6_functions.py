# FUNCTIONS

######################
# def Statements
######################
def my_func(param1='default'):
  """
  Docstring
  This will show up in quick doc popup
  """
  print("my first python function! {}".format(param1))
my_func() # my first python function! default

def giveMeHello():
  return "hello"
giveMeHello() # will not print to terminal
result = giveMeHello()
print(result) # hello

def addNum(num1,num2):
  return num1+num2
result1 = addNum(2,3)
print(result1) # 5
print(type(result1)) # <class 'int'>
result2 = addNum('2','3')
print(result2) # 23; str concatenation
print(type(result2)) # <class 'str'>
print()

# ######################
# Lambda Expressions
# ######################

# Lambda Expressions - aka anonymous function
# when using function that accept other functions as input params

# basic function
def timesTwo(num):
    return num*2
print(timesTwo(5)) # 10
# Lambda expression
x = lambda num: num*2
print(x(5)) # 10

# Filter
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
  return num%2 == 0
evens = filter(even_bool,mylist) # filter(func, iterable)
print(evens) # <filter object at 0x*********> b/c filter is a generator
print(list(evens)) # [2, 4, 6, 8]
# Lambda expression
evens = filter(lambda num:num%2 == 0, mylist)
print(list(evens)) # [2, 4, 6, 8]
print()

# ######################
# Methods
# ######################

tweet  = "Go Sports! #Sports"
result1 = tweet.split('#')
print(result1) # ['Go Sports! ', 'Sports']
result2 = tweet.split('#')[1]
print(result2) # Sports

# 'in' Operator to check if item exists
'x' in [1,2,3] # False
'x' in ['x','y','z'] # True

