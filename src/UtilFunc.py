'''
Created on Apr 23, 2015

@author: Sascha Tetkov
'''

#Groesster Gemiensamer Teiler nache EUKLIDES
def GGT(a,b):
    while a != b:
        if a>b:
            a=a-b 
        else:
            b=b-a 
    return a

#Groesster Gemiensamer Teiler nache EUKLIDES
def GGT_Counting(a,b):
    cnt=0;
    while a != b:
        if a>b:
            a=a-b 
        else:
            b=b-a
        cnt=cnt+1
    print('Iterationen:',cnt) 
    return a


#Fast power according to LEGENDRE
def pot(x,y):
    z=1.0
    while y!=0:
        if y%2==1:
            y=y-1
            z=z*x
        else:
            y=y//2
            x=x*x
    return z

#Fast power according to LEGENDRE with Iteration counter
def pot_Counting(x,y):
    cnt=0
    z=1.0
    while y!=0:
        if y%2==1:
            y=y-1
            z=z*x
        else:
            y=y//2
            x=x*x
        cnt=cnt+1
    print('Iterationen: ',cnt)
    return z


#HP rnd from 1977
def HPRand(z):
    import math
    k=0
    z=z-int(z)
    if z==0:
        z=0.784567731
    while k<10:
        z=z*math.pi
        z=z*z 
        z=z*z
        z=z*z
        z=z-int(z)
        k=k+1
    return z

#checks if two real numbers are sufficiently equal
def gleich(x,y):
    return abs(x-y)<1.0e-10*abs(y)

#binomial coeficient according to Pascal's triangle
def bino(n,k):
    if k==0 or n==k:
        return 1
    else:
        return bino(n-1,k-1) + bino(n-1,k)