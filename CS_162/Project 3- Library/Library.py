# Author: Ty Vareka
# Date: 4/13/2020
# Description: Creates a simplistic library that has multiple different classes.  Then allows members to check out
# or request the library items if they are available to do so.

class LibraryItem:
    """Creating a library item with a unique ID, location, and checkout information """

    def __init__(self, library_item_id, title):
        """Initializes the library item"""
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0

    def get_title(self):
        """Allows access to title outside of the class"""
        return self._title

    def get_location(self):
        """Allows access to the location outside of the class"""
        return self._location

    def get_date_checked_out(self):
        """Allows access to the date check out outside of the class"""
        return self._date_checked_out

    def set_date_checked_out(self, date):
        """Allows for the ability to change the date checked out outside of the class"""
        self._date_checked_out = date

    def set_location(self, loc):
        """Allows changing the location outside of the class"""
        self._location = loc

    def get_checked_out_by(self):
        """Allows access to who checked out the item outside of the class"""
        return self._checked_out_by

    def set_checked_out_by(self, person):
        """Allows changing who checked out the item outside of the class"""
        self._checked_out_by = person

    def get_requested_by(self):
        """Allows access to who requested the item outside of the class"""
        return self._requested_by

    def set_requested_by(self, person):
        """Allows for changing who requested the item outside of the class """
        self._requested_by = person

    def get_libraryItem_id(self):
        """Allows access to library item id outside of the class """
        return self._library_item_id

class Book(LibraryItem):
    """Item book that inherits from LibraryItem class"""

    def __init__(self, book_id, title, author):
        """Initializes the book class which inherits from the library item class"""
        super().__init__(book_id, title)
        self._author = author

    def get_check_out_length(self):
        """Allows access to check out length outside of the class"""
        return 21

    def get_author(self):
        """Allows access to the author outside of the class"""
        return self._author


class Album(LibraryItem):
    """Item album that inherits from LibraryItem class"""

    def __init__(self, album_id, title, artist):
        """Initializes the album class which inherits from the library item class"""
        super().__init__(album_id, title)
        self._artist = artist

    def get_check_out_length(self):
        """Allows access to check out length outside of the class"""
        return 14

    def get_artist(self):
        """Allows access to the artist outside of the class"""
        return self._artist

class Movie(LibraryItem):
    """Item 'movie' that inherits from LibraryItem class"""

    def __init__(self, movie_id, title, director):
        """Initializes the movie class which inherits from the library item class"""
        super().__init__(movie_id, title)
        self._director = director

    def get_check_out_length(self):
        """Allows access to check out length outside of the class"""
        return 7

    def get_director(self):
        """Allows access to the director outside of the class"""
        return self._director

