class Dog():
    # Class Object Attribute, same for any instance of a class
    species = 'Mammal' # Every single dog is a mammal

    def __init__(self, breed, name, spots): # I guess this is similar to a constructor
        self.breed = breed
        self.name = name
        self.spots = spots 

    # Operations/Actions (Methods)
    # Method is afunction that is inside of a class that works with the object
    
    def bark(self, number):
        print("WOOF! " * number + "My name is " + self.name)

my_dog = Dog(breed = 'Labrador', name = 'Sammy', spots = False) # You can also pass in the parameters in order, not neccessary to type out the names

my_dog.species # Mammal

my_dog.bark(4) # Need open/closed parentheses

class Circle():
    pi = 3.14

    def __init__ (self, radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi # You can create a new attribute right in the constructor
        self.diameter = radius * 2

    def get_circumfrence(self):
        return self.radius * self.pi * 2 

my_circle = Circle()

print(my_circle.get_circumfrence())

print(my_circle.area)
