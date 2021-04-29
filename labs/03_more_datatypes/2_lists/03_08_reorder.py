'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

'''
# creating an empty list
lst = []

# number of elemetns as input
i = int(input("Enter the number: "))

# iterating till the range
for i in range(0, 11):
    ele = int(input())

    lst.append(ele)  # adding the element

print(lst[3],lst[5],lst[7],lst[9])
print(lst[10],lst[8],lst[6],lst[4], lst[2])
