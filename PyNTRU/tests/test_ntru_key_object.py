import sys
sys.path.append("..")

from ntru_key import NTRUKey, generate_key
from poly import Polynomial as poly

import unittest

class TestNTRUKeyObject(unittest.TestCase):

    def test_creation_and_operations(self):

        key = generate_key()

        m = poly([1,1,0,0,-1,-1,-1,1,1,0,1,-1,1,0,-1,-1,1,0,0,1,0,1,-1,1], 29)

        c = key.encrypt(m)
        d = key.decrypt(c)

        self.assertEqual(m,d)
        self.assertTrue(key.is_private())
        
if __name__ == '__main__':
    print("Testing NTRU Key Object Operations")
    unittest.main()
