#!/usr/bin/env python3

from poly import Polynomial

def invert_in_2(a,N):
    """ fast inverse algorithm mod 2 """
    k = 0
    b,c = One(N), Zero(N)
    f,g = a, RingPoly(N)
    
    while True:

        while f.tail_coeff() == 0:
            f_list = list(f)
            f = Polynomial(f_list[1:], N)
            c_list = list(c)
            c = Polynomial([0] + c_list, N)
            k+=1
            
        if f == Polynomial([1], N):
            return b*Xnk(N,k)

        if f.deg() < g.deg():
            f,g =g,f
            b,c = c,b

        f = (f+g) % 2
        b = (b+c) % 2
        
def invert_in_2tor(a, N, r):
    """ fast inverse algorithm mod 2^r"""
    b = invert_in_2(a,N)
    q = 2
    
    while q < 2**r:
        q = q**2
        b = (b * (Polynomial([2],N) - (a*b))) % q
    return b

def invert_in_p(a, N):
    """fast inverse algorithm mod 3"""
    k = 0
    b, c = One(N), Zero(N)
    f, g = a, RingPoly(N)

    while True:

        while f.tail_coeff() == 0:
            f_list = list(f)
            f = Polynomial(f_list[1:], N)
            c_list = list(c)
            c = Polynomial([0] + c_list, N)
            k+=1
        
        if f == Polynomial([-1], N):
            return -b*Xnk(N,k)
        if f == Polynomial([1], N):
            return b*Xnk(N,k)

        if f.deg() < g.deg():
            f,g = g,f
            b,c = c,b

        if f.tail_coeff() == g.tail_coeff():
            f = (f-g) % 3
            b = (b-c) % 3
        else:
            f = (f+g) % 3
            b = (b+c) % 3
            
def Zero(N):
    """generate zero polynomial"""
    return Polynomial([0], N)

def One(N):
    """generate one polynomial"""
    return Polynomial([1], N)

def Xnk(N,k):
    """generate X^(N-k) polynomial"""
    xnk = [0 for _ in range(N+1)]
    xnk[N-k-1] = 1
    return Polynomial(xnk, N)

def RingPoly(N):
    """generate X^(N-1) polynomial"""
    rp_coeff = [0 for _ in range(N+1)]
    rp_coeff[0] = -1
    rp_coeff[-1] = 1
    return Polynomial(rp_coeff, N) 



