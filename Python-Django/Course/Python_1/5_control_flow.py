# CONTROL FLOW

###########################
## COMPARISON OPERATORS ###
###########################
# Greater than
1 > 2
# Less than
1 < 2
# Greater than or Equal to
1 >= 1
# Less than or Equal to
1 <= 4
# Equality
1 == 1 # True
1 == "1" # False
'hi' == 'bye' # False
# Inequality
1 != 2 # True

###########################
### LOGICAL OPERATORS #####
###########################
# AND
(1 > 2) and (2 < 3)
# OR
(1 > 2) or (2 < 3)
# Multiple logical operators
(1 == 2) or (2 == 3) or (4 == 4)

##################################
### if,elif, else Statements #####
##################################
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

#####################
### FOR LOOPS #######
#####################
## For Loop with a list
seq = [1,2,3,4,5]
for item in seq:
    print(item+item)
## For Loop with a Dictionary
d = {"Sam":1,"Frank":2,"Dan":3}
for k in d:
  print(k) # keys
  print(d[k]) # values
## For Loop with a Tuple
mypairs = [(1,2),(3,4),(5,6)] # list of 3 tuple pairs
# Normal
for tup in mypairs:
    print(tup)
# Tuple un-packing
for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)

#######################
### WHILE LOOPS #######
#######################
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

#####################
### OTHER TOPICS ####
#####################
# RANGE FUNCTION
# range() quickly generates integers based on starting and ending point

# 1 arg: starting at 0
range(5) # range(0, 5); generates nums 0-4 w/o having to store in memory
list(range(5)) # [0, 1, 2, 3, 4]
for i in range(5):
    print(i)
# 2 args: start and ending
range(1,10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 3rd arg for step-size
list(range(0,10,2)) # [0, 2, 4, 6, 8]

# LIST COMPREHENSION
x = [1,2,3,4]
# We could do this:
out = []
for num in x:
    out.append(num**2)
print(out) # [1, 4, 9, 16]

# Written in List Comprehension Form
out2 = [num**2 for num in x]
print(out2) # [1, 4, 9, 16]