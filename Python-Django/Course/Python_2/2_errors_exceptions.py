# ERRORS AND EXCEPTIONS

###################
# try and except
###################

# Syntax:
#   try:
#     You do your operations here...
#     ...
#   except ExceptionI:
#     If there is ExceptionI, then execute this block.
#   except ExceptionII:
#     If there is ExceptionII, then execute this block.
#     ...
#   else:
#     If there is no exception then execute this block.

# try-except allows us to handle errors then continue with code
try:
  f = open('simple.txt','w') # w - write, r - read
  f.write("Test write to simple text!")
except IOError:
  print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
  print("SUCCESS!")
  f.close()
print("hello world!") # without try-except, will not run
print()

###################
# finally
###################
# finally - always runs regardless of exception in try code block

try:
   f = open("simple.txt", "r")
   f.write("Test write to simple text!")
except:
  print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
   print("I ALWAYS WORK NO MATTER WHAT!")
