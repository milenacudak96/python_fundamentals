'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# 1)
a = 3
b = float(3)
# 2)
c = int(b)
# 3)
print(0.6 // 0.2)
# 4)
d = int(input('Tell the number: '))
h = int(input('Tell me the 2nd number: '))
print(d * h)
