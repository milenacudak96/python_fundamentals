'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
def converter(int):
    km = int * 1.6
    return km

time = 0.5083
result = converter(10)/time
print('th result is: '+ str(result))