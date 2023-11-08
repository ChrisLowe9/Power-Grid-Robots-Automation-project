from databaseConnection import create_db_connection, read_query

class resourceMarket:
    def __init__(self, coal, oil, garbage, uranium):
        self.coal = coal
        self.oil = oil
        self.uranium = uranium
        self.garbage = garbage

    def __str__(self):
        return f"The current resource market is: Coal {self.coal}; Oil {self.oil}; Garbage {self.garbage}; Uranium {self.uranium}."


