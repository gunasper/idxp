import sys
import numpy as np

train="../data/dataset"
test="../data/classificar"

#inicializacao
vetAreas = ['A001', 'A002', 'A003', 'A004', 'A005', 'A006', 'A007', 'A008', 'A009',
	'A010',	'A011', 'A012', 'A013', 'A014', 'A015', 'A016', 'A017', 'A018', 'A019',
	'A020',	'A021', 'A022', 'A023', 'A024', 'A025', 'A026', 'A027', 'A028', 'A029',
	'A030',	'A031', 'A032',
	'A033Front', 'A033Parking']
numAP = 19
database = {}
for i in vetAreas:
	database[i] = []

#leitura da base de dados para a memoria
for line in open(train):
	line = line[:len(line)-1]	
	fingerprint = line.split(',');

	vetorFingerPrint = fingerprint[2:len(fingerprint)]
	area = fingerprint[1]

	x = []	

	#se o RSS de uma medicao faltar algum valor, a medicao recebera valor -100
	for i in range(len(vetorFingerPrint)):
			try:
				valor = float(vetorFingerPrint[i])
			except ValueError:
				valor = -100.0
			x.append(valor)

	database[area].append(x)

treino = {}

#calculo da media dos de fingerprints
for i in database:
	temp = np.array(database[i]).astype(float)
	treino[i] = np.mean(temp, axis=0)
	#treino[i] = np.median(temp, axis=0)

total=0
acertos=0

#testes
for line in open(test):
	line = line[:len(line)-1]	
	fingerprint = line.split(',');

	vetorFingerPrint = fingerprint[2:len(fingerprint)]
	area = fingerprint[1]

	x = []	

	#se o RSS de uma medicao faltar algum valor, a medicao recebera valor -100
	for i in range(len(vetorFingerPrint)):
			try:
				valor = float(vetorFingerPrint[i])
			except ValueError:
				valor = -100.0
			x.append(valor)
	
	#-1 -> exatamente opostos;
	# 1 -> exatamente iguais;
	maisProximo = -1
	vetorRSS = np.array(x)

	#para cada fingerprint precalculado de uma area
	for fp in treino:
		#calculo da distancia de cosseno
		distanciaCosseno = np.dot(vetorRSS,treino[fp]) / (np.linalg.norm(vetorRSS) * np.linalg.norm(treino[fp]))
		if distanciaCosseno > maisProximo:
			maisProximo = distanciaCosseno
			APEncontrado = fp

	if APEncontrado == area:
		acertos+=1
	total+=1

print "acertos:",  acertos
print "total:",  total
print "precisao:", float(acertos)/total





























