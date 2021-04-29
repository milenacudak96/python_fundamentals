'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 2.

'''

gen = (i for i in range (10) if i%2 == 0)
for i in gen:
    print(i)
