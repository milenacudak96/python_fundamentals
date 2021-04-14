'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

'''


class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p = Point(5, 10)

print(p.x + p.y)



