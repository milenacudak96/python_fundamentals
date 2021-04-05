'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
name = str(input('Input your name: '))
first = name[0]
name2 = name[1:]
print( name2 + first + 'ay')