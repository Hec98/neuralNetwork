from functions import printMat, e, numR, inputD, hidden, output

weight = [[numR(), numR(), numR()], # 00 01 02
          [numR(), numR(), numR()], # 10 11 12
          [numR(), numR(), numR()]] # 20 21 22


n1, n2 = 1, 1
inputD(n1, n2)

tup = hidden(weight, n1, n2)

n3 = tup[0]
n4 = tup[1]
n5 = tup[2]

n6 = output(weight, n3, n4, n5)

