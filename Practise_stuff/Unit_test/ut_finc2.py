    
import unittest
from t_finc import *
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( add(1), 2)
    @unittest.skip("demonstrating skipping")
    def test_comb_string(self):
        self.assertEqual( comb_string('a'), 'ax')
    @unittest.expectedFailure
    def test_comb_string2(self):
        self.assertEqual( comb_string('a'), 'ax')

 
if __name__ == '__main__':
    unittest.main()