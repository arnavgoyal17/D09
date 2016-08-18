#!/usr/bin/env python3# Exercise: Presidents# Write a program to:# (1) Load the data from presidents.txt into a dictionary.# (2) Print the years the greatest and least number of presidents were alive.#     (between 1732 and 2016 (inclusive))#     Ex.#       'least = 2015'#       'John Doe'#       'most = 2015'#       'John Doe, Jane Doe, John Adams, and Jane Adams'# Bonus: Confirm there are no ties. If there is a tie print like so:#     Ex.#       'least = 1900, 2013-2015'#       'John Doe (1900)'#       'Jane Doe (2013-2015)'#       'most = 1900-1934, 2013'#       'John Doe, Jane Doe, John Adams, and Jane Adams (1900-1933)'#       'Sally Doe, Billy Doe, Mary Doe, and Cary Doe (1934)'#       'Alice Doe, Bob Doe, Zane Doe, and Yi Do (2013)'############################################################################### Importsimport datetime# BodymaxYear = 0minYear = 0presDict = {}def ReadFile():    listYears = []    minYear = 0    maxYear = 0    with open("presidents.txt", "r") as file:        for items in file:            inputLine = items.strip("\n").split(",")            if(inputLine[2] == "None"):                inputLine[2] = datetime.datetime.now().year            # prepare a list of birth and death year of presidents, if still alive then death = 2016            listYears.append([int(inputLine[1]), int(inputLine[2])])    maxYear = sorted(listYears, key=lambda x:x[1], reverse=True)[0][1]    minYear = sorted(listYears, key=lambda x:x[0])[0][0]    for year in range(minYear, maxYear + 1):        presDict.setdefault(year, [])def AddPresidents():    with open("presidents.txt", "r") as file:        for items in file:            inputLine = items.strip("\n").split(",")            if(inputLine[2] == "None"):                inputLine[2] = datetime.datetime.now().year            lowerYear = int(inputLine[1])            upperYear = int(inputLine[2])            for years in range(lowerYear, upperYear + 1):                presDict[years] = presDict.get(years, []) + [inputLine[0]]def GetLeastMax():    maxYearKey = sorted(sorted(presDict), key=lambda x:len(presDict.get(x)), reverse=True)[0]    maxPresList = presDict.get(maxYearKey)    print("most: " + str(maxYearKey))    print(", ".join(sorted(maxPresList)))    minYearKey = sorted(sorted(presDict), key=lambda x:len(presDict.get(x)))[0]    minPresList = presDict.get(minYearKey)    print("\nleast: " + str(minYearKey))    print(", ".join(sorted(minPresList)))##############################################################################def main():  # CALL YOUR FUNCTION BELOW    ReadFile()    AddPresidents()    GetLeastMax()if __name__ == '__main__':    main()