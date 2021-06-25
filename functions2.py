from math import cos
from random import random

numR = lambda: cos(random())

def printMat(mat):
    for m in mat: print(f"{m}")
    print()

def validateN(n):
    try:
        n = int(n)
        return n
    except:
        print('Dato no valido')
        exit()

def addData(n):
    data = []
    for x in range(0, n, 1): data.append(x)
    return data
