'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = str(input('tell me the sentence: '))

list = sentence.split()

print (max(list, key=len))


