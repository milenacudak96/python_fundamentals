'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

string = input('enter teh string: ')
lst_tuple = [x for x  in zip(*[iter(string)])]
print(lst_tuple)
