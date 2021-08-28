text = "The agent's phone number is 408-555-1234. Call soon!"

print('phone' in text)

import re

pattern = 'phone'

print(re.search(pattern, text)) # Shows the indexes where the pattern is in the text if it is in there

match = re.search(pattern, text)

print(match.span())
print(match.start())
print(match.end())

# If the pattern shows up twice, it only returns the first one

# You can use re.findall(), which returns a list of all the matches in the string
print(re.findall('phone', 'phone once, phone twice'))

for match in re.finditer('phone', 'phone once, phone twice'):
    print(match)
    print(match.span())
    print(match.group())

