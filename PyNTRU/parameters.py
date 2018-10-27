#!/usr/bin/env python3

from poly import Polynomial as poly
import Crypto.Random.random as CR

class Parameters():

    def __init__(self, N, p, q, df, dg, dr):
        """Security paramaters for NTRU"""
        self._N = N
        self._p = p
        self._q = q
        self._df = df
        self._dg = dg
        self._dr = dr

    def gen_fPoly(self):
        """ Generate a f private key """
        fp = [0] * self._N
        p1 = 0
        while p1 != self._df+1:
            x = CR.randint(0,self._N-1)
            if fp[x] == 0:
                fp[x] = 1
                p1+=1
            else:
                pass
        n1 = 0
        while n1 != self._df:
            y = CR.randint(0,self._N-1)
            if fp[y] == 0:
                fp[y] = -1
                n1+=1
            else:
                pass
        return poly(fp, self._N)

    def gen_gPoly(self):
        """ Generate a g private key """
        gp = [0] * self._N
        p1 = 0
        while p1 != self._dg:
            x = CR.randint(0,self._N-1)
            if gp[x] == 0:
                gp[x] = 1
                p1+=1
            else:
                pass
        n1 = 0
        while n1 != self._dg:
            y = CR.randint(0,self._N-1)
            if gp[y] == 0:
                gp[y] = -1
                n1+=1
            else:
                pass
        return poly(gp, self._N)

    def gen_rPoly(self):
        """ Generate a random r for security parameters """
        rp = [0] * self._N
        p1 = 0
        while p1 != self._dr:
            x = CR.randint(0,self._N-1)
            if rp[x] == 0:
                rp[x] = 1
                p1+=1
            else:
                pass
        n1 = 0
        while n1 != self._dr:
            y = CR.randint(0,self._N-1)
            if rp[y] == 0:
                rp[y] = -1
                n1+=1
            else:
                pass
        return poly(rp, self._N)
    
    def get_N(self):
        return self._N

    def get_p(self):
        return self._p

    def get_q(self):
        return self._q

    def get_df(self):
        return self._df + 1, self._df

    def get_dg(self):
        return self._dg, self._dg

    def get_dr(self):
        return self._dr, self._dr


class Moderate(Parameters):
    """ Moderate security standards """
    def __init__(self):
        Parameters.__init__(self, 107, 3, 64, 14, 13, 5)
        
class High(Parameters):
    """ High security standards """
    def __init__(self):
        Parameters.__init__(self, 167, 3, 128, 60, 20, 18)
        
class Highest(Parameters):
    """ Highest security standards"""
    def __init__(self):
        Parameters.__init__(self, 503, 3, 256, 215, 72, 55)
