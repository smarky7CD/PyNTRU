from math import log2 as lg
import base58

from parameters import Parameters, Standard
from poly import Polynomial as poly
from ntru_poly_ops import invert_in_p, invert_in_2tor


PUBLIC_HEAD_BLOCK = "<~~~~~~~~~~PyNTRU Public Key (Alpha Version)~~~~~~~~~~"
PRIVATE_HEAD_BLOCK = "<~~~~~~~~~~PyNTRU Private Key (Alpha Version)~~~~~~~~~~"
END_BLOCK = "~~~~~~~~~~END~~~~~~~~~~>"


class NTRUKey():

    def __init__(self, P, h , f=None, g=None, fp=None, fq=None):
        """Key parameters"""
        self._P = P # parameter set
        self._h = h # public key
        self._f = f # private key f
        self._g = g # private key g
        self._fp = fp # used for decryption
        self._fq = fq # ensure correctness

    def encrypt(self,m):
        """m is a the message encoded as a polynomial"""
        if m._N <= self._P.get_N():

            r = self._P.gen_rPoly()
            e = (r.scale(self._P.get_p())*self._h+m) % self._P.get_q()

            return e # Polynomial representing the encryption message
        else:
            raise Exception("m is too large, must be equal or under size %d" % N)

    def decrypt(self,e):
        """e is an encrypted message encoded as a polynomial"""
        if self._f is None or self._g is None:
            raise Exception("Private key not found.")

        if e._N <= self._P.get_N():

            if not self._fp:
                self._fp = invert_in_p(self._f, self._P.get_N())
            if not self._fq:
                self._fq = invert_in2tor(self._f, self._P.get_N(), int(lg(self._P.get_q())))

            assert(self._h == self._fq * self._g)

            a = (self._f * e) % self._P.get_q()
            b = (self._fp * a) % self._P.get_p()

            return b # decrypted message
        else:
            raise Exception("e is too large, must be equal or under size %d" % self._P.get_N())

    def is_private(self):
        return self._f is not None and self._g is not None

    def export_public_key(self, kn):
        public_key_string = str(self._P) + "\n" + str(self._h)
        export_public_key_string = base58.b58encode(public_key_string.encode())
        with open(kn+".nky", 'w') as kf:
            kf.write(PUBLIC_HEAD_BLOCK)
            kf.write(export_public_key_string.decode())
            kf.write(END_BLOCK)
            
    def export_private_key(self,kn):
        if self.is_private():
            private_key_string = str(self._P) + "\n" + str(self._h) + "\n" + str(self._f) + "\n" + str(self._g)
            export_private_key_string = base58.b58encode(private_key_string.encode())
            with open(kn+".nky", 'w') as kf:
                kf.write(PRIVATE_HEAD_BLOCK)
                kf.write(export_private_key_string.decode())
                kf.write(END_BLOCK)
        else:
            raise Exception("Private key not found.")
        

def generate_key(params=Standard()):

    f = params.gen_fPoly()
    g = params.gen_gPoly()
    
    fp = invert_in_p(f, params.get_N())
    fq = invert_in_2tor(f, params.get_N(), 8)
    
    h = fq*g

    return NTRUKey(params, h, f, g, fp, fq)

def import_key(key_file):

    with open(key_file, 'r') as kf:
        encoded_key =  kf.read().replace("\n", "")
        encoded_key = encoded_key.replace(PRIVATE_HEAD_BLOCK,"")
        encoded_key = encoded_key.replace(PUBLIC_HEAD_BLOCK,"")
        encoded_key = encoded_key.replace(END_BLOCK,"")

    plain_key = base58.b58decode(encoded_key).decode()
    object_param_list = plain_key.split("\n")

    params = object_param_list[0].split(",")
    params = [int(i) for i in params]
    params = Parameters(params[0],params[1],params[2],params[3],params[4],params[5]) 
    
    h = object_param_list[1].split()
    h = [int(i) for i in h]
    h = poly(h, params.get_N())
    
    f = g = None
    if len(object_param_list) == 4:
        f = object_param_list[2].split()
        f = [int(i) for i in f]
        f = poly(f, params.get_N())

        g = object_param_list[3].split()
        g = [int(i) for i in g]
        g = poly(g, params.get_N())

    if f and g:
        return NTRUKey(params, h, f, g)
    else:
        return NTRUKey(params,h)
