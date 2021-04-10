'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

list=[]
for i in range(1,1001):
    list.append(i)
    if i % 2 != 0:
        print(i)