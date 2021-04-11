'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list):
  max_=max(list)
  min_=min(list)
  average_= sum(list)/len(list)
  print('max: ' + str(max_), 'min: ' + str(min_), 'average: ' + str(average_))
  # define the function here
  pass

# call the function below here
stats(example_list)