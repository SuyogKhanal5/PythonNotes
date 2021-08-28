import math

value = 4.35

print(math.floor(value)) # Rounds down

print(math.ceil(value)) # Rounds up

round(4.5) # Standard rounding

print(math.pi)

print(math.e)

print(math.inf) # Infinity
print(math.nan) # Not a number

# Numpy library used for numerical processing

print(math.log(math.e))

print(math.log(100,10)) # What exponent do I need to get 10 to 100

print(math.sin(10))

print(math.cos(10))

print(math.degrees(math.pi/2))

print(math.radians(180))

import random

random.seed(101) # Seed can be whatever you want
print(random.randint(0,100)) # Will print the same sequence of numbers, each seed has different sequence
print(random.randint(0,100))
print(random.randint(0,100))

mylist = list(range(0, 20))

print(random.choice(mylist)) # Prints random number from your list

# Sample with replacement
print(random.choices(population = mylist, k = 10)) # Return random value from list 10 times

# Sample without replacement
print(random.sample(population = mylist, k = 10))

random.shuffle(mylist) # Shuffles list

print(random.uniform(a = 0, b = 100)) # Uses float points for random numbers

print(random.gauss(mu = 0, sigma = 1)) # Normal Distribution