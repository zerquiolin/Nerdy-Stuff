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

slicedGreetings = greeting[2:5] # from index 2 to index 4
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

Let's learn about control flow!
We often want certain code to execute when a particular condition has been met!

To control this flow of logi we use some keywords:

- if
- elif
- else

Control flow syntax makes uses of colons and indentation (whitespaces)
This indentation system is crucial to python and what sets it apart from other programming languages.

IF syntax:

```python
if condition:
   # CODE
else:
   # CODE

# The else statement declares what happens if we dont fulfill the if condition, but keep in mind we CAN'T chain multiple else statements, that stands for ELIF statements!
```

ELIF syntax:

```python
if condition:
   # CODE
elif:
   # CODE
elif:
   # CODE
else:
   # CODE
```

Let's make som quick examples:

```python
if 2 > 5:
   # CODE
elif 2 > 3:
   # Other CODE
else:
   # More CODE
```

<br>

### **For loops**

Many objects in python are 'iterable' meaning we can iterate over every element in the object!

We can use for loops to execute a block of code for every iteration!

<br>

**for loop syntax**:

```python
for variableName in objectName:
   # CODE
```

Let's make some quick examples:

```python
""" Variables """

myList = [ 1, 2, 3]

for data in myList:
   print(data) # 1 2 3

""" Strings """

word = 'Hello World!'

for letter in word:
   print(letter) # H e l l o W o r l d !

""" Tuple Unpacking """

myTupleList = [ (1,2), (3,4), (5,6) ]

# NORMAL
for value in myTupleList:
   print(value) # (1,2) (3,4) (5,6)

# UNPACKING
for a,b in myTupleList:
   print(a) # 1 3 5
   print(b) # 2 4 6

# Output: 1 2 3 4 5 6

# By destructuring or unpacking our tuple values into our selected variables, we can obtain each individual value instead of the entire parenthesis!
""" Library Unpacking """

myLibrary = { 'key': 'value', 'key0': 'value0' }

# NORMAL
for value in myLibrary:
   print(value) # 'key' 'key0'

# By default the for loop iterates on the keys only, if we want to retrieve the items we should use .items()

# ITEMS
for value in myLibrary.items():
   print(value) # ('key'; 'value') ('key0': 'value0')

# If we want to retrieve the values only we should use .values()

# VALUES
for value in myLibrary.values():
   print(value) # 'value' 'value0'

# But if we want to get both keys and values on separate variables inside the same for loop we can use the distructuring/unpacking functionality with .items() method

# UNPACKING
for key,value in myLibrary.items():
   print(key) # key key0
   print(value) # value value0

# Output: key value key0 value0
```

<br>

### **While Loops**

While loops will continue to executo a block of code **while** some condition remains true.

**While loop syntax**:

```python
while someBooleanCondition:
   # CODE
```

We also can combine while loops with else statements!

```python
while someBooleanCondition:
   # CODE
else:
   # Other CODE
```

let's make som quick examples:

```python
index = 0
while index < 5:
   print(f'The current index is: {index}')
   index += 1
else:
   print(f'The current index ({index}) is greather than 5')

# The index will make the condition true and the code inside the while will execute until the condition is no longer true!
# Once the condition turns False, the else code will execute once!
```

<br>

### **Keywords For Loops**

We have special keyword for our loops!

**Break**

The break will actually stop the loop and end its iterations no matter if the condition is still true or if the object was not fully iterated!

```python
user = 911
userIds = [1,911,123,404,200]

for code in userIds:
   if user == code:
      break
   print(code)

# Output: 1

# The foor loop will stop once the userId value is the same as the user!
```

**Continue**

Continue will skip the current cycle!

```python
user = 911
userIds = [1,911,123,404,200]

for code in userIds:
   if user == code:
      continue
   print(code)

# Output: 1 123 404 200

# The foor loop will skip the current cycle once the userId value is the same as the user!
```

**pass**

Will do nothing at all, but will help you avoid errors!

Imagine we are creating our app and decided to set a for loop but still don't know what the actual code inside that loop will be, so you code something like this:

```python
for value in 'Hello World!':
   # TODO
```

This is completely wrong and python will not accept it, instead, you can use the keyword 'pass' to avoid errors and still have the TODO loop:

```python
for value in 'Hello World!':
   # TODO
   pass
```

<br>

### **Usefuil Operator**

#### **Range**

We could Range to define lists, ranges, count and more!

_Range syntax:_

```python
range( initialIndex , finalIndex , jump )

# We can also only set the finalIndex

range( FinalIndex )

# As well as only the initialIndex and the finalIndex

range( initialIndex, finalIndex )
```

Let's make some quick examples:

```python

""" for loops """

for value in range(10):
   print(value)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

""" Lists """

myList = list(range(1:11))
print(myList)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
```

<br>

#### **Enumerate**

Enumerate allow us to keep an eye on the index cycle of our iteration, the way it works is returning a tuple with the current index and the values.

Let's make a quick example:

