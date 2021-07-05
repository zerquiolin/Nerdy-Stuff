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

### **Lists**

<br>

### **Dictionaries**

<br>

### **Tuples**

<br>

### **Files**

<br>

### **Sets**

<br>

### **Booleans**

<br>

<br><br>

## **Comparison Operators**

<br>

### **Basic Operators**

<br>

### **Chained Comparison Operators**

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
