# Let's create the basic Robot class here.

# It will need to have money, a set of power plants, some resources, and cities that it owns.
# It will also need some functions for its actions in various phases
# These functions will be modified later on according to the different options that the robot
# expansion has - so I will need to create some child classes, perhaps.

class Robot:

    def __init__(self, money, name=None, powerPlants=None, resources=None, cities=None):
        self.money = money
        self.name = name
        self.powerPlants = powerPlants
        self.resources = resources
        self.cities = cities

    def __str__(self):
        return f"{self.name} has: Money = {self.money}"

    @classmethod
    def setRobotName(cls, self):
        name = input("What should we call this robot?")
        self.name = name
