def add(n1, n2):
    print(n1+n2)

add(10,20)

number1 = 10
number2 = input("Please provide a number ")

# add(number1, number2) This causes a type error, since you are adding an integer and string

# Everything past the error will not get executed, and nothing will happen

try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE ERROR
    result = number1 + number2
except:
    # HAPPENS IF THERE IS AN ERROR
    print("Hey it looks like you aren't adding correctly!")
else:
    # HAPPENS IF TRY GOES WELL
    print("Add went well!")
    print(result)
finally:
    # HAPPENS NO MATTER WHAT
    print('The Try/Catch is done!')

try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    # This code will only happen if there is specifically a TypeError
    print("There was a TypeError")
except OSError:
    print("Hey only gave read permissions in your open() function. Change 'r' to 'w'")
finally:
    print("I always run!")

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("That is a number")
            print(result)
            break
        finally:
            print("End of try/except/finally")