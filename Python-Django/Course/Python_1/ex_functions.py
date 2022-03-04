## -- PROBLEM 1 -- ##
# Given a list of ints, return True if sequence '1, 2, 3' exists
def arrayCheck(nums):
  # num times to loop is length of list -2 to stop at 3rd last num
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

print(arrayCheck([1, 1, 2, 3, 1])) # → True
print(arrayCheck([1, 1, 2, 4, 1])) # → False
print(arrayCheck([1, 1, 2, 1, 2, 3])) # → True


## -- PROBLEM 2 -- ##
# Given a str, return new str made of every other char starting
# with the first, so "Hello" yields "Hlo".

def stringBits1(str):
  return str[::2]

# Or
def stringBits2(str):
  result = ""
  for i in range(len(str)):
    if i%2 == 0:
      result = result + str[i]
  return result

print(stringBits2('Hello')) # → 'Hlo'
print(stringBits2('Hi')) # → 'H'
print(stringBits2('Heeololeo'))# → 'Hello'

