# Author: Ty Vareka
# Date: 4/27/2020
# Description: Write a class for Nobel Prize data that allows the user to search the class using the year and
# category which returns those Nobel Prize winner(s)

import json

class NobelData:
    '''This class opens a json file and has a method that takes the year/category which returns winner's surname'''

    def __init__(self):
        '''initializes the class'''
        with open('nobels.json', 'r') as NobelInfo:
            self._information = json.load(NobelInfo)

    def search_nobel(self, year, category):
        '''Allows user to search the uploaded json file with year/category to get surnames of those nobel prize
        winners'''
        finalList = []
        lst = self._information["prizes"]
        for i in lst:
            if i["year"] == year and i["category"] == category:
                for winner in i["laureates"]:
                    surname = winner["surname"]
                    finalList.append(surname)
        finalList.sort()
        return finalList



def main():
    '''testing the program with simple parameters'''
    nd = NobelData()
    rslt = nd.search_nobel("2001", "economics")
    print(rslt)

if __name__ == "__main__":
    main()