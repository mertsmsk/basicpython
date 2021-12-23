# -*- coding: utf-8 -*-

liste = ["Muhammet","Mert","Simsek",
         "SuleymanDemirelUniversitesi",
         "BilgisayarMuhendisligi"]

fileAppend = open("dosya.txt","a")

for i in liste:
    fileAppend.write(i)
    fileAppend.write("\n")

fileAppend.close()