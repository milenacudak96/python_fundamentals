'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

number = int(input('enter the number: '))


def fun(number):
    if number % 4 == 0 or number % 7 == 0:
        print('True')
    else:
        print('False')


fun(number)


def fun1(number1):
    if ((number1 % 4 == 0) and (number % 7 == 0)):
        print('True')
    else:
        print('False')


fun1(number)

variable = int(input('enter the number between 1 and 1,000,000,000: '))


def fun2(variable: int) -> variable:
    print(variable)


fun2(variable)
