# Author: Ty Vareka
# Date: 4/6/2020
# Description: This is an online store simulator.  It has a product, customer and store class which all communicate with
# each other to simulate a store-like atmosphere.

class Product:
    """Creates object Product that represents a product with an ID, title, description, price and quantity"""

    def __init__(self, id, title, description, price, quantity_available):
        """Initializes the product"""
        self._id = id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """Allows access to ID from outside the class"""
        return self._id

    def get_title(self):
        """Allows access to title from outside the class"""
        return self._title

    def get_description(self):
        """Allows access to description from outside the class"""
        return self._description

    def get_price(self):
        """Allows access to price from outside the class"""
        return self._price

    def get_quantity_available(self):
        """Allows access to quantity available from outside the class"""
        return self._quantity_available

    def decrease_quantity(self):
        """Decreases the overall quantity by one"""
        self._quantity_available = (self._quantity_available - 1)


class Customer:
    """Creates a customer object that represents a customer with a name and account ID"""

    def __init__(self, name, account_id, p_member):
        """Initializes the customer and creates list for customers cart"""
        self._name = name
        self._account_id = account_id
        self._p_member = bool(p_member) # must be a boolean value, but how to test and make sure of that?
        self._customer_cart = []

    def get_name(self):
        """Allows access to customer name from outside the class"""
        return self._name

    def get_customer_id(self):
        """Allows access to customer ID from outside the class"""
        return self._account_id

    def is_premium_member(self):
        """returns whether the customer is a premium member (True or False)"""
        return self._p_member

    def add_product_to_cart(self, id_number):
        """Adds a product ID code to the list 'customer cart'"""
        self._customer_cart.append(id_number)

    def empty_cart(self):
        """Empties the list keeping track of the customer's cart """
        self._customer_cart = []

    def get_cart(self):
        """Allows access to customer cart from outside the class"""
        return self._customer_cart


class InvalidCheckoutError(Exception):
    """Invalid Checkout Error Exception class"""
    pass


class Store:
    """Creates the object 'Store' which has some number of products in its inventory and some number of customers
    as members"""

    def __init__(self):
        """Initializes the store's inventory"""
        self._inventory = dict()
        self._membership = dict()

    def add_product(self, product):
        """Adds product to the store's inventory"""
        self._inventory[product.get_product_id()] = product

    def add_member(self, member):
        """Adds another customer to the store's list of members"""
        self._membership[member.get_customer_id()] = member

    def get_product_from_id(self, product_id):
        """Allows this class to get the product from the product's ID number"""
        try:
            self._inventory[product_id]
        except KeyError:
            return None
        else:
            return self._inventory[product_id]

    def get_member_from_id(self, customer_id):
        """Allows this class to get the member from the member's ID number"""
        try:
            self._membership[customer_id]
        except KeyError:
            return None
        else:
            return self._membership[customer_id]

    def product_search(self, search_string):
        """Allows the class to search the list of products and return a list of products that include what was
        typed in the search_string"""
        l = list()
        search_string = search_string.lower()
        for key, p in self._inventory.items():
            if search_string in p.get_title().lower() or search_string in p.get_description().lower():
                l.append(key)
        l.sort()
        return l

    def add_product_to_member_cart(self, product_id, customer_id):
        """Takes a product id and customer's id, then adds that product to the members shopping cart"""
        if product_id in self._inventory and customer_id in self._membership:
            if self.get_product_from_id(product_id).get_quantity_available() > 0:
                self._membership[customer_id].add_product_to_cart(product_id)
                return "product added to cart"
            else:
                return "product out of stock"
        else:
            if product_id in self._inventory:
                return "member ID not found"
            else:
                return "product ID not found"

    def check_out_member(self, customer_id):
        """Checks out the member by taking everything in the shopping cart, totaling it up and returning the
        cost of everything in the cart.  Also checks to see if hte member is a premium member, if they are, no
        shipping cost, but if they are not a premium member, they will have an extra 7% shipping charge added"""
        total = 0
        if customer_id in self._membership:
            cart = self._membership[customer_id].get_cart()
            for i in cart:
                if self.get_product_from_id(i) == None:
                    break
                elif self.get_product_from_id(i).get_quantity_available() > 0:
                    total += self.get_product_from_id(i).get_price()
                    self.get_product_from_id(i).decrease_quantity()
                else:
                    break
            if not self._membership[customer_id].is_premium_member():
                total += (total * 0.07)
            self._membership[customer_id].empty_cart()
            return total
        else:
            raise InvalidCheckoutError

def main():
    """simple function to show how the program works.  Will only run if __name__ == __main__"""
    p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
    p2 = Product("888", "Bird of unusual size", "when a bird of the usual size just won't do", 25.98, 10)
    p3 = Product("887", "Cat of unusual size", "when a cat of the usual size just won't do", 50.55, 5)
    p4 = Product("886", "A Dog", "woof woof", 60.75, 12)
    c1 = Customer("Yinsheng", "QWF", True)
    myStore = Store()
    myStore.add_product(p1)
    myStore.add_product(p2)
    myStore.add_product(p3)
    myStore.add_product(p4)
    myStore.add_member(c1)
    myStore.add_product_to_member_cart("889", "QWF")
    try:
        result = myStore.check_out_member("QWF")
    except InvalidCheckoutError:
        print("An error has occurred due to an invalid customer.  Invalid checkout")
    else:
        print(result)

if __name__ == "__main__":
    main()
