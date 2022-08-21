# Jonathan Martinez, Jam76378@usc.edu
# ITP 115, Spring 2022
# Section: Section: 31803 Mambas
# Final Project
# main.py
# Description:
# Using both the Tasks and Interface Files, we create a Program that will loop until "Q" or "q" is given.
# This program will give the following: 1) Print all the National Parks, 2) Print the National Parks found in a State
# as given by user input 3) Print the Largest National Park, and it's description 4) Use user input to find matches and
# partial matches in all the National Parks 5) Quit the Program

import tasks  # Using the Tasks Python File
import interface  # Using the Interface Python File


def main():
    print("National Parks")
    parksList = tasks.readParksfile()  # Read the CSV File to be used in another Locations
    menuDict = interface.getMenuDict()  # Get the all values for the Menu that will be Displayed later
    doWeContinue = True  # Until this turns false, continue the loop
    while doWeContinue == True:
        interface.displayMenu(menuDict)
        userInput = interface.getUserchoice(menuDict)  # Display the Menu and ask for User Input
        if userInput == "A":
            interface.printAllParks(parksList)  # User Selects "A", print all Parks in parksList
            print()
            doWeContinue = True
        elif userInput == "B":
            interface.printParksinState(parksList)  # User Selects "B", asks input, display parks in State (if valid)
            print()
            doWeContinue = True
        elif userInput == "C":
            interface.printLargestPark(parksList)  # User Selects "C", prints the largest park in parksList
            doWeContinue = True
        elif userInput == "D":
            interface.printParksForSearch(parksList)  # User Selects "D", asks input, displays parks that match or
            print()
            doWeContinue = True  # partial match input
        elif userInput == "Q":  # User Selects "Q", While Loop terminates
            print()
            doWeContinue = False  # Turns this condition to false which terminates the While Loop
        else:  # User Selects invalid input and the While Loop will ask again for another option
            print()
            doWeContinue = True
    print("Thank you for using my Program!") # Print this at the very end once the While Ends


main()
