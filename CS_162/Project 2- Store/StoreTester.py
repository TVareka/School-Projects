# Author: Ty Vareka
# Date: 4/6/2020
# Description: This program is testing our store.py program to make sure that it is doing what we intend it to.  This
# program includes 5 tests in total using 3 different assert functions.

import Store
import unittest

class TestStore(unittest.TestCase):
    """Tests our store for functionality"""
    def test_1(self):
        """This test is checking to make sure the checkout price is equal to 33.45 (since they are a premium member"""
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Store.Customer("Yinsheng", "QWF", True)
        myStore = Store.Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        self.assertEqual(result, 33.45)

    def test_2(self):
        """This test is checking to make sure the program is charging the extra 7% shipping cost for non-premium
        members"""
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Store.Customer("Yinsheng", "QWF", False)
        myStore = Store.Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        self.assertEqual(result, (33.45 * 1.07))

    def test_3(self):
        """This test is checking to make sure the product search is working and returning a list with the product id
        '889' in it"""
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Store.Product("888", "Bird of unusual size", "when a bird of the usual size just won't do", 25.98, 10)
        p3 = Store.Product("887", "Cat of unusual size", "when a cat of the usual size just won't do", 50.55, 5)
        p4 = Store.Product("886", "A Dog", "woof woof", 60.75, 12)
        myStore = Store.Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)
        myStore.add_product(p4)
        result = myStore.product_search("size")
        self.assertIn('889', result)

    def test_4(self):
        """This test is checking ot make sure that the product search is working correctly and NOT returning
        the 4th product, since it does not have the word 'size' in it's name or description"""
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Store.Product("888", "Bird of unusual size", "when a bird of the usual size just won't do", 25.98, 10)
        p3 = Store.Product("887", "Cat of unusual size", "when a cat of the usual size just won't do", 50.55, 5)
        p4 = Store.Product("886", "A Dog", "woof woof", 60.75, 12)
        myStore = Store.Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)
        myStore.add_product(p4)
        result = myStore.product_search("size")
        self.assertNotIn('886', result)

    def test_5(self):
        """This test is making sure the 'None' is being returned when trying to get a product from an ID that
        doesn't exist"""
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Store.Product("888", "Bird of unusual size", "when a bird of the usual size just won't do", 25.98, 10)
        p3 = Store.Product("887", "Cat of unusual size", "when a cat of the usual size just won't do", 50.55, 5)
        p4 = Store.Product("886", "A Dog", "woof woof", 60.75, 12)
        myStore = Store.Store()
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)
        myStore.add_product(p4)
        result = myStore.get_product_from_id('900')
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
