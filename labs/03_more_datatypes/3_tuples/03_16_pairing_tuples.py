'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

numbers = list(input('enter the number: '))
tuple_ = ()


def fun(numbers):
    for i in numbers:
        if numbers == 2:
            tuple_.append(numbers)
    else:
        numbers.append(numbers)
    numbers.append(tuple_)
    return tuple_


fun = fun(numbers)
print(fun)
