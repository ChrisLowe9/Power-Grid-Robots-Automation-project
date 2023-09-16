# This file is going to allow me to create regions and then assign cities to
# those regions. At the moment I think I will trust myself to type in the names
# accurately - but when this is implemented on a website, it may be better to
# use a drop-down menu that is populated by names pulled from the 'cities' directory.

regions = {}

def createRegionLists(regions):

    print("Let's add regions to our list")
    noOfRegions = int(input("How many regions do you want to create? (Use numerals only) "))

    while noOfRegions > 0:
        regionColour = input("What colour is the region you want to add? ")
        noOfCities = input("How many cities does the region have? (Use numerals only, or I will cry) ")
        regions[regionColour] = [int(noOfCities)]
        noOfRegions -= 1

    print("Let's add cities to our regions")

    for key, value in regions.items():
        counter = value[0]
        cityList = []
        while counter > 0:
            cityName = input(f"What city do you want to add to {key} region? ")
            cityList.append(cityName)
            counter -= 1
        regions[key].append(cityList)

createRegionLists(regions)

print(regions)
