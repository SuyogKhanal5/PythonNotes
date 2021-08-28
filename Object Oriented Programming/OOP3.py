# Inheritance - Make new classes using classes that have already been defined

class Animal():
    def __init__ (self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print("I am eating")

class Dog(Animal): # Dog is known as a "derived class" because it derives some of its methods from Animal
    def __init__(self):
        Animal.__init__(self) # Creates an instance of the animal class inside of the Dog Class
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print('WOOF!')

myDog = Dog() # Prints Animal Created and Dog Created

# Can also use the old methods
myDog.eat()

# To overwrite a method, name a method inside of your class the same as the method you want to overwrite. The one inside the new class will take precedence
myDog.who_am_i() 

myDog.bark() # WOOF