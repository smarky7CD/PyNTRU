import sys
sys.path.append("..")

from poly import Polynomial as poly

import unittest

class TestPolynomials(unittest.TestCase):

    def test_init(self):
        a = poly([3,4,5,6,7], 5)
        b = poly([6,1,2,9,13,0,0,0,0,0,0,0,0,0,0,0,0,0], 18)
        self.assertEqual(str(a), "3 4 5 6 7")
        self.assertEqual(str(b), "6 1 2 9 13")
        
    def test_add(self):
        f = poly([3,0,2,0,-3,0,1], 7)
        g = poly([1,-3,1,0,0,2,-1], 7)
        fpg = f + g
        self.assertEqual(fpg._coeff, [4,-3,3,0,-3,2])

    def test_conv_product(self):
        f = poly([3,0,2,0,-3,0,1], 7)
        g = poly([1,-3,1,0,0,2,-1], 7)
        fmg = f * g
        self.assertEqual(fmg._coeff, [4, -10, -1, -3, 1, 14, -5])

    def test_mod_and_eq(self):
        a = poly([3,4,5,6,7], 5)
        b = poly([6,1,2,9,13,0,0,0], 8)
        self.assertFalse(a == b)
        self.assertTrue(a%3 == b%3)

    def test_len(self):
        a = poly([3,4,5,6,7], 5)
        g = poly([1,-3,1,0,0,2,-1], 7)
        self.assertEqual(len(a), 5)
        self.assertFalse(len(a) == len(g))
                    
if __name__ == '__main__':
    print("Testing polynomials...")
    unittest.main()
