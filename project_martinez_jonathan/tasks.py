# Jonathan Martinez, Jam76378@usc.edu
# ITP 115, Spring 2022
# Section: Section: 31803 Mambas
# Final Project
# task.py
# Description:
# Create Three Functions which do the three following tasks: 1) Read in a CSV and Create a List that contains dictionaries
# that correspond to each National Park 2) Convert a date written in "YYYY-MM-DD" to "Month Name DD, YYYY" and 3) Find
# the largest park in the list created in the first task

def readParksfile():  # Opens the CSV File "national_parks.csv" and generates a List of Dictionaries where each Dictionary is a National Park
    parkList = []  # Create Empty List
    fin = open("national_parks.csv", "r")  # Open CSV File
    header_line = fin.readline().strip()
    header_list = header_line.split(",")  # Split Header into a List of Strings
    # print(header_list)  # Sanity Check
    for line in fin:
        parkDict = {}
        line = line.strip()
        info_list = line.split(",")  # Converts Line to List
        # print(info_list)  # Sanity Check
        for item in range(len(header_list)):
            key = header_list[item]
            value = info_list[item]
            parkDict[key] = value
        parkList.append(parkDict)

    fin.close()
    # print(parkList[0])  # Sanity Check
    # print(len(parkList))  # Sanity Check

    return parkList  # Return List with Dictionaries

def convertDate(dataStr):  # Converts a date written in "YYYY-MM-DD" to "Month Name DD, YYYY"
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    dataStr = dataStr.split("-")
    if dataStr[1] == "01":
        thisMonth = month_names[0]
    elif dataStr[1] == "02":
        thisMonth = month_names[1]
    elif dataStr[1] == "03":
        thisMonth = month_names[2]
    elif dataStr[1] == "04":
        thisMonth = month_names[3]
    elif dataStr[1] == "05":
        thisMonth = month_names[4]
    elif dataStr[1] == "06":
        thisMonth = month_names[5]
    elif dataStr[1] == "07":
        thisMonth = month_names[6]
    elif dataStr[1] == "08":
        thisMonth = month_names[7]
    elif dataStr[1] == "09":
        thisMonth = month_names[8]
    elif dataStr[1] == "10":
        thisMonth = month_names[9]
    elif dataStr[1] == "11":
        thisMonth = month_names[10]
    elif dataStr[1] == "12":
        thisMonth = month_names[11]
    updatedDate = thisMonth + " " + dataStr[2] + ", " + dataStr[0]
    return updatedDate  # Returns a Variable which contains a Date written in "Month DD, YYYY"

def getLargestPark(parksList): # Print the Largest Park by looping through all the dictionaries inside of the List
    maxValue = 0
    biggestPark = " "
    for item in range(len(parksList)):
        newVar = parksList[item]['Acres']
        # print(newVar)  # Sanity Check
        if int(newVar) > int(maxValue):
            maxValue = newVar
            biggestPark = parksList[item]['Code']
        else:
            maxValue = maxValue
    # print(maxValue)  # Sanity Checks
    # print(biggestPark)  # Sanity Checks
    return biggestPark  # Returns the 'Code' for the Largest Park

# readParksfile()
# convertDate()
# parksList = readParksfile()
# getLargestPark(parksList)
