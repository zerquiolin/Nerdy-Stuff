# 0 1 2
# 0 1 3
# 0 2 2
# 0 2 3

# 1 1 2
# 1 1 3
# 1 2 2
# 1 2 3

# 3 4 4 5 4 5 5 6







myList = [ 'even' if ( (x+y+z)%2 == 0 ) else 'odd' for x in [0,1] for y in [1,2] for z in [2,3] ]

# 'odd' 'even' 'even' 'odd' 'even' 'odd' 'odd' 'even'

print(myList)

l = [1, 2, 3, 4, 5]
y = ['one' if v == 1 else 'two' if v == 2 else 'other' for v in l]
print(y)

