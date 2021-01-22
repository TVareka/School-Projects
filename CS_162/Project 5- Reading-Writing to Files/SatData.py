# Author: Ty Vareka
# Date: 4/27/2020
# Description: Class named SatData writes the data to a text file in csv.  The class has a method that takes a list of
# DBNs and saves a csv file, but with only the rows corresponding to the DBNs in the list.

import json

class SatData:
    '''Class that writes the data to a text file in csv.  It has a method that takes a list of DBNs and saves a
    csv file, but only with the rows corresponding to the DBNs in the list'''

    def __init__(self):
        '''Initializes the class'''
        with open('sat.json', 'r') as satInfo:
            self._information = json.load(satInfo)

    def save_as_csv(self, DBNlist):
        '''This function takes a list of DBNs and creates a CSV file save with the rows corresponding to the DBNs
        in the list'''
        d = dict()
        DBNlist.sort()
        with open("output.csv", 'w') as startFile:
            startFile.write('DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,' +
                            'Writing Mean\n')
        for i in self._information["data"]:
            if i[8] in DBNlist:
                d[i[8]] = [i[9], i[10], i[11], i[12], i[13]]
                with open("output.csv", 'a') as outfile:
                    outfile.write(i[8] + ',' + i[9] + ',' + i[10] + ',' +  i[11] + ',' + i[12] + ',' + i[13] + '\n')






def main():
    '''testing the program with simple parameters'''
    nl = SatData()
    dbns = ["02M303", "02M294", "01M450", "02M418"]
    nl.save_as_csv(dbns)

if __name__ == "__main__":
    main()
