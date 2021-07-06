# **_Python_**

## **Introduction**

<br>

### **What Is Python?**

Python was specifically design as an easy to use lenguage with a very high focus on readability of code.

Python use something called whitespace and indentation that makes its code very accessible, even if you dont python!

Another characteristic is Python is really focused on optimizing developer time than a computer's as well as having incredible documentation!

<br>

### **What Can Python Actually Do?**

Automate simple task:

~ Searching for files and editing them.

~ Scraping information from a website.

~ Reading and editing excel files.

~ Work with Pdf's.

~ Automate emails and text messages.

~ Fill out forms.

<br>

Data Science and Machine Learning:<br>
_(And it's libraries)_

~ Analyze large data files. <br>
_(numpi & pandas)_

~ Create visualizations.<br>
_(seabourn & matplotlib)_

~ Perform machine learning tasks.<br>
_(psychic learn & tensor flow)_

~ Create and run predictive algorithms.<br>
_(psychic learn & tensor flow)_

<br>

Create Websites:

~ Use web frameworks such as django and flask to handle the backend of a website and user data.

~ Create interactive dashboards for users.<br>
_(plotty & dash)_

<br>

### **How To Start Using Python?**

We are going to be working on Visual Studio Code, thankfully the process is pretty simple, we just need to install two things:

**1.** [**Python**](https://www.python.org/downloads/)

**2.** [**Visual Studio Code Python Extension**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

After installing all the requirements we now can start using python, we could either create a python file by using the .py extension or create a Jupiter Notebook which will allow us to create and run specific chunks of code and have our data and learning path organized, the way we create our notebook is by using the .ipynb extension!
<br>

<br><br>

## **Object And Data Structure Basics**

<br>

### **Variable Assignment**

We can store data types on variables, to easily reference them later on our code!

But hey, we have some rules we have to follow:

1. Names can not start with a number.
2. There can be no spaces in the name, we can use camel case or snake case syntax.
3. Can't use any of these symbols:
   - : " ' / ? | \ ( ) ! @ # % ^ & \* ~ - +
4. It's considered best practice (PEP8) taht names are lowercase.
5. Avoid using words that have special meaning in python like 'list' and 'str' (keep in mind if the variable name you selected gets highlighted, it's a special keyword thus it cannot be used).

Python uses **Dynamic Typing**, this means we can reassign variables to different data types!
This makes python very flexible in assigning data types, this is different than other languages that are **Statically-Typed**.

For example:

```python
myDogs = 1
myDogs = ['one']

# This is totally fine!
```

_Pros and Cons of dynamic typing:_

| Pros                    | Const                                        |
| ----------------------- | -------------------------------------------- |
| Very easy to work with  | May result in bugs for unexpected data types |
| Faster development time | you need to be awate of type()               |

Let's make a quick example on how to verify the type of our variables:

```python
# To verify the type of our variables we have to use the 'type()' function, where we send our variables as the parameter and it will return it's type.

var = 1
print(type(var)) # int

var = 1.1
print(type(var)) # float

var = 'Hello World!'
print(type(var)) # string

var = true
print(type(var)) # boolean
```

<br>

### **Numbers**

We have two main number types:

~ Integers which are whole numbers.

~ Floating Point numbers which are numbers with a decimal.

<br>

Let's make some operations!

```python
# Addition
print( 5 + 5 ) # 10

# Subtraction
print( 5 - 3 ) # 2

# Multiplication
print( 5 * 5 ) # 25

# Division
print( 10 / 5 ) # 2

# Mod ~ Modulo
print( 12 % 2 ) # 0

# Power
print( 2 ** 5 ) # 32
```

_Fun Fact_
_~ There are 53 bits of precision available for a Python float, this means 0.1 is actually 0.1000000000000000055511151231257827021181583404541015625!_

<br>

### **Strings**

Strings are secuences of characters, using the syntac of either single quotes or double quotes:

```python
greatings = 'hello!'
greatings = "Hello!"
greatings = "I don't do that!"
```

~ Because strings are _ordered sequences_ it means we can use _indexing_ and _slicing_ to grab sub-sections of the string.

~ _Indexing_ notation uses [] notation after the string (or variable assign to the string).

~ _Indexing_ allow syou to grab a single character from the string

~ These actions ise [] square brackets and a number index to indicate positions of what you wish to grab:

**Character:** H e l l o <br>
**Index:** 0 1 2 3 4

We also have a cool feature called _Reverse Indexing_ which allow us to get the last items even thought we don't actually now it's lenght:

**Character:** H e l l o <br>
**Index:** 0 1 2 3 4
**Reverse Index:** 0 -4 -3 -2 -1

~ _Slicing_ allows you to grab a subsection of multiple characters, a 'slice' of the string.

~ _Slicing_ has the following syntax:

```python
[start:stop:step]

# start is a numerical index for the slice start
# stop is the index you will go up to (but will not be included)
# step is the size of the 'jump' ypu take
```

<!-- -->tab - new line

Let's make a quick example:

```python
# Defining our string
greetings = "Hello World!"

""" Indexing """

indexedGreetings = greetings[11]
print(indexedGreetings) # '!'

""" Reversed indexing """

reversedIndexingGreetings = greetings[-1]
print(reversedIndexingGreetings) # '!'

""" slicing """

slicedGreetings = greeting[2:] # from index 2 to the end
print(slicedGreetings) # 'llo World!'

slicedGreetings = greeting[2:5] # from index 2 to index 5
print(slicedGreetings) # 'llo '

slicedGreetings = greetings[6:12:1] # jump of 1
print(slicedGreetings) # 'World!'

slicedGreetings = greetings[6:12:2] # jump of 2
print(slicedGreetings) # 'Wrd'

slicedGreetings = greetings[::2] # iterates over the entire string with a jump of 2
print(slicedGreetings) # 'HloWrd'

slicedGreetings = greetings[::-1] # reverse the string!
print(slicedGreetings) # '!dlroW olleH'

""" len """

greetingsLength = len(greetings)
print(greetingsLength) #12

# len is a built-in function that returns us the actual lenght of our string

""" Concatenate """

# We also can concatenate strings
morning = "Good Morning "
name = "zerquiolin!"
greetings = morning + name
print(greetings) # 'Good Morning zerquiolin!'

""" Multiplication """

user = "zerquiolin"
print(user * 2) # 'zerquiolinzerquiolin'

""" Split """

user = "zerquiolin is god"
splittedUser = user.split()
print(splittedUser) # ['zerquiolin', 'is', 'god']

splittedUser = user.split('i')
print(splittedUser) # ['zerqu', 'ol', 'n ', 's god']

""" Aditional """

# We can set a tab by using \t
greetings = "Hello \t World!"
print(greetings) # Hello    World!

# We can set a break line by using \n
greetings = "Hello \n World!"
print(greetings)
# Hello
#  World!

# We have to keep in mind as we work with tabs and/or line breaks, once we use the len() function, it will count our '\t' characters as only one character!
# For example:

greetings = "Hello \n World!"
print(len(greetings)) # instead of getting 15 we are getting 14
```

There are a lot more functions whitin the strings ecosystem, but one thing we have to keep in mind is **Strings are NOT mutable**, we cannot change the value of a string by setting:

```python
greetings = "Hello World!"

greetings[11] = '.'

""" NO, this is completely WRONG! """
```

<br>

#### **String Interpolation**

This is a cool feature for injecting variable our strings!

so instead of:

```python
user = "zerquiolin"

print("Hello " + user) # Hello zerquiolin
```

We have two methods for this:

1. .format() method. <br>

2. f-strings (Formatted string literals)

<br>

**_.format()_**

the format method allows to inject variables into strings, by defining where the variable will go using {} inside the string we want to inject and then its value inside the parenthesis of the method.

Example:

```python
greetings =  "Hello {}".format('zerquiolin')

print(greetings) # Hello zerquiolin
```

We have to keep in mind this takes the value by the index position, so if we have three variables inside our string they will be set in order as we pass them on the method:

```python
greetings =  "Hello {}, how is your {} going?".format('zerquiolin', 'day')

print(greetings) # Hello zerquiolin, how is your day going?

""" Now let's change the order """
greetings =  "Hello {}, how is your {} going?".format('day', 'zerquiolin')

print(greetings) # Hello day, how is your zerquiolin going?
```

See the difference?

Now, we can actually set the order we want no matter the order we passed to the method:

```python
""" Index """

greetings =  "Hello {1}, how is your {0} going?".format('day', 'zerquiolin')

print(greetings) # Hello zerquiolin, how is your day going?

""" Repeated values """

greetings =  "Hello {0}, how is your {0} going?".format('day', 'zerquiolin')

print(greetings) # Hello day, how is your day going?

""" Variables """

# We actually can assign variables to our data:
greetings =  "Hello {user}, how is your {day} going?".format(day = 'day', user = 'zerquiolin')

print(greetings) # Hello zerquiolin, how is your day going?

""" Float formatin """

# This allow us to adjust the lenght and precition of our flotaing point number!
value =  "Value: {f:1.2f}".format(f = 106.123456789)
print(value) # 106.12
# This just allow us to show the lenght we want for our flaoting point variable.
value =  "Value: {f:1.6f}".format(f = 106.123456789)
print(value) # 106.123457

""" F-strings """

# This works pretty similar to the .format() method, the difference is by only setting and f before our string we can call every varible we want without a problem
user = 'zerquiolin'
question = 'How are you?'

greetings = f"Hello {user}! {question}"

print(greetings) # Hello zerquiolin! How are you?
```

<br>

### **Lists**

Lists are ordered sequences that can hold a variety of object types, they use square brackets [] and commas to separate the objects in the list:

```python
myList = [1,2,3,4,5]
```

List also support indexing and slicing. Lists can be nested and also have a variety of useful method that can be called off of them.

Let's make some examples:

```python
# Our lists can have any object type!

myList = ['string', 1, 5.0, True]

# We can also use indexing!

print(myList[0]) # 'string'
print(myList[1]) # '1'
# Reverse indexing also works fine!
print(myList[-1]) # 'True'

# We can also use slicing!

slicedList = myList[1:]

print(slicedList) # [1,5.0, True]

# We can also add new values to our list!
# We have to use the method .append(variable)

myList.append(False)
# We have to keep in mind once we append a new value it will be stored at the end of the list!
print(myList) # ['string', 1, 5.0, True, False]

# We can also reasign new values!

print(myList) # ['string', 1, 5.0, True, False]
myList[4] = True
print(myList) # ['string', 1, 5.0, True, True]
myList[4] = False
print(myList) # ['string', 1, 5.0, True, False]

# We can also delete values of our list!
# We have to use the method .pop(index), this method will return and delete the value we selected!
# This method have an index values of -1 by default, so if you call the method without any index value it will delete the last value stored

print(myList.pop()) # False
# Remember pop returns the value we chose and delete it from the list!

print(myList.pop(2)) # 5.0

# We can also nest lists!

numbersList = [1,2,3]
nestedList = [numbersList, numbersList, numbersList]

print(nestedList) # [ [1,2,3], [1,2,3], [1,2,3] ]

# How can we access our values?

print(nestedList[0][0]) # 1
print(nestedList[1][1]) # 2
print(nestedList[2][2]) # 3

# We can also sort our list by using the .sort() method

myList = [5,4,3,2,1]

print(myList) # [5,4,3,2,1]

myList.sort()

print(myList) # [1,2,3,4,5]
```

<br>

### **Dictionaries**

Dictionaries are unordered mappings for storing object; Dictionaries use a key-value pairing sequence!
This key-value pair allow us to quickly grab object without needing to know an index location.

This is their structure:

```
{ 'key': 'value', 'key1': 'value' }
```

Let's make some examples:

```python

# Our dictionaries could any object type we want!

myDictionary = { 'user': 'zerquiolin', 'code': 911, 'numList': [1,2,3], 'numDictionary': {'one': 1} }

# We can access our values by passing its key!

print( myDictionary['user'] ) # 'zerquiolin'
print( myDictionary['numList'] ) # [1,2,3]
print( myDictionary['numDictionary']['one'] ) # 1

# We can add object by refering to a new key and setting the value

print(myDictionary) # {'user': 'zerquiolin', 'code': 911, 'numList': [1, 2, 3], 'numDictionary': {'one': 1}}
myDictionary['newList'] = ['hi!','hola!']
print(myDictionary) # {'user': 'zerquiolin', 'code': 911, 'numList': [1, 2, 3], 'numDictionary': {'one': 1}, 'newList': ['hi!', 'hola!']}

# We can also reassign values by refering to the key and setting the value

print(myDictionary) # {'user': 'zerquiolin', 'code': 911, 'numList': [1, 2, 3], 'numDictionary': {'one': 1}, 'newList': ['hi!', 'hola!']}
myDictionary['user'] = "it's zerquiolin"
print(myDictionary) # {'user': "it's zerquiolin!, 'code': 911, 'numList': [1, 2, 3], 'numDictionary': {'one': 1}, 'newList': ['hi!', 'hola!']}

# If we want to retrieve the keys only we use .keys()

keys = myDictionary.keys()
print(keys) # dict_keys(['user', 'code', 'numList', 'numDictionary', 'newList'])

# If we want to retrieve the values only we use .values()

values = myDictionary.values()
print(values) # dict_values(["it's zerquiolin", 911, [1, 2, 3], {'one': 1}, ['hi!', 'hola!']])

# If we want to retrieve the items we use .items()

items = myDictionary.items()
print(items) # dict_items([('user', "it's zerquiolin"), ('code', 911), ('numList', [1, 2, 3]), ('numDictionary', {'one': 1}), ('newList', ['hi!', 'hola!'])])



```

<br>

### **Tuples**

Tuples are very similar to lists. However they have on key difference ~ **IMMUTABILITY**.

Once an element is inside a tuple it cannot be reassigned.

The tuples structure is parenthesis:

```
( 1, 2, 3)
```

Let's make some examples:

```python
# As tuples are very similar to list we can have different object types!

myTuple = ( 1, 'one', True, [1,2,3] )

# How can we access our values?

print(myTuple[0]) # 1
print(myTuple[2]) # True
print(myTuple[3]) # [1,2,3]

""" Built-In functions """

myTuple = ( 'a', 'a', 'b' )

# Tuples only have two functions:

# count
# returns the number of times an specific value is repeated

print(myTuple.count('a')) # 2

# index
# returns the number of times an specific value is repeated

print(myTuple.index('a')) # 0
# Returns the index of the first match
```

Tuples are often used to secure our data and be sure that a value will never change!
<br>

### **Sets**

Sets are unordered collections of **UNIQUE** elements.

Meaning there can only be one representative of the same object!
(You can only have one 'a', or one number 1 or so)

Let's make a quick example:

```python

mySet = {'hi'} # Using it this way, we must have at least one item!
# Or
mySet = set();

# How can we add values to my set?

print(mySet) # set()
mySet.add('zerquiolin');
print(mySet) # {'zerquiolin'}
mySet.add(911)
print(mySet) # {'zerquiolin', 911}
# It might look as a dictionary but it doesn't have keys!

# Our sets can only contain unique values, so if we try to add multiple repeated values it will only store the first one!

print(mySet) # {'zerquiolin', 911}
mySet.add(911)
print(mySet) # {'zerquiolin', 911}

# We also can cast our data!

myList = [1,1,1,1,2,2,2,2,3,3,3,3]
mySet = set(myList)
print(mySet) # [1,2,3]

```

<br>

### **Booleans**

Booleans are operators that allow us to convey **True** or **False** statements

Let's make some quick examples:

```python

print( 1 > 0 ) # True
print( 1 > 2 ) # False
print( 1 == 2 ) # False
print( 1 < 2 ) # True

```

<br>

### **Files**

Here we work with some of the basics of I/O over .txt files!

We can read and write information over a .txt file, but, how can we do that?

**Data.txt**

```
Hello
There!
How are you!?
```

**myFile.py**

```python
# As we want to read a file, we first need to open the file by using the open() method

myFile = open('Data.txt')

# How can we read our data?

print(myFile.read()) # 'Hello\nThere!\nHow are you!?'
# \n stands for a break line!

# There is something important here, as we already read the file, there is a pointer that stays at the end of the characters, so if we read the file again:

print(myFile.read()) #
# We got nothing!
# The way we can solve this problem is using the .seek(index) method, were by passing the index of the character you want to go the pointer will be redirected to that character as well!

myFile.seek(0) # here our pointer returned to the start!


""" IMPORTANT """

# As we are using our Data.txt file, once we end our processes we MUST close our file, otherwise it will still open in the background!

myFile.close()

# But here is a cool feature that allows you to be focused on more logic and processes than keeping an eye on closing the file when your done using it:

with open('Data.txt') as myFile:
   data = myFile.read()

# With that structure we are calling our file and assigning it to our variable 'myFile', this way, we don't actually need to be worried about closing the file!
# Also, notice there is an indentation, everything on that indentation will recognize our 'myFile' variable otherwise won't

# Now we know how to handle opening and assigning a file, but how can we correctly write and/or read?

# Inside our open() method there is a parameter called 'mode' which allows us to decide whether we want to read, write, or both!

# But first let's take look on its modes:
```

**Reading, Writing, Appending Modes**

1. mode = 'r' -> in read only
2. mode = 'w' -> is write only (will overwrite files or create new files)
3. mode = 'a' -> is append only (will add on to files)
4. mode = 'r+' -> is reading and writing
5. mode = 'w+' -> ia writing and reading (Overwrites existing files or creates new files)

```python
# Let's use the w mode to create a new file with text!

with open('newFile.txt', mode = 'w') as myFile:
   myFile.write('Hey This is my new File!');

# Once we get how this method works we can now implement advance features, for example, let's create a list bases on the content of our text file

 with open('newFile.txt', mode = 'w') as myFile:
    content = myFile.readlines()

# .readlines() method will return each line as a single value on a list object!

# Finally we have to keep in mind our path locations:

# Windows = C:\\Users\\UserName\\Folder\\Test.txt
# notice the doubel backslash

# Mac = /Users/UserName/Folder/Test.txt
```

<br>

<br><br>

## **Comparison Operators**

<br>

### **Basic Operators**

| Operator | Description                                                                                                                   |
| -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ==       | If the values of two operands are equal, then the condition becomes true.                                                     |
| !=       | If the values of two operands are not equal, then the condition becomes tre                                                   |
| >        | If the value of left operand is greater than the value of the right operand, then the condition becomes true                  |
| <        | If the value of left operand is less than the value of the right operand, then the condition becomes true                     |
| >=       | If the value of left operand is less greater than or equal to the value of the right operand, then the condition becomes true |
| <=       | If the value of left operand is less less than or equal to the value of the right operand, then the condition becomes true    |

<br>

### **Chained Comparison Operators**

We can use logical operators to combine comparisons:

- and
- or
- not

```python
""" AND """

print( (1 == 1) and (2 == 3) ) # False
print( ('one' == 'one') and (True) ) # True

""" OR """

print( (1 == 1) or (2 == 3) ) # True
print( ('one' == 'one') or (True) ) # True

""" NOT """

print(not True) # False
print(not(1 == 1)) # False
```

Keep in mind:

```python
# Once we set an operation like this:

2 <= 3 >= 1

# The first operator '2' has to fulfill the condition with the second operator '3' and the third operator '1' as well!

# Reestructuring the condition it would look like this:

( 2 <= 3 ) and ( 2 >= 1 )
```

<br>

<br><br>

## **Python Statements**

<br>

### **If ~ Elif ~ Else**

<br>

### **For loops**

<br>

### **While Loops**

<br>

### **Range()**

<br>

### **List Comprehensions**

<br>

<br><br>

## **Methods And Functions**

<br>

### **Methods**

<br>

### **Functions**

<br>

### **Lambda Expressions**

<br>

### **Nested Statements**

<br>

### **Scope**

<br>

<br><br>

## **Object Oriented Programming 'OOP'**

<br>

### **Objects**

<br>

### **Classes**

<br>

### **Methods**

<br>

### **Ineritance**

<br>

### **Special Methods**

<br>

<br><br>

## **Errors And Exception Handling**

<br>

### **Erros**

<br>

### **Exceptions**

<br>

### **Try**

<br>

### **Except**

<br>

### **Finally**

<br>

<br><br>

## **Modules And Packages**

<br>

### **Creating Modules**

<br>

### **Installing Modules**

<br>

### **Exploring The Python Ecosystem**

<br>

<br><br>

## **Built-In Functions**

<br>

### **Map**

<br>

### **Reduce**

<br>

### **Filter**

<br>

### **Zip**

<br>

### **Enumerate**

<br>

### **All ~ Any**

<br>

### **Complex**

<br>

<br><br>

## **Decorators**

<br>

<br><br>

## **Python Generator**

<br>

### **Iteration Vs Generation**

<br>

### **Creating Generators**

<br>

<br><br>

## **Advanced Lectures**

<br>

<br><br>

```

```
