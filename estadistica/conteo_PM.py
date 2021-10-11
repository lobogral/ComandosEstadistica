from math import prod


def factorial(n):
    return n * factorial(n-1) if n > 1 else 1


def nP(n, r):
    return factorial(n) // factorial(n-r)


def nT(n, list_args):
    mult = prod([factorial(i) for i in list_args])
    return factorial(n) // mult


def nC(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))
