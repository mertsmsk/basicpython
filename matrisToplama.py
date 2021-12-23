# -*- coding: utf-8 -*-

x = [[1,3,5],[7,9,11],[13,15,17]]
y = [[2,4,6],[8,10,12],[14,16,18]]
sonuc =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j] + y[i][j]

print(sonuc)