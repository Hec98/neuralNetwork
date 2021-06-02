import math
from random import random

def printMat(mat):
    for m in mat:
        print(f"  {m}")
    print()
    
e = lambda val: 1/(1 + math.pow(math.e, -1 * val))

numR = lambda: math.cos(random())

def inputD(n1, n2):
    print("Input\n")
    print(f"n1 = {n1}\nn2 = {n2}\n")

def hidden(weight, n1, n2):
    print("Hidden\n")     
                      
    mat = [[weight[0][0] * n1, weight[0][1] * n2], 
           [weight[0][2] * n1, weight[1][0] * n2], 
           [weight[1][1] * n2, weight[1][2] * n1]]
                      
    printMat(mat)         
                      
    madAdd = [[mat[0][0] + mat[0][1]], 
              [mat[1][0] + mat[1][1]],
              [mat[2][0] + mat[2][1]]]

    printMat(madAdd)

    madAdd[0][0] = e(madAdd[0][0])
    madAdd[1][0] = e(madAdd[1][0])
    madAdd[2][0] = e(madAdd[2][0])

    printMat(madAdd)

    n3, n4, n5 = madAdd[0][0], madAdd[1][0], madAdd[2][0]
    print(f"n3 = {n3}\nn4 = {n4}\nn5 = {n5}")
    return n3, n4, n5

def output(weight, n3, n4, n5):
    print("Output\n")

    matF = [[n3 * weight[2][0]],
            [n4 * weight[2][1]],
            [n5 * weight[2][2]]]
    printMat(matF)

    n6 = matF[0][0] + matF[1][0] + matF[2][0]
    print(n6)
    n6 = e(n6)
    print(f"\nn6 = {n6}")
    return n6
