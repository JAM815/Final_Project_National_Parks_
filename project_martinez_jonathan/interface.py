# Jonathan Martinez, Jam76378@usc.edu
# ITP 115, Spring 2022
# Section: Section: 31803 Mambas
# Final Project
# interface.py
# Description:
# Creates a menu that has 5 Different Options. From here, we create a function that ask for userInput. Using this input
# we created functions that will be used to define each of the five options

import tasks  # Need to use Tasks File for a couple of these functions


def getMenuDict():  # Dictionary Containing all Options that will be displayed in the Menu
    options_dict = {"A": "All National Parks", "B": "Parks in a Particular State", "C": "The Largest Park",
                    "D": "Search for Park", "Q": "Quit"}
    return options_dict


def displayMenu(menuDict):  # Displays Menu using Dictionary Keys and Values
    for key in menuDict:
        newValue = menuDict[key]
        print(key, "->", newValue)


def getUserchoice(menuDict):  # Displays the Menu and asks for User Input
    menuDict = menuDict
    key_list = list(menuDict)
    doWecontinue = True
    while doWecontinue == True:
        userInput = input("Choice: ")
        if userInput.strip().lower() == "a":  # Branching occurs here to determine what letter the User was trying to
            doWecontinue = False              # input
            uppercaseString = key_list[0]
        elif userInput.strip().lower() == "b":
            doWecontinue = False
            uppercaseString = key_list[1]
        elif userInput.strip().lower() == "c":
            doWecontinue = False
            uppercaseString = key_list[2]
        elif userInput.strip().lower() == "d":
            doWecontinue = False
            uppercaseString = key_list[3]
        elif userInput.strip().lower() == "q":
            doWecontinue = False
            uppercaseString = key_list[4]
        else:
            doWecontinue = True  # Continue While Loop until User chooses a correct option
    return uppercaseString  # Returns the Userinput as an Uppercase letter


def printAllParks(parksList):  # Prints out all Parks in parksList
    for item in range(len(parksList)):  # For all items inside parksList, conduct this for loop
        parkName = parksList[item]['Name']  # for each item in parksList look at nth dictionary and tell me the value
        parkCode = parksList[item]['Code']  # for ['key'] in each dictionary
        parkState = parksList[item]['State']
        parkAcres = parksList[item]['Acres']
        parkDate = parksList[item]['Date']
        dateConversion = tasks.convertDate(parkDate)  # Use Task to convert to a date that we want
        print(parkName + "  (" + parkCode + ") ")  # Print all information using the information that we found earlier
        print("  Location: " + parkState)
        print("  Area: " + parkAcres + " acres")
        print("  Date Established: " + dateConversion)
        print()


def getStateAbbr():  # Asks for the Abbreviation of the State
    correctState = True
    while correctState == True:
        moreUserinput = input("Enter a state: ")
        if len(moreUserinput.strip()) > 2:
            print("Need the two letter abbreviation")
            correctState = True
        else:
            correctState = False
            upperCaseinput = moreUserinput.strip().upper()
    return upperCaseinput  # Returns User Input as an Uppercase Value without Spaces


def printParksinState(parksList):
    possibleState = getStateAbbr()  # Using the getStateAbbr Function
    numberParks = 0  # Condition that allows us to determine if we need the outer if statement
    for item in range(len(parksList)):
        parkName = parksList[item]['Name']
        parkCode = parksList[item]['Code']
        parkState = parksList[item]['State']
        parkAcres = parksList[item]['Acres']
        parkDate = parksList[item]['Date']
        dateConversion = tasks.convertDate(parkDate)
        if parkState == possibleState:  # Print the information ONLY if the variable "parkState" = userinput from
            numberParks = numberParks + 1  # getStateAbbr()
            print(parkName + "  (" + parkCode + ") ")
            print("  Location: " + parkState)
            print("  Area: " + parkAcres + " acres")
            print("  Date Established: " + dateConversion)
            print()
    if numberParks == 0:  # Print if no valid states were found with those two Letters
        print("There are no national park in " + possibleState + " or it is not a valid state")


def printLargestPark(parksList):  # Loop through all the Items in the parksList and search for the "code" for the park
    largestParkCode = tasks.getLargestPark(parksList)  # found in task.getLargestPark
    for item in range(len(parksList)):
        parkName = parksList[item]['Name']
        parkCode = parksList[item]['Code']
        parkState = parksList[item]['State']
        parkAcres = parksList[item]['Acres']
        parkDate = parksList[item]['Date']
        dateConversion = tasks.convertDate(parkDate)
        parkDescription = parksList[item]['Description']
        if parkCode == largestParkCode:  # Print out the Park Name, Code, State, Acres, etc. for the Park that matched
            print(parkName + "  (" + parkCode + ") ")  # the 'Code' obtained from task.getLargestPark
            print("  Location: " + parkState)
            print("  Area: " + parkAcres + " acres")
            print("  Date Established: " + dateConversion)
            print("  Description: " + parkDescription)
            print()


def printParksForSearch(parksList):  # Search Feature using User Input
    lastUserinput = input("Enter text for searching: ")  # Ask for User Input
    searchInput = lastUserinput.strip().lower()
    doesParkexist = 0  # Used to determine if we need the outer If statement or not
    for item in range(len(parksList)):
        parkName = parksList[item]['Name']
        parkCode = parksList[item]['Code']
        parkState = parksList[item]['State']
        parkAcres = parksList[item]['Acres']
        parkDate = parksList[item]['Date']
        dateConversion = tasks.convertDate(parkDate)
        parkDescription = parksList[item]['Description']
        if searchInput in parkName.lower():  # If the searchInput is in parkName, print out the Park and all it's info
            doesParkexist = doesParkexist + 1
            print(parkName + "  (" + parkCode + ") ")
            print("  Location: " + parkState)
            print("  Area: " + parkAcres + " acres")
            print("  Date Established: " + dateConversion)
            print("  Description: " + parkDescription)
            print()
        elif searchInput in parkCode.lower():  # if the searchInput was not in parkName, but in parkCode, print out the
            doesParkexist = doesParkexist + 1  # park info
            print(parkName + "  (" + parkCode + ") ")
            print("  Location: " + parkState)
            print("  Area: " + parkAcres + " acres")
            print("  Date Established: " + dateConversion)
            print("  Description: " + parkDescription)
            print()
        elif searchInput in parkDescription.lower():  # If the searchInput was not in the previous two, but in the
            doesParkexist = doesParkexist + 1         # description, print out the park info out
            print(parkName + "  (" + parkCode + ") ")
            print("  Location: " + parkState)
            print("  Area: " + parkAcres + " acres")
            print("  Date Established: " + dateConversion)
            print("  Description: " + parkDescription)
            print()
    if doesParkexist == 0:  # Print this out if there are no parks that match the searchInput
        print("There are no national parks for the search term of " + "\'" + lastUserinput + "\'")

# Test Input for Sanity Checks
# displayMenu(getMenuDict())
# getUserchoice(getMenuDict())
# getStateAbbr()
# = tasks.readParksfile()
# parksList = y
# printAllParks(y)
# printParksinState(parksList)
# print(tasks.getLargestPark(y))
# printLargestPark(parksList)
# printParksForSearch(parksList)
