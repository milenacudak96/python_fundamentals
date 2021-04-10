'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

number = int(input('enter the number between 0 and 1000000000: '))

while number in range(1, 1000000000):
    print(number)
    break
else:
    int(input('enter the other number: '))