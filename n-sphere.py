# coding: latin-1

class PiFraction(object):
    num = 0
    den = 0
    pi = 0
    
    def __init__(self, n, p, d):
        self.num = n
        self.den = d
        self.pi = p

def Multiply(pf1, pf2):
    return PiFraction(pf1.num * pf2.num, pf1.pi + pf2.pi, pf1.den * pf2.den)

# Euclid's Algorithm to find the greatest common divisor is more efficient
def Reduce(pf):
    n = pf.num
    d = pf.den
    for i in range(2, int(min(n, d)) + 1):
        while (n % i == 0 and d % i == 0):
            n = n / i
            d = d / i
    return PiFraction(int(n), pf.pi, int(d))

# F(n) = definite integral of cos(x)^n dx from -pi/2 to pi/2
def F(n):
    num = 1
    den = 1
    for i in range(1, n + 1):
        if (i % 2 == n % 2):
            den *= i
        else:
            num *= i
    if (n % 2 == 0):
        return PiFraction(num, 1, den)
    else:
        return PiFraction(num * 2, 0, den)
        
def dimensionalConstant(dimension):
    dc = PiFraction(1, 0, 1)
    for i in range (1, dimension + 1):
        dc = Reduce(Multiply(dc, F(i)))
    return dc

def printFormula(dc, dimension):
    pi = "π"
    numerator = ""
    if (dc.num != 1 or dc.pi == 0):
        numerator += str(dc.num)
    if (dc.pi != 0):
        if (dc.pi == 1):
            numerator += pi
        else:
            numerator += pi + "^"
            numerator += str(dc.pi)
            numerator += "."
    if (dimension != 0):
        if (dimension == 1):
            numerator += "r"
        else:
            numerator += "r^"
            numerator += str(dimension)
    print(numerator)
    if (dc.den != 1):
        line = ""
        for i in range (0, len(numerator)):
            line += "-"
        print(line)
        print(dc.den)
    print()
    
def printVolume(dimension):
    printFormula(dimensionalConstant(dimension), dimension)

def printSurfaceArea(dimension):
    dimC = Reduce(Multiply(PiFraction(dimension, 0, 1), dimensionalConstant(dimension)))
    printFormula(dimC, dimension - 1)

for d in range (1, 10):
    num = str(d) + "-sphere"
    print(num)
    print()
    print("Volume:")
    printVolume(d)
    print("Surface Area:")
    printSurfaceArea(d)
    print()
