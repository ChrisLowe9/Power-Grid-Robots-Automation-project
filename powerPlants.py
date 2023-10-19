import mysql.connector
from mysql.connector import Error

from databaseConnection import create_db_connection, read_query

class PowerPlant:
    def __init__(self, cost, type, resource, resource2=None, powerCost=None, citiesPowered):
        self.cost = cost
        self.type = type
        self.resource = resource
        self.resource2 = resource2
        self.powerCost = powerCost
        self.citiesPowered = citiesPowered

    @classmethod
    def fetchPowerPlantsFromDatabase(cls, databasePath):
        power_plants = []

        # Connect to the SQL database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # execute an SQL query to fetch power plant data
        cursor.execute("SELECT cost, type, resource, resource2, powerCost, citiesPowered FROM powerPlants")

        # Fetch data from the query
        rows = cursor.fetchall()

        # Create PowerPlant instances from the fetched data
        for row in rows:
            powerPlant = cls(*row)
            power_plants.append(powerPlant)

        # Close the database connection
        connection.close()

        return power_plants

