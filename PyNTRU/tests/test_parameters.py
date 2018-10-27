import sys
sys.path.append("..")

from parameters import Highest

import unittest

class TestParameters(unittest.TestCase):

    def test_fPoly(self):
        s = Highest()
        fp = s.gen_fPoly()
        self.assertEqual(fp._coeff.count(1), 216)
        self.assertEqual(fp._coeff.count(-1), 215)

    def test_gPoly(self):
        s = Highest()
        fg = s.gen_gPoly()
        self.assertEqual(fg._coeff.count(1), 72)
        self.assertEqual(fg._coeff.count(-1), 72)

    def test_rPoly(self):
        s = Highest()
        fr = s.gen_rPoly()
        self.assertEqual(fr._coeff.count(1), 55)
        self.assertEqual(fr._coeff.count(-1), 55)
        
if __name__ == '__main__':
    unittest.main()