```python

myList = ['a', 'b', 'c']

for value in myList:
   print(value)

# Output:
# 'a'
# 'b'
# 'c'

# Now with enumerate
for value in enumerate(myList):
   print(value)

# Output:
# (0,'a')
# (1,'b')
# (2,'c')

# And we can also destructure our values!
for index, value in enumerate(myList):
   print(f'Value: {value} ~ Index: {index}')

# Output:
# Value: a ~ Index: 0
# Value: b ~ Index: 1
# Value: c ~ Index: 2

# Complex example:

myLibrary = {'key': 'value', 'key0': 'value0'}
for index, data in enumerate(myLibrary.items()):
   key, value = data
   print(f'Index: {index} ~ Key: {key} ~ Value: {value} ')

# Output:
# Index: 0 ~ Key: key ~ Value: value
# Index: 1 ~ Key: key0 ~ Value: value0
```

<br>

#### **Zip**

Zip help us to associate lists into tuples, meaning we can pair different lists, each tuple will contain the values of the same index, but we have to keep in mind if our lists are uneven the values that doesn't have a pair on the other lists will not be included.

_syntax:_

```python
zip(list0, list1, ...listn)
```

```python
list0 = [1,2,3,4]
list1 = ['one', 'two', 'three']

# Notice our lists are uneven!

zipList = zip(list0, list1)

# But we have to keep in mind once we use the zip method the result will be a zip object!
# To access its values we can use for loops or even parse its type (parse will be explained further in the course!)

print( list( zipList ) )

# Output: [(1, 'one'), (2, 'two'), (3, 'three')]

# or

for item in ziplist:
   print(item)

# Output:
# (1, 'one')
# (2, 'two')
# (3, 'three')
```

<br>

#### **In Operator**

In operator helps us know if an element is stored on a specific object by returning True or False!

_Syntax:_

```python
value in value0
```

let's make some quick examples:

```python
print( 'a' in 'How are you?' ) # True

myList = [1,2,3,4,5]
index = 0
print( index in myList ) # False

myLibrary = {'key': 'value', 'key0': 'value0'}
print( 'key' in myLibrary.keys() ) # True
```

<br>

#### **Min**

Min help to fin the minimum element of a list!

_syntax:_

```python
min(myList)
```

Let's make some quick examples:

```python
numbersList = [5,4,3,2,1]
lettersList = ['a', 'b', 'c', 'd', 'e']

print( min( numbersList ) ) # 1
print( min( lettersList ) ) # 'a'
```

<br>

#### **Max**

Max help to fin the maximum element of a list!

_syntax:_

```python
max(myList)
```

Let's make some quick examples:

```python
numbersList = [5,4,3,2,1]
lettersList = ['a', 'b', 'c', 'd', 'e']

print( max( numbersList ) ) # 5
print( max( lettersList ) ) # 'e'
```

<br>

#### **Random Library**

Random is a python built-in library that contains lot of important and useful functions!

<br>

##### **Shuffle**

Shuffle allows us to shuffle our list on much easier way, but we have to keep in mind the shuffle function doesn't return anything!

_Syntax:_

```python
# Before checking the syntax we have import our library!

# Import
from random import shuffle

# Syntax
shuffle(myList)

# Code
myList = [1,2,3,4,5]
print(myList) # [1,2,3,4,5]

# shuffle
shuffle(myList)
print( myList ) # [4, 1, 5, 2, 3]

# This is only one possibility, remember it shuffles it randomly!
```

<br>

##### **Radint**

Radint returns a random integer between the range we assign it to be!

_Syntax:_

```python
# Before checking the syntax we have import our library!

# Import
from random import randint

# Syntax
randint( intialIndex, finalIndex )
# Both initial and final index will be taken!

# Code
print( randint( 0, 5 ) ) # 3
print( randint( 0, 10 ) ) # 4
print( randint( 0, 100 ) ) # 30
print( randint( 0, 1000 ) ) # 566

# These are only some possibilities, remember its random!
```

<br>

#### **Input**

Once we want to retrieve some information from the user we could use the input() method, which allows us to access the input of the user via command prompt!

**We have to keep in mind each value the input method returns will be a string type!**

_Syntax:_

```python
# We have to keep in mind the input() method returns the actual value, so we have to store that data!

# Syntax
input( text ) # This text will be shown to the user!

# Code
userInput = input( "What's your name?" )
print( f'Hello {userInput}, I hope you are having a great day!' )

# Lets say our input is: zerquiolin, then the output will be:

# 'Hello zerquiolin, I hope you are having a great day!'
```

<br>

#### **Parse**

Once we encounter a situation where the types we have don't meet the requirements we need we need to change its types!

But how can we change types?

~ To change an object type we have to specify its new type and then wrap the object inside parentheses:

```python
value = '911'
number = int(value)
```

Let's make a quick example:

```python

input0 = int(input('first value'))
input1 = int(input('second value'))

print(f'{input0} + {input1} = {input0+input1}')

# Lets say our first input was: 5 and our second input was: 5, then our output will be:
# 5 + 5 = 10
```

<br>

in operator

min()

max()

shuffle (list) # from random import shuffle

randint(start,end) # from random import randint

input(text) always string

parse: int(value) float(value)

<br>

### **List Comprehensions**

List comprehensions are a unique way of quickly creating a list with python.

