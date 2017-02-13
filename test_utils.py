# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016
#

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertEqual(utils.fact(0),1)
        try:
            utils.fact(-5)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True) 
        self.assertIsNone()
    
    def test_roots(self):
        slef.assertEqual(utils.roots(5,2,3),-1)
        self.assertEqual(utils.roots(2,20,2),(2,5))

    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
