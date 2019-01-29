#!/usr/bin/env python3

# !!! Won't actually work, stolen from C pseudo-code !!!

def polyMult(a,b,c,n,N):
    """
    This is a recusive trunc poly multiplication routine.
    It runs in about O(.75n^2).
    Computes the c*b and stores the result in a.  
    Polys b and c have degree n-1.
    Routine is recalled recursively until polys have deg < cutOff.
    If N>0, prodcuted is computeed as a convolution; X^N = 1.
    """
    cutOff = 32 # experimentally determined optimal value

    # for small n, compute the product directly
    if n < cutOff:
        for k in range(2*n-1):
            a[k] = 0
            start = max(0,k-n+1)
            stop = min(k+1,n)
            for i in range(start,stop):
                a[k] += b[i]*c[k-i]
    # otherwise n is large, compute the product recursively         
    else:
        n1 = n//2
        n2 = n -n1
        # write b as b = b1 + b2X^n1 
        # write c as c = c1 + c2X^n1
        B = b1 + b2 # deg n2-1
        C = c1 + c2 # deg n2-1
        a1 = b1 * c1
        polyMult(a1,b1,c1,n1,N)
        a2 = b2*c2
        polyMult(a2,b2,c2,n2,N)
        a3 = B*C
        polyMult(a3,B,C,n2,N)
        a = a1 + (a3-a1-a2)*X^(n1) + a2*X^(2*n1)

        if 2*n-1 > N and N > 0:
            for k in range(N, 2*n-1):
                a[k-N] += a[k]

