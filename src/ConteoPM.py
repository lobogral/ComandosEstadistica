def __prod(lista):
    if (lista == []):
        return 1
    else:
        return lista[0]*__prod(lista[1:])

def factorial(n):
    if (n > 1):
        return n * factorial(n-1)
    else:
        return 1

def P(n,r):
    return factorial(n) // factorial (n-r)

def PClase(n, *args):
    return factorial(n) // __prod([factorial(i) for i in args])

def C(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))