class Patron:
    """Class for the patron with a unique ID and name. Keeps track of all patron information"""

    def __init__(self, patron_id, name):
        """Initializes the patron class"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        """Allows access to the fine amount outside of the class"""
        return self._fine_amount

    def add_library_item(self, id_number):
        """Adds library id to checked out items list"""
        self._checked_out_items.append(id_number)

    def remove_library_item(self, id_number):
        """Removes library item from the checked out items list"""
        self._checked_out_items.remove(id_number)

    def get_checked_out_items(self):
        """Allows access to the checked out items list from outside the class"""
        return self._checked_out_items

    def get_patron_id(self):
        """Allows access to the patron id from outside of the class"""
        return self._patron_id

    def amend_fine(self, amount):
        """Adds or subtracts an amount from the fine amount"""
        self._fine_amount += amount

class Library:
    """large class that keeps track of everything in the library including patrons"""

    def __init__(self):
        """Initializes library inventory/members and sets current date to 0"""
        self._current_date = 0
        self._holdings = dict()
        self._members = dict()

    def add_library_item(self, libraryItem):
        """takes LibraryItem object and adds it to the holdings"""
        self._holdings[libraryItem.get_libraryItem_id()] = libraryItem

    def add_patron(self, patron):
        """Adds patron object to members"""
        self._members[patron.get_patron_id()] = patron

    def get_library_item_from_id(self, libraryItem_id):
        """Allows this class to get the Library Items from ID"""
        try:
            self._holdings[libraryItem_id]
        except KeyError:
            return None
        else:
            return self._holdings[libraryItem_id]

    def get_patron_from_id(self, patron_id):
        """Allows this class to get the patron from their ID"""
        try:
            self._members[patron_id]
        except KeyError:
            return None
        else:
            return self._members[patron_id]

    def check_out_library_item(self, patron_id, libraryItem_id):
        """takes member id and library item id and checks out their items"""
        if patron_id in self._members and libraryItem_id in self._holdings:
            if self.get_library_item_from_id(libraryItem_id).get_location() == 'CHECKED_OUT':
                return 'item already checked out'
            elif self.get_library_item_from_id(libraryItem_id).get_location() == 'ON_HOLD_SHELF':
                if self.get_library_item_from_id(libraryItem_id).get_requested_by() == patron_id:
                    self.get_library_item_from_id(libraryItem_id).set_checked_out_by(patron_id)
                    self.get_library_item_from_id(libraryItem_id).set_date_checked_out(self._current_date)
                    self.get_library_item_from_id(libraryItem_id).set_location('CHECKED_OUT')
                    self.get_library_item_from_id(libraryItem_id).set_requested_by(None)
                    self.get_patron_from_id(patron_id).add_library_item(libraryItem_id)
                    return 'check out successful'
                else:
                    return 'item on hold by other patron'
            elif self.get_library_item_from_id(libraryItem_id).get_location() == 'ON_SHELF':
                self.get_library_item_from_id(libraryItem_id).set_checked_out_by(patron_id)
                self.get_library_item_from_id(libraryItem_id).set_date_checked_out(self._current_date)
                self.get_library_item_from_id(libraryItem_id).set_location('CHECKED_OUT')
                self.get_patron_from_id(patron_id).add_library_item(libraryItem_id)
                return 'check out successful'
        else:
            if patron_id in self._members:
                return 'item not found'
            else:
                return 'patron not found'

    def return_library_item(self, libraryItem_id):
        """takes library item id and if it was checked out, will place the book where it needs to go.  Also removes
        the library item from the patron's list of checked out items"""
        if libraryItem_id in self._holdings:
            if self.get_library_item_from_id(libraryItem_id).get_checked_out_by() == None:
                return 'item already in library'
            else:
                patron_id = self.get_library_item_from_id(libraryItem_id).get_checked_out_by()
                self.get_patron_from_id(patron_id).remove_library_item(libraryItem_id)
                self.get_library_item_from_id(libraryItem_id).set_checked_out_by(None)
                if self.get_library_item_from_id(libraryItem_id).get_requested_by() != None:
                    self.get_library_item_from_id(libraryItem_id).set_location('ON_HOLD_SHELF')
                else:
                    self.get_library_item_from_id(libraryItem_id).set_location('ON_SHELF')
                return 'return successful'
        else:
            return 'item not found'

    def request_library_item(self, patron_id, libraryItem_id):
        """checks to see if item is in library and then if the item is on hold.  If it is in the library and not on hold
        it will change its location to the on hold shelf"""
        if patron_id in self._members and libraryItem_id in self._holdings:
            if self.get_library_item_from_id(libraryItem_id).get_requested_by() != None:
                return 'item already on hold'
            else:
                self.get_library_item_from_id(libraryItem_id).set_requested_by(patron_id)
                if self.get_library_item_from_id(libraryItem_id).get_location() == 'ON_SHELF':
                    self.get_library_item_from_id(libraryItem_id).set_location('ON_HOLD_SHELF')
                return 'request successful'
        else:
            if patron_id in self._members:
                return 'item not found'
            else:
                return 'patron not found'

    def pay_fine(self, patron_id, payment):
        """Takes a patron id/payment amount and puts that amount toward the patron's fines"""
        if patron_id in self._members:
            self.get_patron_from_id(patron_id).amend_fine(-payment)
            return 'payment successful'
        else:
            return 'patron not found'

    def increment_current_date(self):
        """Increments the date by 1, then goes through the list of holdings.  If an item is checked out, it
        checks to see if the item is overdue and fines the patron if they have overdue items. """
        self._current_date += 1
        for key, item in self._holdings.items():
            if item.get_location() == 'CHECKED_OUT':
                days_out = self._current_date - item.get_date_checked_out()
                if (item.get_check_out_length() - days_out) < 0:
                    patron_id = item.get_checked_out_by()
                    self.get_patron_from_id(patron_id).amend_fine(0.10)


def main():
    """Tests the program based on basic parameters"""
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    print(lib.check_out_library_item("bcd", "456"))
    loc = a1.get_location()
    print(loc)
    lib.request_library_item("abc", "456")
    for i in range(57):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    print(p2_fine)
    lib.pay_fine("bcd", p2_fine)
    lib.return_library_item("456")

if __name__ == "__main__":
    main()
