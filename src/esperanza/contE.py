from distribuciones import conjuntaContinua as conjCont

establecerFdp = conjCont.establecerFdp

def E(func):
    return conjCont.ProbTotal(func*conjCont.fdp)
