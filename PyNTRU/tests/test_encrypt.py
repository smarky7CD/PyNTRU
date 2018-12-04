import sys
sys.path.append("..")

from parameters import Standard
from poly import Polynomial
from ntru_poly_ops import invert_in_p, invert_in_2tor

import unittest

class TestSimpleEncrypt(unittest.TestCase):

    def test_full_run(self):
        x = Standard()

        f = x.gen_fPoly()
        g = x.gen_gPoly()

        fp = invert_in_p(f, x.get_N())
        fq = invert_in_2tor(f, x.get_N(), 8)

        h = fq*g

        m = Polynomial([-1,0,1,1,1,-1,0,0,0,0,-1,1,1,0,1,1,0,-1,1], x.get_N())

        r = x.gen_rPoly()
        e = (r.scale(x.get_p())*h + m) % x.get_q()

        a = (f*e) % x.get_q()
        b = (fp*a) % x.get_p()
        
        self.assertEqual(b,m)


if __name__ == '__main__':
    print("Testing simple encryption and decryption")
    unittest.main()
