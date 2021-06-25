from functions import w, epsilon, inputD, hidden, output

weight = w()

def red(weight):
    n1, n2 = 1, 1
    inputD(n1, n2)
    n = hidden(weight, n1, n2)
    n3 = n[0]
    n4 = n[1]
    n5 = n[2] 
    n6 = output(weight, n3, n4, n5)
    return n6

original = red(weight)

for x in range(0, 1000):
    weight = epsilon(weight)

segunda = red(weight)

if segunda < original: print(f"Se redujo de {original} a {segunda}")
