from functions2 import printMat, validateN, addData

nHidden = input('Ingresa el número de capas ocultas -> ')
nHidden = validateN(nHidden)

neurons, data = [], []

for x in range(0, nHidden, 1):
   neuron = input(f'Ingrese el número de neuronas de la capa {x+1} -> ')
   neuron = validateN(neuron)
   neurons.append(neuron)

print(f'\nCapas Oculta\n{neurons}')

for y in neurons: data.append(addData(y))

print('\nDatos')
printMat(data)
