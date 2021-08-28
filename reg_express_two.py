import re

# \d is a digit
# \w is alphanumeric
# \s is white space
# \D is a non digit
# \W is non-alphanumerica
# \S is non-whitespace

text = 'My phone number is 408-555-1234'

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text) # Make sure to add the r in front of the string to tell python these are not escape characters

print(phone)
print(phone.group())

# + Occurs one or more times    | Example: 'Version \w-\w+' ---> 'Version A-b1_1'
# {3} Occurs exactly 3 times    | Example: '\D{3}' ------------> 'abc'
# {2,4} Occurs 2 to 4 times     | Example: '\d{2,4} -----------> '123'
# {3,} Occurs 3 or more         | Example: '\w{3,} ------------> 'anycharacters'
# * Occurs zero or more times   | Example: 'ABC*' -------------> 'AAACC'
# ? Occurs once or none         | Example: 'plurals?' ---------> 'plural'

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)

print(phone)
print(phone.group())

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern,text)

print(results.group())
print(results.group(1)) # Group ordering starts at 1