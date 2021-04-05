'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
r = 3.14
h = 5
pi = 3.141592653589793
volume = pi * r ** 2 * h
print('volume is: '+ str(volume))
surface = (2 * pi * r * h) + 2*pi*r**2
print('surface is: '+ str(surface))
