class Dog():
# Defining our dog's object!

    # Class Object Attributes
    bark = 'woof'

    # init method
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    # Our methods
    def greetings(self, day='sunday'):
        return f"Hello! I'm {self.name}:{self.code}, and today is {day}! {Dog.bark} {Dog.bark}!"



""" Now let's create our instance, call our attributes and methods! """

# We can create our object by passing the values in two different ways!
# Refering the parameter and its value
myDog = Dog(name='Rambo', code=911)
# Passing only the value
myDog = Dog('Rambo', 911)

# Now we have access to its attributes and methods!

# Let's call its attributes
print( myDog.bark ) # 'woof'
print( myDog.name ) # 'Rambo'
print( myDog.code ) # 911

# Let's call its methods
print( myDog.greetings() ) # "Hello! I'm Rambo:911, and today is sunday! woof woof!"

# Notice pretty important, we are not using parenthesis when we are calling our attributes, and it's not necessary, because we are retrieving information and not executing operations/methods!
# If we call a method without the parenthesis we will get the method and its location in the storage, but will not execute its process!
