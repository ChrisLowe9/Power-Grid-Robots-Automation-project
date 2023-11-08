from databaseConnection import create_db_connection, read_query

class PowerPlant:
    def __init__(self, cost, type, resource=None, resource2=None, powerCost=None, citiesPowered=None):
        self.cost = cost
        self.type = type
        self.resource = resource
        self.resource2 = resource2
        self.powerCost = powerCost
        self.citiesPowered = citiesPowered

    def __str__(self):
        return f"Cost: {self.cost}, Type: {self.type}, Resource: {self.resource}, Resource2: {self.resource2}, PowerCost: {self.powerCost}, CitiesPowered: {self.citiesPowered}"

    @classmethod
    def fetchPowerPlantsFromDatabase(cls, user_name, user_password):
        # I might not ever need this method to fetch the data for the whole deck of power plants unless we
        # reach a point where we have a robot that is capable of predicting what power plants might come out and
        # trying to use that prediction to judge if it should buy a power plant or not. That is a long way off in
        # the future!
        power_plants = []

        # Connect to the SQL database
        connection = create_db_connection("localhost", user_name, user_password, "robots")

        # execute an SQL query to fetch power plant data, and extract the data from the query
        rows = read_query(connection, "SELECT cost, type, resource, resource2, powerCost, citiesPowered FROM powerplants")


        # Create PowerPlant instances from the fetched data
        for row in rows:
            powerPlant = cls(*row)
            power_plants.append(powerPlant)

        # Close the database connection
        connection.close()

        return power_plants

    # @classmethod
    # def identifyResourcesNeeded(cls, PowerPlantCost):



    @classmethod
    def updateRobotPowerPlants(cls, user_name, user_password, PowerPlantCost):

        # This method needs a list of costs for the power plants that the robot owns, so that it can then get those
        # details from the entries in the power plant deck database. In the read-query, it joins the
        # integers into a string that MySQL will recognise.
        power_plants = []

        # Connect to the SQL database
        connection = create_db_connection("localhost", user_name, user_password, "robots")

        # execute an SQL query to fetch power plant data, and extract the data from the query
        rows = read_query(connection,
                          f"SELECT cost, type, resource, resource2, powerCost, citiesPowered FROM powerplants WHERE cost IN ({', '.join(map(str, PowerPlantCost))})")

        # Create PowerPlant instances from the fetched data
        for row in rows:
            powerPlant = cls(*row)
            power_plants.append(powerPlant)

        # Close the database connection
        connection.close()

        return power_plants


def createMarket(step):
    # This function just creates a list of integers that we can then use in the updatePowerPlantMarket method
    # in the class. I am doing it separately because the human player will have the physical cards in front of
    # them and draw the new cards from the deck, and I just want to ask them to tell the robot what the cost of
    # each power plant in the market is. Then the robot can fetch the appropriate information from the database
    # of power plant cards.
    ppMarket = []

    # If it is step 3, then we should only have 6 power plants in the market. Otherwise there should be 8.
    if (step == 3):
        marketSize = 6
    else:
        marketSize = 8
    print(f"Market size is {marketSize}, because it is step {step}.")

    while marketSize > 0:
        ppMarket.append(int(input("What is the cost of the next power plant in the market?")))
        marketSize = marketSize-1

    # Let's get the power plants in order if the player entered them out of order.
    ppMarket.sort()
    return ppMarket