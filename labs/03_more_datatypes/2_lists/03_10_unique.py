'''
Write a script that creates a list of all unique values in a list. For example:


'''
list1 = [1, 2, 6, 55, 2, 4, 6, 1, 13]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)



