st = 'Print only the words that start with s in this sentence'
for value in st.split():
    if value[0].lower() == 's':
        print(value)


print( list(range(0,11,2)) )

print( list(item for item in range(1,51) if item % 3 == 0) )


st = 'Print every word in this sentence that has an even number of letters'
for value in st.split():
    if len(value) % 2 == 0:
        print(f'value: {value} is even!')

print( list( 'FizzBuzz' if item % 3 == 0 and item % 5 == 0 else 'Buzz' if item % 5 == 0 else 'Fizz' if item % 3 == 0 else item  for item in range(0,101) ) )



st = 'Create a list of the first letters of every word in this string'
print( list( word[0] for word in st.split() ) )














myList = [ number for number in range(0,101,2) ]

print(myList)
















