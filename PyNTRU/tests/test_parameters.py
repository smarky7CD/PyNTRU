import sys
sys.path.append("..")

from parameters import Standard

import unittest

class TestParameters(unittest.TestCase):

    def test_fPoly(self):
        s = Standard()
        fp = s.gen_fPoly()
        self.assertEqual(fp._coeff.count(1), 216)
        self.assertEqual(fp._coeff.count(-1), 215)

    def test_gPoly(self):
        s = Standard()
        fg = s.gen_gPoly()
        self.assertEqual(fg._coeff.count(1), 72)
        self.assertEqual(fg._coeff.count(-1), 72)

    def test_rPoly(self):
        s = Standard()
        fr = s.gen_rPoly()
        self.assertEqual(fr._coeff.count(1), 55)
        self.assertEqual(fr._coeff.count(-1), 55)

    def test_toString(self):
        s = Standard()
        p_string = str(s)
        self.assertEqual(p_string, "503,3,256,215,72,55")
        
if __name__ == '__main__':
    print("Testing polynomial generation from parameters...")
    unittest.main()
