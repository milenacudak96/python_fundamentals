'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

cartesian_product = [(a, b) for a in sizes for b in colors]
print(cartesian_product)