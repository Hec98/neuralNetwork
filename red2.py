from functions2 import printMat, validateN, addData, numR

nHidden = input('Ingresa el número de capas ocultas -> ')
nHidden = validateN(nHidden)

neurons, data, weights = [], [], []

for x in range(0, nHidden, 1):
   neuron = input(f'Ingrese el número de neuronas de la capa {x+1} -> ')
   neuron = validateN(neuron)
   neurons.append(neuron)

print(f'\nCapas Oculta\n{neurons}')

for y in neurons: 
    data.append(addData(y))
    weights.append(addData(y, numR()))

printMat(data, 'Datos')
printMat(weights, 'Pesos')
printMat(neurons)
