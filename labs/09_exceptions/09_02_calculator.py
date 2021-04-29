'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
number1 = input('enter the number')
number2 = input('enter the number')


def division(number1, number2):
    a = number1 / number2
    return a


try:
    int_number1 = int(number1)
    int_number2 = int(number2)
    division(int_number1, int_number2)
except ZeroDivisionError:
    print('no division by zero')
except ValueError:
    print('Please enter an integer.')

