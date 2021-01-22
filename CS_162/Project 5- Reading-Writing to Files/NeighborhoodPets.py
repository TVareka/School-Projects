# Author: Ty Vareka
# Date: 4/27/2020
# Description: Creates a class called NeighborhoodPets that can save pets that are added to it, to a json file.
# This class can also delete pets, search for owners, load data from a json file, and get a list of all pet species

import json

class NeighborhoodPets:
    '''Class that has a method for adding a pet, deleting a pet, searching for the owner of a pet, saving data to a
    JSON file, loading data from a json file and getting a list of all pet species'''

    def __init__(self):
        '''Initializes the class'''
        self._petDict = {}

    def add_pet(self, name, species, petOwner):
        '''Adds pet, species and pet owner to the json file'''
        if name not in self._petDict:
            self._petDict[name] = [species, petOwner]

    def delete_pet(self, name):
        '''Deletes a pet from json file via a name (pet's names must be unique)'''
        if name in self._petDict:
            del self._petDict[name]

    def get_owner(self, name):
        '''Allows access to the owner from a pet name'''
        if name in self._petDict:
            return self._petDict[name][1]

    def save_as_json(self, jsonFile):
        '''Saves the info as a json file'''
        with open(jsonFile, 'w') as outfile:
            json.dump(self._petDict, outfile)

    def read_json(self, jsonFile):
        '''read the json file'''
        with open(jsonFile, 'r') as infile:
            self._petDict = json.load(infile)

    def get_all_species(self):
        '''allows access to all species in the dictionary'''
        s = set()
        for name in self._petDict:
            s.add(self._petDict[name][0])
        return s


def main():
    '''testing the program with simple parameters'''
    np = NeighborhoodPets()
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
    np.save_as_json("D:\\Test\\5d.txt")
    np.delete_pet("Tiny")
    np.save_as_json("D:\\Test\\notiny.txt")
    spot_owner = np.get_owner("Spot")
    print(spot_owner)
    species_set = np.get_all_species()
    print(species_set)
    np.read_json("D:\\Test\\5d.txt")
    species_set = np.get_all_species()
    print(species_set)

if __name__ == "__main__":
    main()



