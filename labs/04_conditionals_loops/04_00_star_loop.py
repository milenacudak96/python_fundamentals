'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5

for i in range(n):
    for j in range(i):
        print('*',end='')
    print('*')

