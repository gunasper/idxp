#esse script calcula os valores minimos e maximos de cada RSS para uma dada area

import sys
import numpy as np

numAP = 19
medicoes = [[]*numAP for j in range(numAP) ]

for line in sys.stdin:
	line = line[:len(line)-1]
	valores = line.split(',')

	for i in range(numAP):
		valor = -1* float(valores[i])
		medicoes[i].append(valor)

for i in range(numAP):
	if (i<9):
		AP = 'AP0' + str(i+1)
	else:
		AP = 'AP' +str(i+1)
	est = np.array(medicoes[i])
	print AP,'\t', est.min(), '\t', est.max(), '\t', est.mean(), '\t', est.std()