If you find yourself using a for loop along with .append() to create a list, _List Comprehensions_ are a good alternative!

_This topic is pretty tricky but once you get how it works everything will become more natural!_

Let's start by its syntax:

![image](ListComprehensionsSyntax.png)

As you can see, we have an expression that used to be inside the for loop, this expression if the proccess we want our item to follow and then return its result and save it into our list/set/library!

Normal view:

```python
for item in iterable:
   expression
```

Now, let's take a look at this example:

![image](ListComprehensionsExample.png)

As you can see, we have our Expression 'x\*\*2', for our loop that contains our item 'x' and our iterable 'range(0,50)' as well as an incorporated if statements!

So once we start iterating our range() element, for each cycle we are in, the item 'x' will be operated into its second power and returned!

But what is we want and else statement?

Let's make a quick example with if ~ else statements:

```python
print( list( 'even' if item % 2 == 0 else 'odd' for item in range(1,11) ) )

# Output: ['odd', 'even','odd', 'even','odd', 'even','odd', 'even','odd', 'even']
```

If we want to add another if statement we set the condition after the for statement:

```python
myList = [1,2,3,4,5,6,7,8,9]

print( list( 'even' if item % 2 == 0 else 'odd' for item in myList if item in [3,4,5,6] ) )

# Output: ['odd', 'even', 'odd', 'even']

# We have to keep in mind once we set our if statement after the loop we can't chain an else statement!!
```

Let's make some examples with list comprenhesions and its normal normal way, so you get the idea even better!

```python
""" First Example """

# List Comprenhnesions

myList = [ item for item in range(0,11) if item % 2 == 0 ]
print(myList) # 0 2 4 6 8 10

# Normal

myList = []
for item in range(0,11):
   if( item % 2 == 0 ):
      myList.append(item)
print(myList)

""" Second Example """

# List Comprehensions

myList = [ 'even' if item % 2 == 0 else 'odd' for item in range(1,11) ) ]
print(myList) # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Normal

myList = []
for item in range(1,11):
   if item % 2 == 0:
      myList.append('even')
   else:
      myList.append('odd')
print(myList) # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

```

We shouldn't code more complicated List Comprehensions than the ones we just did, the code gets messy and we sacrifice some readability!

Nevertheless, if you want to push yourself more with List comprehensions, here are some more complex examples:

```python

""" First Example """

# List Comprehensions

myList = [ 'even' if item % 2 == 0 else 'odd' for item in range(1,11) if item in [2,3,4,5,6,7,8] ]
print(myList) # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Normal

myList = []
for item in range(1,11):
   if item in [2,3,4,5,6,7,8]:
      if item % 2 == 0:
         myList.append('even')
      else:
         myList.append('odd')
print(myList) # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

""" Second Example """

# Nested if ~ else statements

# List Comprehensions

numbers = [1,2,3,4,5,6,7,8]
myList = [-1,0,1,2,3,4,5,6,7,8,9]

newList = [ 'one' if value == 1 else 'two' if value == 2 else 'other' for value in myList if value in numbers ]

print( newList ) # ['one', 'two', 'other', 'other', 'other', 'other', 'other', 'other']

# Normal

newList = []

for value in myList:
   if value in numbers:
      if value == 1:
         newList.append('one')
      else:
         if value == 2:
            newList.append('two')
         else:
            newList.append('others')

print( newList ) # ['one', 'two', 'other', 'other', 'other', 'other', 'other', 'other']

""" Third Example """

# Nested for loops

# List Comprehension

myList = [ x + y for x in range(0,4) for y in range(0,4) ]

print(myList) # [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6]

# Normal

myList = []

for x in range(0,4):
   for y in range(0,4):
      myList.append(x+y)

print(myList) # [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6]
```

<br>

<br><br>

## **Methods And Functions**

<br>

### **Methods**

Built-in object in python have a variety of methods you can use!

The most common one we have used is append() from the list object!

