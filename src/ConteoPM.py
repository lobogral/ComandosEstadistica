from math import prod

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

def nP(n,r):
    """
    Calcula el numero de permutaciones
    n -> Numero de objetos totales
    r -> Numero de objetos tomados
    """
    return factorial(n) // factorial (n-r)

def nT(n, listArgs):
    """
    Calcula el numero de permutaciones de clase
    n -> Numero de objetos totales
    listArgs -> 
      Lista de numeros (n1,...,nk) tales 
      que n1 + ... + nk = n
    """
    mult = prod([factorial(i) for i in listArgs])
    return factorial(n) // mult

def nC(n,r):
    """
    Calcula el numero de combinaciones
    n -> Numero de objetos totales
    r -> Numero de objetos tomados
    """
    return factorial(n) // (factorial(r) * factorial(n-r))