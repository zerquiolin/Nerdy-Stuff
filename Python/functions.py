# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens( a,b ):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    
    return max(a, b)


print( lesser_of_two_evens(2,4) ) # 2
print( lesser_of_two_evens(2,5) ) # 5

# Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers( text ):
    a,b = text.lower().split()
    
    return a[0] == b[0]


print(animal_crackers('Levelheaded Llama')) # True
print(animal_crackers('Crazy Kangaroo')) # False

# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty( n1,n2 ):
    return ( n1 + n2 == 20 ) or ( n1 == 20 or n2 == 20)


print(makes_twenty(20,10)) # True
print(makes_twenty(12,8)) # True
print(makes_twenty(2,3)) # False

# Write a function that capitalizes the first and fourth letters of a name

def old_macdonald( name ):

    return "".join( [name[:3].capitalize(), name[3:].capitalize()] )


print(old_macdonald('macdonald')) # MacDonald

# Given a sentence, return a sentence with the words reversed

def master_yoda( text ):
    return " ".join(text.split()[::-1])


print(master_yoda('I am home')) # 'home am I'
print(master_yoda('We are ready')) # 'ready are We'

# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there( n ):

    return ( abs(n-100) <= 10 or abs(n-200) <= 10 )


print(almost_there(90)) # True
print(almost_there(104)) # True
print(almost_there(150)) # False
print(almost_there(209)) # True

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33( nums ):

    for index in range(0,len(nums)-2):
         if nums[index: index+2] == [3,3]:
             return True
    
    return False


print(has_33([1, 3, 3])) # True
print(has_33([1, 3, 1, 3])) # False
print(has_33([3, 1, 3])) # False

# Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    newText = ''
    for letter in text:
        newText += letter*3

    return newText

print(paper_doll('Hello')) # 'HHHeeellllllooo'
print(paper_doll('Mississippi')) # 'MMMiiissssssiiippppppiii'

# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST

def blackjack(a,b,c):
    result = sum([a,b,c])

    if result <= 21:
        return result
    elif result <= 31 and 11 in [a,b,c]:
        return result-10
    else:
        return 'BUST'


print(blackjack(5,6,7)) # 18
print(blackjack(9,9,9)) #'BUST'
print(blackjack(9,9,11)) # 19

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):

    result = 0
    breaker = False
    
    for number in arr:
        if breaker:
            if number == 9:
                breaker = False
            continue
        else:
            if number == 6:
                breaker = True
                continue

            result += number

    return result


print(summer_69([1, 3, 5])) # 9
print(summer_69([4, 5, 6, 7, 8, 9])) # 9
print(summer_69([2, 1, 6, 9, 11])) # 14

# Write a function that takes in a list of integers and returns True if it contains 007 in order

print('here')
def spy_game(nums):
    
    secret = [0,0,7,'done']

    for number in nums:
        if number == secret[0]:
            secret.pop(0)

    return len(secret) == 1


print(spy_game([1,2,4,0,0,7,5])) # True
print(spy_game([1,0,2,4,0,5,7])) # True
print(spy_game([1,7,2,0,4,5,0])) # False

# Write a function that returns the number of prime numbers that exist up to and including a given number. (By convention, 0 and 1 are not prime)

def count_primes(num):
    final = 0
    breaker = False

    for number in range(2,num):
        for div in range(2,number):
            if number % div == 0:
                breaker = True
        
        if breaker:
            breaker = False
            continue
        else:
            final += 1
       
    return final


print(count_primes(100)) # 25
print(count_primes(1000)) # 168

# Write a function that takes in a single letter, and returns a 5x5 representation of that letter. (For purposes of this exercise, it's ok if your dictionary stops at "E")

def print_big( letter ):
    alphabet = {
        'a': [[2],[1,3],[0,1,2,3,4],[0,4],[0,4]],
        'b': [[0,1,2,3,4],[0,4],[0,2,3],[0,4],[0,1,2,3,4]],
        'c': [[0,1,2,3,4],[0],[0],[0],[0,1,2,3,4]],
        'd': [[0,1,2,3],[0,4],[0,4],[0,4],[0,1,2,3]],
        'e': [[0,1,2,3,4],[0],[0,1,2],[0],[0,1,2,3,4]]
        }

    result = ''

    for y in range(0,5):
        for x in range(0,5):
            result += '*' if x in alphabet[letter][y] else ' '

        result += '\n'

    return result

print(print_big('a'))
print(print_big('b'))
print(print_big('c'))
print(print_big('d'))
print(print_big('e'))

# Another version


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

        


""" Methods And functions """

import math

# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as (4/3) * π * r^3

def vol(rad):
    return (4/3) * math.pi * rad**3


print( vol(2) ) # 33.510321638291124

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_bool(num,low,high):
    return num >= low and num <= high


print( ran_bool(3,1,10) ) # True

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# HINT: Two string methods that might prove useful: .isupper() and .islower()

def up_low(s):
    upper = 0
    lower = 0

    for letter in s:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return {'upper': upper, 'lower': lower}

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print( up_low(s) ) # ( {'upper': 4, 'lower': 33} )

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list( set( lst ) )


print( unique_list([1,1,1,1,2,2,3,3,3,3,4,5]) ) # [1, 2, 3, 4, 5]

# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):  
    res = 1

    for number in numbers:
        res *= number

    return res


print( multiply([1,2,3,-4]) ) # -24

# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

def palindrome(s):
    
    return s.replace(' ', '').lower() == s.replace(' ', '').strip().lower()[::-1] 


print( palindrome('helleh') ) # True

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string

# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(str1.lower().strip().replace(' ','')).intersection(set(alphabet)) == set(alphabet)


print( ispangram("The quick brown fox jumps over the lazy dog") ) # True