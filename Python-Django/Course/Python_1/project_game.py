import random

# GET GUESS
def get_guess():
  '''
  Asks for the number guess and transforms the string to a list.
  '''
  return list(input("What is your guess? "))

# GENERATE COMPUTER CODE 123
def generate_code():
  '''
  generates a 3 digit list for the code
  '''
  digits = [str(num) for num in range(10)]
  random.shuffle(digits)
  return digits[:3]

# GENERATE THE CLUES
def generate_clues(code,userGuess):
  '''
  Takes user guess and code then compares numbers in a loop and
  creates list of clues according to matching parameters.
  '''
  if userGuess == code:
    return "CODE CRACKED!"

  clues = []

  # Compare guess to code
  # enumerate(iterable, start default=0)
  # use tuple-unpacking
  for ind,num in enumerate(userGuess):
    if num == code[ind]:
      clues.append("Match")
    elif num in code:
      clues.append("Close")
  if clues == []:
    return ["Nope"]
  else:
    return clues

# Run Game
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

# Create a Secret Code to start the Game
secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")

# Empty Clue Report to Start with
clueReport = []

# Keep asking until the user has gotten it right!
while clueReport != "CODE CRACKED":
  # Ask for guess
  guess = get_guess()

  # Give the clues
  clueReport = generate_clues(guess,secretCode)
  print("Here is the result of your guess:")
  for clue in clueReport:
    print(clue)

