'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f' Planet {self.name} is {self.color}'


Mars = Planet('Mars', 'blue')
print(Mars.name)
