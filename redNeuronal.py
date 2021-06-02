from functions import printMat, e, numR
n1, n2 = 1, 1
w13, w14, w15 = numR(), numR(), numR()
w23, w24, w25 = numR(), numR(), numR()
w36, w46, w56 = numR(), numR(), numR()

weight = [[numR(), numR(), numR()], # 00 01 02
          [numR(), numR(), numR()], # 10 11 12
          [numR(), numR(), numR()]] # 20 21 22

print("Weight\n")
printMat(weight)

print("Input\n")
print(f"n1 = {n1}\nn2 = {n2}\n")

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

print("Output\n")

matF = [[n3 * weight[2][0]],
        [n4 * weight[2][1]],
        [n5 * weight[2][2]]]
printMat(matF)

n6 = matF[0][0] + matF[1][0] + matF[2][0]
print(n6)
n6 = e(n6)
print(f"\nn6 = {n6}")   
