# Handle the exception thrown by the code below by using try and except blocks.
"""
for i in ['a','b','c']:
    print(i**2)
"""

def func():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except:
        print('Not a valid iterator')
    finally:
        print("I always run")


# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

"""
x = 5
y = 0

z = x/y
"""

def func0():
    try:
        x = 5
        y = 0

        z = x/y
    except:
        print("You cannot divide by 0!")
    finally:
        print("All done!")


# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
"""
def ask():
    pass
"""

def ask():
    while True:
        try:
            value = int( input( 'Enter your value!' ) )
        except:
            print("Not a valid value!")
            continue
        else:
            print(value**2)
            break

ask(2) # 4