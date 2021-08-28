class Sample():
    pass

# Convention for Classes is Camel Casing (SampleWord)

my_sample = Sample()
type(my_sample)

# __main__.Sample

class Dog():
    def __init__(self, breed, name, spots): # Special method called init, called upon whenever instance of class is created. Always start off with self keyword, connects it to instance of the class, allows it to refer to itself
        
        # Take in the argument, and assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots 

my_dog = Dog(breed = 'Labrador', name = 'Sammy', spots = False)

type(my_dog) # __main__.Dog

my_dog.breed # Labrador