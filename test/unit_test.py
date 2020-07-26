import unittest
from unittest.mock import Mock

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import main
import brute_force_method as bfm
import greedy_method as gm


"""
    Unit test class to check whether the implemented methods
    to find the shortest common string is working correct or not

    Comment line 61 in main.py before running unit tests
"""
class shortest_common_string_Testing(unittest.TestCase):

    def test_get_data(self):
        """ tests whether get_data method in main.py reads data from file 
            and return the contents in string array fromat.
            use unit_test_file.txt data for test purpose.
        """
        self.assertEqual(main.get_data("./test/unit_test_file.txt"), ['check', 'data', 'is', 'right'])

    def test_find_shortest_common_string(self):
        """ tests whether the method is navigating as per the user choice """
        self.assertEqual(
            main.find_shortest_common_string(['all is well', 'ell that en', 'hat end', 't ends well']), None)
    
    def test_write_file(self):
        self.assertEqual(main.write_to_file("check writing data to file", "Brute Force"), None)
    
    def test_brute_force_method(self):
        """ tests the brute force method """
        self.assertEqual(
            bfm.shortest_common_string(['all is well', 'ell that en', 'hat end', 't ends well']), 
            'all is well that ends well')

    def test_greedy_method(self):
        """ tests the greedy method """
        self.assertEqual(
            gm.greedy_shortest_common_string(['all is well', 'ell that en', 'hat end', 't ends well']), 
            'all is well that ends well')


if __name__ == '__main__':
    unittest.main()






