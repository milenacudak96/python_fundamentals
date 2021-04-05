'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

string1 = input('Provide me with your 1st sentence: ')
string2 = input('Provide me with your 2nd sentence: ')
string3 = input('Provide me with your 3rd sentence: ')

print(len(string1), string1)
print(len(string2), string2)
print(len(string3), string3)


# CHALLENGE

if (len(string1) >= len(string2)) and (len(string1) >= len(string3)):
   largest = string1
elif (len(string2) >= len(string1)) and (len(string2) >= len(string3)):
   largest = string2
else:
   largest = string3

print("The largest numbers has", largest)