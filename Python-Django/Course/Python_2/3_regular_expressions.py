# REGULAR EXPRESSIONS

import re # regular expressions
# One of the most common uses for re module is for finding patterns in text.

######################################
### Searching for Patterns in Text ###
######################################

# List of patterns to search for
patterns = [ 'term1', 'term2' ]

# Text to parse
text = 'This is a string with term1, but does not have the other term.'

for pattern in patterns:
  print("I'm searching for: " + pattern)
  if re.search(pattern, text):
    print("MATCH!")
  else:
    print("NO MATCH!")
print()

text = 'This is a string with term1, but does not have the other term.'
match = re.search('term1',text)
print(match.start()) # 22
print(match.end()) # 27
print()

#######################################
#### Split with regular expressions ###
#######################################

# Term to split on
split_term = '@'

email = 'user@gmail.com'

# Split the email
print(re.split(split_term, email)) # ['user', 'gmail.com']
print()

############################################
### Finding all instances of a pattern #####
############################################

# Returns a list of all matches
print(re.findall('match','test phrase match is in match middle')) # ['match', 'match']
print()

#############################
### Character Sets ##########
#############################

def multi_re_find(patterns,phrase):
  '''
  Takes in a list of regex patterns
  Prints a list of all matches
  '''
  for pattern in patterns:
    print("Searching for pattern {}".format(pattern))
    print(re.findall(pattern,phrase))
    print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = [ 'sd*',    # s followed by 0 or more d's
                'sd+',      # s followed by 1 or more d's
                'sd?',      # s followed by 0 or one d's
                'sd{3}',    # s followed by 3 d's
                'sd{2,3}',  # s followed by 2-3 d's
                's[sd]+',  # s followed by 1 or more s's or d's
                ]

multi_re_find(test_patterns, test_phrase)

#############################
### Exclusion ###############
#############################

# Use ^ to exclude terms by incorporating it into bracket syntax notation.
# Ex: [^...] will match any single character not in the brackets.

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[^!.?]+']
multi_re_find(test_patterns, test_phrase) # ['This is a string', ' But it has punctuation', ' How can we remove it']

#############################
## Character Ranges #########
#############################

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=[ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

multi_re_find(test_patterns,test_phrase)

#############################
### Escape Codes ############
#############################

# 'r'  tells Python the expression is a raw string
# in a raw string, escape sequences are not parsed
# ex. '\n' is parsed as a single newline character
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)

