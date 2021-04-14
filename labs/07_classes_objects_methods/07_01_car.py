'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car:
    """This is class called Car"""

    def __init__(self, model, year, max_speed=0):
        """ThiS an init method"""
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def accelerate(self):
        """This method should add 5 to the speed data attribute each time it is called."""
        self.max_speed = self.max_speed + 5

    def __str__(self):
        return f'Car {self.model} from {self.year} has max speed of {self.max_speed}'


Skoda = Car('Skoda', 2000, 150)
print(Skoda)
print(Skoda.model)
Skoda.accelerate()
print(Skoda)
