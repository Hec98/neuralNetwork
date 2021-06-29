from math import cos
from random import random

numR = lambda: cos(random())

def printMat(mat, tex = ''):
    print(f'\n {tex}')
    for m in mat: 
        p = ''
        for n in m: p += f' {n} '
        print(f"{p}")

def validateN(n):
    try:
        n = int(n)
        return n
    except:
        print('Dato no valido')
        exit()

def addData(n, n2 = 0):
    data = []
    count = 0
    while count < n:
        data.append(n2)
        count += 1
    return data
