    
import unittest
from t_finc import *
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( add(1), 2)
 
    def test_comb_string(self):
        self.assertEqual( comb_string('a'), 'ay')
 
if __name__ == '__main__':
    unittest.main()