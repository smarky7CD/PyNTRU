#!/usr/bin/env python3

from itertools import zip_longest

class Polynomial():

    def __init__(self,c, N):
        self._coeff = strip(c,0)
        self._N = N
        
    def __add__(self, other):
        new_coeff = [sum(x) for x in zip_longest(self, other, fillvalue=0)]
        return Polynomial(new_coeff, self._N)

    def __sub__(self, other):
        return self + (-other)
    
    def scale(self, m):
        """scalar multiplication of polynomial by int m"""
        new_coeff = [m*c for c in self]
        return Polynomial(new_coeff, self._N)
    
    def __mul__(self, other):
        """convolution product of truncated poly ring"""
        if self.isZero() or other.isZero(): return Zero()
        
        tmp_coeff = [0 for _ in range(self._N*2 -1)]

        for i,a in enumerate(self):
            for j,b in enumerate(other):
                tmp_coeff[i+j] += a*b

        trunc1 = tmp_coeff[:self._N]
        trunc2 = tmp_coeff[self._N:]

        new_coeff = [sum(x) for x in zip_longest(trunc1,trunc2,fillvalue=0)]
        return Polynomial(new_coeff, self._N)                     
            
    def __mod__(self, m):
        """ Reducing a polynomial's coeff mod m, also does center-lifting """
        reduced_coeff = list(map(lambda x: x%m if x%m <= m//2 else x%m - m, self))
        return Polynomial(reduced_coeff, self._N)

    def __str__(self):
        return ' '.join([str(c) for c in self])
    
    def __len__(self):
        return len(self._coeff)

    def __iter__(self):
        return iter(self._coeff)

    def __neg__(self):
        return Polynomial([-c for c in self], self._N)
    
    def __eq__(self, other):
        return self.deg() == other.deg() and all([x==y for (x,y) in zip(self,other)])

    def __ne__(self, other):
        return self.deg() != other.deg() and all([x!=y for (x,y) in zip(self,other)])

    def tail_coeff(self):
        return self._coeff[0]
       
    def lead_coeff(self):
        return self._coeff[-1]

    def deg(self):
        return len(self) - 1
    
    def isZero(self):
        return self._coeff == [0]
    
def strip(L, e=0):
    """ strip all copies of e from end of list"""
    if len(L) == 0: return L

    i = len(L) - 1
    while i>=0 and L[i] == e:
        i -= 1

    return L[:i+1]




