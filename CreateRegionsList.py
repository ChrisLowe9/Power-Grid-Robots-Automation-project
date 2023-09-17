# This file is going to allow me to create regions and then assign cities to
# those regions. At the moment I think I will trust myself to type in the names
# accurately - but when this is implemented on a website, it may be better to
# use a drop-down menu that is populated by names pulled from the 'cities' directory.

import json

regions = {}

def createRegionLists(regions):

    print("Let's add regions to our list")
    noOfRegions = int(input("How many regions do you want to create? (Use numerals only) "))
    # In the final version, I will  want to put a limit on the number of regions that someone
    # put in a map, because otherwise someone could use automation to take up too many resources
    # of the website. We want to limit the size of the map (and the way Power Grid is designed,
    # there are not that many regions anyway.)

    while noOfRegions > 0:
        regionColour = input("What colour is the region you want to add? ")
        noOfCities = int(input("How many cities does the region have? (Use numerals only, or I will cry) "))
        regions[regionColour] = [noOfCities]
        noOfRegions -= 1

        print(f"Let's add cities to the {regionColour} region")

        counter = noOfCities
        cityList = []
        while counter > 0:
            cityName = input(f"What city do you want to add to {regionColour} region? ")
            cityList.append(cityName)
            counter -= 1
        regions[regionColour].append(cityList)


    return regions

def saveRegionList(regions):
    # This function is going to save the dictionary I create as a json file, so that I don't have to
    # keep on inputting the data.

    fileName = input("What name do you want to give your file? ")

    filePath = fileName + '.json'

    with open(filePath, 'w') as json_file:
        json.dump(regions, json_file)


def modifyRegionList():
    # This function is going to open a pre-created json file, and add regions to it.
    # I don't think that this function needs to reference an external object, because
    # it will have a prompt to specify the json file to open.
    # First, ask what file to open.
    # Then print the contents of the file, and ask if the user wants to continue.
    # Then access the 'createRegionLists' function to add regions
    # Then print the modified contents and ask if they are ok.
    # Then save the modified contents.

    file_path = input('What json file do you want to open? Please type the whole name. ')

    with open(file_path, 'r') as json_file:
        regions = json.load(json_file)

    print(f"This is the contents of the file you opened: {regions}")

    createRegionLists(regions)

    print('Here is the updated list of regions and cities')
    for region in regions:
        print(f"{region} : {regions[region]}")

    saveFileValue = input("Do you want to save this file? 1 for Yes - anything else and you will lose all your hardwork. ")

    if saveFileValue == '1':
        with open(file_path, 'w') as json_file:
            json.dump(regions, json_file)

# createRegionLists(regions)

# print(regions)

# saveRegionList(regions)

modifyRegionList()