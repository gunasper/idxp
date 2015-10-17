# -*- coding: utf-8 -*-
import sys
import numpy as np
import math
from sklearn import svm

train="../data/dataset"
test="../data/classificar"

from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier, KNeighborsRegressor
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn import tree
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

vetAreas = ['A001', 'A002', 'A003', 'A004', 'A005', 'A006', 'A007', 'A008', 'A009',
	'A010',	'A011', 'A012', 'A013', 'A014', 'A015', 'A016', 'A017', 'A018', 'A019',
	'A020',	'A021', 'A022', 'A023', 'A024', 'A025', 'A026', 'A027', 'A028', 'A029',
	'A030',	'A031', 'A032',
	'A033Front', 'A033Parking']
numAP = 19

treino = []
classes = []

numAmostras = {}
prevCorretas = {}
prevTotal = {}
prevErradas = {}

for area in vetAreas:
	#número de amostras numa determinada área
	numAmostras[area] = 0
	#número de previsões CORRETAS para uma determinada área		
	prevCorretas[area] = 0
	#número de previsões para uma determinada área
	prevTotal[area] = 0
	#número de previsões ERRADAS para uma determinada área		
	prevErradas[area]=0


count = 0

#calcula o fingerprint para cada area
for line in open(train):
	count +=1
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

	treino.append(x)
	classes.append(area)

X = treino
y = classes
C = 1.0

#clf = KNeighborsClassifier(n_neighbors=70).fit(treino,classes) #39%
#clf = svm.SVC(kernel='linear', C=C).fit(X, y) #43%
#clf1 = DecisionTreeClassifier(min_samples_split=80).fit(X,y)
#clf = RadiusNeighborsClassifier(radius=400.0).fit(X, y)
#clf = MultinomialNB(alpha=20.2).fit(X,y)
#clf = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y) #3%
#clf = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y) #38% com mto problema de performance
#clf = svm.LinearSVC(C=C).fit(X, y)


#variaveis para calcular precisao
acerto = 0
total = 0

#para cada linha do teste
for line in open(test):
	line = line[:len(line)-1]	
	fingerprint = line.split(',');

	vetorFingerPrint = fingerprint[2:len(fingerprint)]
	area = fingerprint[1]

	x = []
	#se o fingerprint de uma medicao faltar algum valor, este fingerprint sera descartado
	for i in range(len(vetorFingerPrint)):
			try:
				valor = float(vetorFingerPrint[i])
			except ValueError:
				valor = -100

			x.append(valor)
	
	APEncontrado = clf.predict([x])

	prevTotal[APEncontrado[0]]+=1

	if APEncontrado == area:
		acerto+=1
		prevCorretas[area] +=1
	else:
		prevErradas[area] +=1
	total+=1

print "acertos:",  acerto
print "total:",  total
print "%", float(acerto)/total
for i in prevTotal:
	try:
		#print i, 'acertos:', prevCorretas[i], '  erros:', prevErradas[i], '  tentativas: ', prevTotal[i], '  % acertos/tentativas:', float(prevCorretas[i])/prevTotal[i]
		x = float(prevCorretas[i])/(prevCorretas[i]+prevErradas[i])
		y = float(prevCorretas[i])/prevTotal[i]
		#print i, '\t&', prevCorretas[i], '\t&', prevErradas[i], '\t& ', prevTotal[i], '\t&', "%.2f" % y, '\t&', "%.2f" % x, "\\\\"
	except:
		print
