'''
Write a script with a function that demonstrates the use of *args.

'''

def fun(*args):
    for i in args:
        print(i)

fun(1,2,3,4,5)