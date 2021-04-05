'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
string = input('Please provide me with your sentence: ')
letter = input('Please provide me with your letter: ')
finder = string.find(letter)
print('your letter index is: ' + str(finder))
