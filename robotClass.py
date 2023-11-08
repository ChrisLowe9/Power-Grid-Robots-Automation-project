# Let's create the basic Robot class here.

# It will need to have money, a set of power plants, some resources, and cities that it owns.
# It will also need some functions for its actions in various phases
# These functions will be modified later on according to the different options that the robot
# expansion has - so I will need to create some child classes, perhaps.

class Robot:

    def __init__(self, money, name=None, powerPlants=[], resources={'coal': 0, 'oil': 0, 'garbage': 0, 'uranium': 0}, cities=None):
        self.money = money
        self.name = name
        self.powerPlants = powerPlants
        self.resources = resources
        self.cities = cities

    def __str__(self):
        return f"{self.name} has: Money = {self.money} and these powerplants: {self.powerPlants}"

    @classmethod
    def setRobotName(cls, self):
        name = input("What should we call this robot?")
        self.name = name

    @classmethod
    def deductRobotMoney(cls, self, amount):
        self.money = self.money - amount

    @classmethod
    def addRobotMoney(cls, self, amount):
        self.money = self.money + amount


    @classmethod
    def addPowerplant(cls, self, powerPlant):
        self.powerPlants.append(powerPlant)
        if len(self.powerPlants) > 3:
            minPowerPlant = min(self.powerPlants)
            self.powerPlants.remove(minPowerPlant)

    @classmethod
    def addResources(cls, self, shoppingBasket):
        resources = ['coal', 'oil', 'garbage', 'uranium']
        for resource in resources:
            self.resources[resource] += shoppingBasket[resource]

    @classmethod
    def removeResources(cls, self, burntResources):
        resources = ['coal', 'oil', 'garbage', 'uranium']
        for resource in resources:
            self.resources[resource] -= burntResources[resource]