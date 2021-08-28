mylist = [1,2,3]

print(len(mylist))

class Sample():
    pass

mySample = Sample()
# You cannot use built in python functions with user defined objects regularly

# In order to do this, you need to use magic methods, also known as dunder methods (double underscore)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return (self.title + " by " + self.author)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")

b = Book('Python Rocks', 'Suyog', 200)
print(b) # Prints location of the book object, if you do not have __str__

print(len(b))

del b # deletes the variable from the computer's memory