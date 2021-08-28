import re

print(re.search(r'cat|dog','The cat is here')) # Use the pipe operator to see if you have cat or dog

print(re.findall(r'.at', 'The cat in the hat sat'))  # . is the wild card operator, so use it if you dont know one of the letters
print(re.findall(r'...at', 'The cat in the hat went splat'))

print(re.findall(r'^\d', '1 is a number' )) # ^ is used to see if the string starts with something
print(re.findall(r'\d$', 'The number is 2' )) # $ is used to see if the string ends with something

phrase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]' # Use [^ID] to exclude something based on one of your identifiers
print(re.findall(pattern, phrase))

pattern = r'[^\d]+' # The + makes it all print on one line
print(re.findall(pattern, phrase))

text = 'Only find the hypen-words in this sentence, but you do not know how long-ish each one is' 
pattern = r'[\w]+-[\w]+'
re.findall(pattern, text)