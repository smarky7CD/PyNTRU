import sys
sys.path.append("..")

from parameters import Standard
from poly import Polynomial
from ntru_poly_ops import invert_in_p, invert_in_2tor

import unittest

class TestNTRUPolyOps(unittest.TestCase):

    def test_fip(self):
        x = Standard()
        f = x.gen_fPoly()
        f_i = invert_in_p(f, x.get_N())
        self.assertTrue((f*f_i)%3 == Polynomial([1], x.get_N()))

    def test_fiq(self):
        x = Standard()
        f = x.gen_fPoly()
        f_i = invert_in_2tor(f, x.get_N(), 8)
        self.assertTrue((f*f_i)%256 == Polynomial([1], x.get_N()), 8)
        
if __name__ == '__main__':
    print("Testing NTRU polynomial operations...")
    unittest.main()
