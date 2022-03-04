# TUPLES

t = (1,2,3)
print(t[0]) # 1
t = ('a',True,123)
print(t) # ('a', True, 123)
# tuples are like lists, except they're immutable
# t[0] = 'NEW' # will result in TypeError
print()

# SETS - unordered collections of unique elements
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(4) # will not be added b/c not unique
x.add(0.1)
print(x) # {0.1, 1, 2, 4}
converted = set([1,1,1,2,2,2,2,3,3,3])
print(converted) # {1, 2, 3}


