"""
A simple example of a unit test.
"""

import unittest
from backend import additional_backend as my_lib


class TestBackEnd(unittest.TestCase):
    """
    A class for some unit tests.
    """
    
    def test_string_multi(self):
        """
        A foo to test "string_multi" function from the backend.
        """
        
        # cases with self
        case1 = ['a',  3, 'a a a ']
        case2 = ['',   3, '   ']
        case3 = [' ',  3, '      ']
        case4 = ['12', 3, '12 12 12 ']
        case5 = ['- ', 3, '-  -  -  ']
        cases = [case1, case2, case3, case4, case5]
        
        for i in cases:
            res = my_lib.string_multi(i[0], i[1])
            self.assertEqual(res, i[2])
            
            
if __name__ == '__main__':
    unittest.main()
    
    