There is tons of method you can find on the [python documentation!](https://devguide.python.org/)

<br>

### **Functions**

Creating a clean repeteable code is a key part of becoming an effective programmer.

**Functions** allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire block of code!

<br>

#### **Def Keyword**

Creating a function requires a very specific syntax, including the _def_ keyword, correct indentation, and proper structure!

_Syntax:_

```python
def function_name():
   # code
```

Inside the parenthesis is where we are going to send the variables we want to interact with inside the function! For example:

```python
def function_name( name ):
   print( f'Hello {name}' )

function_name( 'zerquiolin' ) # zerquiolin
```

Notice we have a particular syntax on the function name, this is called snake case, is based on word divided by '\_' and in lower case, but you can choose to use it or not, its totally optional!

We also have somethig called **Return** which allow us to send back the result of the function and assign its output to a new variable. For example:

```python
def function_name():
   return 'Hello World!'

greetings = function_name()

print(greetings) # Hello World!
```

<br>

#### **Basic Of Functions**

We have seen some examples of functions, but lets take a look at this case:

```python
def function_name( name ):
   print( f'Hello {name}' )

function_name() # Here we will get an error because we didn't sent any values for the name parameter!
```

But there is a way to handle this situation, we can set default values for our parameters!

```python
def function_name( name = 'default' ):
   print( f'Hello {name}' )

function_name() # Hello default
```

Now let's create a quick example where we can see the functions on a real situation:

We will create function that returns the even number of the given list!

```python
numbersList = [1,2,3,4,5,6,7,8,9,10]

def even_numbers( iterable ):
   temporalList = []

   for number in iterable:
      if number % 2 == 0:
         temporalList.append(number)

   return temporalList

evenNumbersList = even_numbers( numbersList )

print( evenNumbersList ) # numbersList
```

<br>

#### **Functions And Tuple Unpacking**

To comprehend better our functions let's make a function that returns the employee of the month based on a list that contains tuples, each tuple contains the name and the hours each person worked through the month:

```python

workers = [ ('Zerquiolin', 911), ('Nadiv', 900), ('David', 850), ('Nicolas', 800) ]

def employee_of_the_month( employees ):

   maxHours = 0
   winer = ''

   for employee, hours in  employees:
      if hours > maxHours:
         winer = employee
         maxHours = hours

   return (winer, maxHours)

results = employee_of_the_month(workers)
print( results ) # ('Zerquiolin', 911)
```

<br>

#### **args & kwargs**

Imagine you are creating a function and suddenly you encounter a situation where you have to pass n variables as parameters, but you don't have the exact amount it's going to be passed!

What could we do in this situation?

As you may know we can set optional parameters, let's make and example where we add each value we get!

```python
def add( a, b, c=0, d=0, e=0 ):
   return ( a+b+c+d+e )
```

As you can see, we set 'c', 'd' and 'e' as optional parameters, so we have no problem using 2 to 5 variables in our function, but what if we have more than 5, or more than 10, 100, 1000?
That gets a little complicated and long doesn't it?

Luckily we have a solution called **\*args**, it takes all the variables the user pass to the function and create a tuple with them:

Let's refactor our add function:

```python
def add( *args ):
   return ( sum(args) )
```

See how easy it was to improve our code and accept n variables?

But don't worry you don't necessarily must call the variable 'args' what makes the magic is the star before the variable name!

You can use whatever you want:

```python
def add( *whatMattersIsTheStar ):
   return ( sum(whatMattersIsTheStar) )
```

We also have **\*\*kwargs** (keyword args), as **\*args** created a tuple, **\*\*\*kwargs** creates a library!

_They work the same!_

The difference is based on assigning values to the variables passed!

Let's create a quick example where we create a library based on a employees list:

```python
def createEmployees( **lib ):
   print( lib )

printEmployees( e0 = 'Nadiv', e1 = 'Andres', e2 = 'David', e3 = 'Camila', e4 = 'Daniel',)

# Output {'e0': 'Nadiv', 'e1': 'Andres', 'e2': 'David', 'e3': 'Camila', 'e4': 'Daniel'}
```

And yes!
We can use both **\*args** **\*\*kwargs** in the same function!

```python
def mixArgs( *args, **kwargs ):
   print(args)
   print(kwargs)
```

But we have to keep in mind we can't change between _\*args_ and _\*\*kwargs_ values:

We can NOT do this:

```python
mixArgs( 1,2,3, name = 'zerquiolin', 4, hola = 'hello' )
```

It is completely incorrect, we first need to set our \*args values and then our \*\*kwargs values!

We should do this instead:

```python
mixArgs( 1,2,3,4, name = 'zerquiolin', hola = 'hello' )
```

<br>

### **Lambda Expressions**

Lambda expressions are a way to quickly create one time use functios that you don't really name, use them one time and never use them again!

Let's take a look on map and filter before moving on!

#### **Map**

The map function helps us to map over each item on the list and make a process on them, but this does not affect the original list, so we can save the result parsing it into a list or more!

Syntax:

```python
map( function, iterable )
```

Let's make some quick examples:

```python
def square( number ):
   return number ** 2

numsList = [1,2,3,4,5,6,7,8,9]
squareNumsList = list( map( square, numsList ) )

print( squareNumsList )
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

_Notice once we pass our function, we didn't send the parameters, map will get the parameters by itself as you reference the iterable!_

You can also do complex proccesses:

```python
def isEven( number ):
   return {number: True if number % 2 == 0 else False}

numsList = [1,2,3,4,5,6,7,8,9]
evenNumsList = list( map( square, numsList ) )

print( evenNumsList )
# Output: [{1: False}, {2: True}, {3: False}, {4: True}, {5: False}, {6: True}, {7: False}, {8: True}, {9: False}]
```

<br>

#### **Filter**

Filter works pretty similar to map, the difference lies in returning only the items or values that meet the requirements we passed in, we are filtering out our values!

Syntax:

```python
map( function, iterable )
```

_We have to keep in mind, our function must return true or false so our value can be returned, otherwise, it won't work!_

<br>

Let's recreate the example of the even number we did on map, but using filter instead:

```python
def checkEven( number ):
   return number % 2 == 0

numsList = [1,2,3,4,5,6,7,8,9]
evenNumsList = list( filter( checkEven, numsList ) )

print( evenNumsList )
# Output: [2,4,6,8]
```

<br>

Now that we have clear the uses of map and filter functions, we can create anonymous functions (lambda expressions!)

Let's start by converting this function :

```python
def square( num ):
   return num ** 2
```

into a lambda expression:

```python
lambda num: num ** 2
```

Notice we got rid of the _def_ keyword and the parenthesis of the parameters, as well as the _return_ keyword!
This is a lambda expression, we don't usually give it a name because they are thought of as a one-time use!

Lambda expressions work by defining a variable after the keyword _lambda_, then, after the colon, we encounter the expression where the value we were given is processed and later returned!

Nevertheless, if you want to give it a name:

```python
square = lambda num: num ** 2
```

Lambda expressions are useful when using map and filter functions!

Let's make some quick examples:

```python

nums = [1,2,3,4,5,6,7,8,9]

""" Map """

print( list( map( lambda number: number ** 2, nums ) ) )
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
print( nums )
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

""" Filter """

print( list( filter( lambda number: number if number % 2 == 0 else number ** 2 ), nums ) )

```

<br>

### **Nested Statements & Scope**

Once you create a varible it gets stored in whats called the name space, and each variable has a _scope_!
The _scope_ determines the visibility of our variables in other parts of our code!

Variables follow the **LEGB Rules**:

- **L** ~ Local
  - Names assigned in any way within a function (def or lambda) and not declared global in that function.
- **E** ~ Enclosing function locals
  - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
- **G** ~ Global (module)
  - Names assigned at the top-level of a module file, or declared global in a def whitin the file!
- **B** ~ Built-in (python)
  - Names preassigned in the built-in names module: open, range, SyntaxError, ...

Keep in mind this is the actual order python will looking!

Let's create a basic example:

```python
# Let's create a 'global', 'enclosing' and 'local' variables!
# Enclosing function local variables are just functions inside functions!

""" Global variable """

word = 'Global variable'


def printWord():

   """ Enclosing function local """

   word = 'Enclosing function' # This is a local variable for printWord()!

   def newWord():

      """ Local variable """

      word = 'Local'# This is a local variable for printWord()!
      print( f"I'm a {word}" )

   newWord()

printWord()
```

Notice we have a _global_, _enclosing_ and _local_ variable with the same name, but how can we know which value will take?<br>
It all depends on the name space, let's look at the **LEGB** rules, this rules state a specficic pattern or order to follow, so let's imagine we are at level 0 inside the _print()_ method on the **_newWord()_** function and the nearest **_'word'_** variable we have is the 'local' variable within this function with a value of 'Local variable', so this is the value it will take, but what if we comment out that local variable? <br>
Well, As the scope of the **_'word'_** variable inside the **_printWord()_** function _enclosures_ the **_newWord()_** function the _print()_ method will jump one level up and adquire its value ('Enclosing function')!<br>
And again, what happens if we comment out this variable? <br>
As we have a _global_ variable also called **_word_** that enclosures our **_printWord()_** function, the _print()_ method will jump one level up and get its value ('Global variable')!

<br><br>

Now we have certain knowledge of scope and nested statements, we need to keep something really **important** in mind!

<br>

If we declare a local variable that already exits globaly, once we update that variable, the update will only occur locally, because of its scope and it wont be able to extend to another name space level!

```python
""" Global """

name = 'zerquiolin'

def printName():

   """ Local """

   name = "it'szerquiolin"

   print(name)


"""
As you can see, we have to variables with the same name but different scope, so let's try printing them out to see the magic!
"""

print( name ) # 'zerquiolin'

printName() # "it'szerquiolin"

print( name ) # 'zerquiolin'
```

Due to the scope of local variables we cannot affect global variables, but there is a way!
Using the keyword **global** before the local assignment we assure the variable we just declared will be taken from the global name space!

```python
""" Global """

name = 'zerquiolin'

def printName():

   """ Global in Local """

   global name # Declaring the global variable

   name = "it'szerquiolin" # Updating the global variable!

   print(name)


"""
As you can see, we just declare locally our global variable and updated it, now lets try printing them out to see the magic!
"""

print( name ) # 'zerquiolin'

printName() # "it'szerquiolin"

print( name ) # "it'szerquiolin"
```

_And that if how you locally reassign a global variable!_

Nevertheless, it's recommended to use a more basic method, requiring the global variable via parameters and returning its new value!

```python
""" Global """

name = 'zerquiolin'

def printName(name):

   name = "it'szerquiolin" # Updating the global variable!

   return name

print( name ) # 'zerquiolin'
name = printName(name)
print( name ) # "it'szerquiolin"
```

This method is often used with larger scripts, so this way you can easily debug your code and prevent accidental updates!

<br>

<br><br>

## **Object Oriented Programming 'OOP'**

<br>

Object Oriented Programming (OOP) allows programmers to create their own objects that have methods and attributes.

Recall that after defining a string, list, dictionary, or other objects, you were able to call methods off of them with the .method_name() syntax.

In general, OOP allows us to create code that is repeatable and organized.

For much larger scripts of python code, functions by themself aren't enough fo organization and repeatability.

Commonly repeated tasks and objects can be defined with OOP to create code that is more usable!

_let's check the syntax:_

```python
# Let's start by the 'class' keyword, this is what defines an object

class NameOfClass():
   # Notice we use camel case, it's usually used for classes name just as it's usually used snake case for functions! but don't worry, you can use whatever you feel comfortable with

   # We also have an special method called __init__() this allows us to create an instance of the actual object!
   def __init__(self, param1, param2):
      # Notice we have a 'self' keyword and two parameters, the self keyword help us to link parameters directly to the instance, we assign that value to an attribute of the object, this way we know we are refering to the variables passed on the instance and not a global variable
      self.param1 = param1
      self.param2 = param2


   # We can also link methods/functions to this class by passing self as a parameter!

   def method_name(self):
      # CODE
      print(self.param1)
      # remember we link the param1 to the class?
      # This way python knows you are calling the connected attribute and not a global variable
```

We just saw a brief example and explanation of classes, but now let's take a closer look!

As you know what defines an object is the keyword 'class', and inside our object have to use the '\_\_init\_\_()' method, where we pass in the 'self' keyword that connects that method to our object as well as our parameters, keep in mind the init method its automaticly runned when we call the class, creating a new instance!

But there is something important we need to know...

**_attributes_**

The attributes are basically variables linked to our object and unique for each instance of the class, how can we define them?

Remember we used the 'self' keyword to link the init method, we can use to link our own methods and attributes!

```python
class Dog():
   # By using the class keyword we are creating a dog object!

   # Let's define our init method
   def __init__(self, breed, name, spots):
      self.breed = breed
      self.name = name
      self.spots = spots
      # Here we just created our object attributes!
      # Notice our attributes have the same name as the parameters of the init method, this is a common and good practice, nevertheless, you can call and assign your attributes to whatever you want!

   # Let's create and link our method
   def greet(self):
      return f"Hi! my name is {self.name} and I'm a {self.breed} dog! Nice to meet you!"
   # By passing in the self keyword we are linking that method to our object!



   """
   There is one important topic, just as we have the facility of dynamic typing we can't assure the right values will be passed to our object, so we have to document all related to our object for other programmers to understand and send correct values!
   Luckily there is a way we will see later in the course!
   """
```

We also have...

**Class Object Attributes**

This work just as the normal attributes, but they will be the SAME for each instance of the class, and we don't have to use the self keyword to define them, by declaring the attributes before the init method we are defining our _Class Object Attributes_!

Example:

```python
class Dog():
   # Class Object Attributes
   bark = 'guau'

   def __init__(self, name):
      self.name = name

   def methodName(self):
      # now we have two ways to call the class object variables

      # By using self
      print( self.bark )

      # By using the class name
      print( dog.bark )

      # They will work the same!
```

Last but not least important a brief explasnation of methods...

**Methods**

Methods are just functions inside a class and can be called by refering to the object and a thot to access its methods!

Quick example:

```python
class Dog():
   # Class Object Attributes
   bark = 'guau'

   def __init__(self, name):
      self.name = name

   # Remember when creating methods/functions we are just going to create operations and can ask for values/parameters to simplify our code or even have more information!
   # Rememer we can also set default values for our parameters in case its not needed to send values
   def methodName(self, number=1, day='monday'):
      return f'Hi! My name is {self.name}, today is {day} and my number is {number}! {dog.bark}! {dog.bark}!'
```

Now that we have the basics let's create an example where we create and call our class:

```python
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
```

<br>

### **Inheritance**

Inheritance allows us to create new classes based on classes that already have been defined.

One benefit of using inheritance is reusing code and reduce the complexity of a program!

We have our principal/mold class that will allow us to create derivated or secondary classes:

```python
class Animal():

   def __init__(self):
      print('Animal created')

   def eat(self):
      print("I'm eating")
```

Now imagine we want to secondary class based on our primary class, we want to inherit its methods and attributes, so we use _inheritance_:

To use inheritance we must pass in the class object inside the parameter of the secondary class and create a new instance inside its _init_ method:

```python
class Dog( Animal ): # Notice we are passing in the primary class we want to inherit from!

   # Now for our inheritance to work, we need to create its instance inside the init method
   def __init__(self):
      Animal.__init__(self)

   # Now once created an instance of 'dog', we can call the methods from 'Animal'

   # And as normal we can create our own methods!
   def bark(self):
      print('woof woof')
```

```python
myAnimal = Animal() # 'Animal created'
myAnimal.eat() # "I'm eating"

myDog = Dog() # 'Animal created'
myDog.bark() # 'woof woof'
myDog.eat() # "I'm eating"
# See? We used an Animal method calling it from a Dog object!
# We successfully inherit the properties of Animal!
```

But, what if we want our eat method behaves differently inside our Dog object?
We can rewrite the method by calling it the same way on our Dog's object!

```python
class Dog( Animal ): # Notice we are passing in the primary class we want to inherit from!

   # Now for our inheritance to work, we need to create its instance inside the init method
   def __init__(self):
      Animal.__init__(self)

   # Now once created an instance of 'dog', we can call the methods from 'Animal'

   # And as normal we can create our own methods!
   def bark(self):
      print('woof woof')

   # Here we will rewrite the eat method from the Animal object!
   def eat(self):
      print("I'm a dog and I'm eating!")
```

```python
myAnimal = Animal() # 'Animal created'
myAnimal.eat() # "I'm eating"

myDog = Dog() # 'Animal created'
myDog.bark() # 'woof woof'
myDog.eat() # "I'm a dog and I'm eating!"
# See? We successfully make the eat method from Animal have a different behavior inside the Dog's class!
```

<br>

### **Polymorphism**

In python polymorphism, ferers to the way in which different object classes can share the same method name!

Let's create an example with two different classes but with a method in common called 'speak'

```python
class Dog():
   def __init__(self, name):
      self.name = name

   def speak(self):
      return self.name + " says woof!"

class Cat():
   def __init__(self, name):
      self.name = name

   def speak(self):
      return self.name + " says meow!"

"""
Now that we have two different classes with a method that has the same name we can demostrate polymorphism
"""

# Let's iterate over a list of Pets containing dogs and cats, and call the same method!

myDog = Dog('Rambo')
myCat = Cat('Snowball')
pets = [myDog, myCat]

for pet in pets:
   print(pet.speak()) # Notice we don't mind which object is currently on the pet variable, we are just calling its eat method, and since both of the objects have this method, everything will work and we will have created our first polymorphism example!

# Output:
# Rambo says woof!
# Snowball says meow!
```

The most common used for polymorphism is using **Abstract Clasess** and **Inheritance**!

<br>

### **Abtract Classes**

What an abstract is, its never expected to be instantiated, its though as being a base class only!

Remeber on our examples of inheritance, we inherit a class and instantiated it as well?
In abstract classes we don't create a new instance, the objective of abstract classes is to be a template for different classes!

Let's create our template class!

```python
class Animal():

   def __init__(self, name):
      self.name = name

   def speak(self):
      # Since this is a template method, we are not going to create any proccesses, we are going to throw an error, so once we create our subclass we must overwrite it!
      raise NotImplementedError('Subclass must implement this abstrac method!')

      """

      Don't worry, we will take care of errors later in the course!

      """
```

Now, if we try to create an instance of this class we will for sure can, but each of its methods will throw an error and will not be useful, remember we are using it as a **Template!**

```python
myAnimal = Animal('Pepe')
myAnimal.speak() # Error Thrown!
```

Now let's create two subclasses of _Animal_:

```python
class Dog(Animal): # We are inheriting from our abstract class!

   # Since we are using our Animal template, we don't necessarily need to implement the init method!

   # Now as we know, we have an unimplemented method called speak, so now we are going to overwrite it to avoid the error and create our own functionality!

   def speak(self):
      print( f"Hello I'm {self.name}" )

# Now let's make the same procces for our second subclass
class Cat(Animal):

   def speak(self):
      print(f"Hello I'm {self.name}")
```

Now let's instance them and call its methods!

```python
myDog = Dog('Rambo')
myCat = Cat('Snowball')

myDog.speak() # "Hello I'm Rambo"
myCat.speak() # "Hello I'm Snowball"
```

<br>

### **Special/Magic/Dunder Methods**

As you know we have built-in methods like _len_ _del_ _print_ _str_ and many more, but if we try to use them with our own objects they will just simply not work!

Let's create an example with a Book object:

```python
class Book():

   def __init__(self, name, author, pages):
      self.name = name
      self.author = author
      self.pages = pages


"""
So if we try to use some of the built-in methods, we will get an error!
"""

myBook = Book('My Story', 'zerquiolin', 911)

len(myBook) # Error Thrown!
print(myBook) # Error Thrown!
del(myBook) # Error Thrown!

"""
But don't worry!
We can handle all these uses and avoid getting an error, as you know, we have our init method inside our classes that allows us to create our instances, well, as init there are tons of useful methods as well!

We can use __len__ method to set a return for whenever a len() is called for our method!

We can use __str__ method to set a return for whenever we want to use the str() method to parse our object or the print() method to print our object!

We can use __del__ method to set a behavior once our object is deleted!
"""
```

So let's create our new updated and functional object!

```python
class Book():

   def __init__(self, name, author, pages):
      self.name = name
      self.author = author
      self.pages = pages

   # Len method handler
   def __len__(self):
      return self.pages # Returns the amount of pages!

   # str method handler
   def __str__(self):
      return f'{self.name} written by {self.author}: {self.pages} pages.'
      # Returns the string version of our object!

   # del method handler
   def __del__(self):
      print(f'{self.name} has been successfully deleted!')



"""
Let's test our brand new object!
"""

myBook = Book('My Story', 'zerquiolin', 911)

len(myBook) # 911
print(myBook) # 'My Story written by zerquiolin: 911 pages.'
del(myBook) # 'My Story has been successfully deleted!'
```

<br>

<br><br>

## **Modules And Packages**

<br>

### **Pip Install ~ PyPi**

_PyPi_ is a repository for open-source third-party Python packages.

It's similar to RubyGems in the ruby world, PHP's packagist, CPAN for Perl, and NPM for Node.js

So far we have user built-in packages, but there are so other libraries available that people have open-sourced and shared on PyPi.

We can use **pip install** at the command line to install these packages!

By installing python from python.org or through the Anaconda distribution you also installed **pip**!

**pip** is a simple way to download packages at your command line directly from the PyPi repository!

There are packages already created for almost any use case you can think of!

Let's make a quick example downloading and installing external packages!

On the terminal type:

```
pip install 'Package Name'
```

Now let's install a package that allows us to work with excel files!

Let's use [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

```
pip install openpyxl
```

And now we can easily import the package!

```python
import openpyxl
```

<br>

### **Own Modules & Packages**

Modules are just .py scripts that you call in another .py script!

Packages are collections of modules.

Let's make some examples:

We will create a .py file called 'myModule' that will contain the functions we will later call in another file.

_*myModule.py*_:

```python
def myFunc():
   print("I'm a function inside myModule!")
```

Now let's import our module and use its functions!

_*myProgram.py*_:

```python
from myModule import myFunc

myFunc() # I'm a function inside myModule!
```

We now have successfully created our own module!
But, later on we might have a lot more functions and files that work together, and that's when we create our packages.

Let's create a package!

To create a package we only need to set a folder and a \_\_init\_\_ file in order for python to recognize that folder as a package, but it's not necessary to contain data in the file, it just works as a reference!

For example:

Let's create a folder called _myPackage_ and inside the folder we will have another folder called _subPackage_, don't forget to add the \_\_init\_\_ file inside the folders to be recognized as packages!

Now, let's create a file inside each of those folders, containing the following data:

_File_ on _myPackage_

```python
def myFunc():
   print("I'm inside the myPackage")
```

_SubFile_ on _subPackage_

```python
def myFunc():
   print("I'm inside the subPackage")
```

Now let's create a separate file importing them:

```python
from myPackge import File
from myPackge.subPackage import SubFile

File.myFunc() # "I'm inside the myPackage"
SubFile.myFunc() # "I'm inside the subPackage"
```

<br>

### **\_\_name\_\_ and \_\_main\_\_**

After having a deeper understanding over python and its functionalities you might encounter something like this:

```python
if __name__ == '__main__':
   pass
```

Somethimes when you are importing from a module, you would like to know wheter a modules function is being used as an import, or if you are using the original .py file of that module.

Lets's create some examples:

Let's create two files:

_one.py_

```python
print(' This is one.py file ')

def func():
   print("Function at one.py!")

"""
__name__ name is a built-in variable that allows us to determine whether the current file is either imported or not!

Once the file runs if it is the current file and not imported it will be assigned as '__main__' otherwise it won't
"""

if __name__ == '__main__':
   # Here we will execute some code as we know the file is being ran and not imported

   print( "I wasn't imported" )
else: # It's not common to use an else statement in this case, but for getting how it works we are using it!
   print("I was imported")
```

_two.py_

```python
import one

one.func()

print(' This is two.py file ')

if __name__ == '__main__':
   # Here we will execute some code as we know the file is being ran and not imported

   print( "I wasn't imported" )
else: # It's not common to use an else statement in this case, but for getting how it works we are using it!
   print("I was imported")
```

Now if we run our file we will get:

_one.py_

```python
' This is one.py file '

"I wasn't imported"
```

_two.py_

```python
' This is one.py file '

"I was imported"

"Function at one.py!"

' This is two.py file '

"I wasn't imported"
```

A common use of this conditional is to run scripts:

```python
def funct0():
   pass
def funct1():
   pass
def funct2():
   pass

if __name__ == "__main__":
   funct0()
   funct1()
   funct2()
```

<br>

<br><br>

## **Errors And Exception Handling**

<br>

Errors are bound to happen in your code, especially when some else ends up using it in an unexpected way!

We can use error handilng to attempt to plan for possible errors!

For example, a user may try to write to a file that was only opened in mode='r'.<br>
Currently if there is any type of error in your code, the entire script will stop, and we don't want that!

So we can use Error Handling to let the script continue with other code, if there is an error!

There is three keywords for this:

1. **try**
   - This is the block of code to be attempted (may lead to an error).
2. **except**
   - Block of code will execute in case there is an error in try block.
3. **finally**
   - A final block of code to be executed, regardless of an error.

Let's make an example:

```python
def add(a,b):

   # We are going to handle each error it might occur will adding a + b
   # For example: we CAN'T add a string with a integer, that will generate an error and we need to handle it

   # Let's use our try block, where is going to 'try' the code inside
   try:
      result = a + b
   # If our result gets an error we could handle it by using except!
   except:
      print('The values provided were not correct!')
   # We can chain different exception based on its type!
   # We could OSErrors, ArithmeticError, LookupError and so much more!
   # And we CAN have a different aproach to each error
   except BufferError:
      # Some code
      pass
   except LookupError:
      # Some code
      pass
   except OSError:
      # Some code
      pass
   # If it didn't occur an error we also can chain an else statement rigth after the except block!
   else:
      print(result)
   # We also have an always run block called 'finally', this block will run no matter an error occurred or not!
   finally:
      print( 'I will always run no matter what!' )
```

<br>

### **PyLint overview**

<br>

### **Running Tests With Unittest Library**

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
