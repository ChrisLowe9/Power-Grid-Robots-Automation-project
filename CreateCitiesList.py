# This file is going to have a function to use prompts to create a dictionary with the
# details of the cities.

# Cities need:
# A name (which will be the key in the dictionary)
# A size (the number of spaces available)
# A cost value for each space

# I will also need to allocate cities to different regions
# I think I will create another dictionary of regions, and then assign the cities to those regions.

# For some of the choices, I have left it open for users to type in whatever they like, with that
# going to a default 'else' option - I wonder if that presents a security risk if a user were to
# input a magic cheat code that told my programme to do something else? This is something to find out about.

def addNonstandardCity(cities, cityName):
    # This is a separate function that asks what the value of each of the spaces in a city is.
    values = []
    spaceNo = 1
    citySize = None

    # First we find out how many spaces the city has.
    while citySize is None:
        citySizeInput = input(f"How many spaces does {cityName} have? Type 1, 2, 3, etc. ")
        try:
            citySize = int(citySizeInput)
        except:
            print("Invalid input. Please enter a valid integer, such as 1, 2 or 3.")

    spaces = citySize
    cities[cityName] = [citySize]

    # Then we find out the value of the spaces
    while spaces > 0:
        spaceValue = None
        while spaceValue is None:
            spaceValueInput = input(f"What value is {spaceNo}? Normally it will be 10, 15 or 20. ")
            try:
                spaceValue = int(spaceValueInput)
            except:
                print("Invalid input. Please enter a valid integer, such as 10, 15 or 20.")
        values.append(spaceValue)
        spaces -= 1
        spaceNo += 1

    cities[cityName].append(values)

    return cities

# This empty directory may not be needed when these functions are accessed from other files.
# Should I comment it out when I start doing that? Or can I just leave it in here, I wonder.
cities = {}

def createCitiesList(cities):
    # A pre-existing cities dictionary will be passed in, to enable this function to add
    # to a pre-existing list, rather than having to start from scratch each time.

    # print(len(cities)) # To check how many cities I have in 'cities' already

    addCity = True

    while addCity:

        cityName = input("What is the name of the city? ")

        print(f"Is {cityName} a standard 10, 15, 20 city?")

        standardCity = input("Type 1 for yes, or anything else for no. ")

        if standardCity == "1":
            # If we said it is a standard city, then that is what we add to the dictionary.
            citySize = 3
            values = [10, 15, 20]
            cities[cityName] = [citySize, values]
        else:
            # If we said it isn't standard, then we need more information.
            # I've defaulted to this function as even standard cities can be
            # inputted if we go down this route. The choice is just to let the user
            # save time if they want.
            addNonstandardCity(cities, cityName)

        print("Do you want to stop adding cities?")
        userChoice = input("Typing 1 will stop this, while anything else will continue. ")
        if userChoice == "1":
            addCity = False
            print("We will stop now.")
        else:
            print("We will continue.")

    return cities

createCitiesList(cities)

print(cities)

