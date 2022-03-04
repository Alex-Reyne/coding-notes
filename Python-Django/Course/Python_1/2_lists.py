# LISTS - python's form of arrays

# Basics
mylist = [1,2,3]
print(mylist) # [1,2,3]
mylist = ['str',1,2,3,0.01,True,'str2',[1,2,3]] # can contain mixed data types
print(mylist) # ['str', 1, 2, 3, 0.01, True, 'str2', [1, 2, 3]]
print(len(mylist)) # length of 8 elements
print()

# Slicing
mylist = ['a','b','c','d','e']
print(mylist[0]) # a
print(mylist[-1]) # e
print(mylist[1:]) # ['b', 'c', 'd', 'e']
print(mylist[:3]) # ['a', 'b', 'c']
print()

# List Methods
# lists are mutable, unlike strings
mylist[0] = 'NEW ITEM'
print(mylist) # ['NEW ITEM', 'b', 'c', 'd', 'e']
mylist.append("APPENDED ITEM")
print(mylist) # ['NEW ITEM', 'b', 'c', 'd', 'e', 'APPENDED ITEM']
mylist.append(['x','y','z'])
print(mylist) # ['NEW ITEM', 'b', 'c', 'd', 'e', 'APPENDED ITEM', ['x', 'y', 'z']]
list_two = ['x','y','z']
mylist.extend(list_two) # extends list to include new array items
print(mylist) # ['NEW ITEM', 'b', 'c', 'd', 'e', 'APPENDED ITEM', ['x', 'y', 'z'], 'x', 'y', 'z']
mylist = ['a','b','c','d','e']
item = mylist.pop() # grabs last item from list, and returns it
print(mylist) # ['a', 'b', 'c', 'd']
print(item) # e
item = mylist.pop(0) # can specify index position to pop
print(mylist) # ['b', 'c', 'd']
print(item) # a
mylist = ['a','b','c','d','e']
mylist.reverse()
print(mylist) # ['e', 'd', 'c', 'b', 'a']
mylist = [4,6,1,7,43,2]
mylist.sort()
print(mylist) # [1, 2, 4, 6, 7, 43]
print()

# Nested Lists
mylist = [1,2,['x','y','z']]
print(mylist[2]) # ['x', 'y', 'z']
print(mylist[2][1]) # y
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0]) # 1

# List Comprehension
first_col = [row[0] for row in matrix]
print(first_col) # [1, 4, 7]

