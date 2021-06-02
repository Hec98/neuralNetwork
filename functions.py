import math
from random import random

def printMat(mat):
    for m in mat:
        print(f"  {m}")
    print()
    
e = lambda val: 1/(1 + math.pow(math.e, -1 * val))

numR = lambda: math.cos(random())

