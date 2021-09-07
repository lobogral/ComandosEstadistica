from math import prod

def factorial(n):
    if (n > 1):
        return n * factorial(n-1)
    else:
        return 1

def P(n,r):
    return factorial(n) // factorial (n-r)

def PClase(n, *args):
    return factorial(n) // prod([factorial(i) for i in args])

def C(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))