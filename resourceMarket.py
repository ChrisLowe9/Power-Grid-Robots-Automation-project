from databaseConnection import create_db_connection, read_query

class resourceMarket:
    def __init__(self, coal, oil, garbage, uranium):
        self.coal = coal
        self.oil = oil
        self.uranium = uranium
        self.garbage = garbage

    def __str__(self):
        return f"The current resource market is: Coal {self.coal}; Oil {self.oil}; Garbage {self.garbage}; Uranium {self.uranium}."

    @classmethod
    def deductResource(cls, self, amount, keyWord):
        if keyWord == 'coal':
            self.coal = self.coal - amount
        elif keyWord == 'oil':
            self.oil = self.oil - amount
        elif keyWord == 'uranium':
            self.uranium = self.uranium - amount
        elif keyWord == 'garbage':
            self.garbage = self.garbage - amount
    @classmethod
    def addResource(cls, self, amount, keyWord):
        if keyWord == 'coal':
            self.coal = self.coal + amount
        elif keyWord == 'oil':
            self.oil = self.oil + amount
        elif keyWord == 'uranium':
            self.uranium = self.uranium + amount
        elif keyWord == 'garbage':
            self.garbage = self.garbage + amount