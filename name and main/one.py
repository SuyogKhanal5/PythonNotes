# python one.py

# No main function in Python, all code at indentation level 0 gets run when script file is called

# Built in variable, assigned name depending on how you are running the script
__name__ == "__main__"
# Assigns __main__ to the __name__ variable when the script is run directly

if __name__ == "main":
    print('This code is being run directly')

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == "main":
    print('ONE.PY is being run directly')
else:
    print('ONE.PY has been imported')