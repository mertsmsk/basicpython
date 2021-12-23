# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:48:57 2019

@author: merts
"""

#json datası için json import edilmeli

import json

data = '{"name":"mert","surname":"simsek","yas":"22"}'
print(type(data))

jdata = json.loads(data) #string jsona çevirildi.

print(type(jdata))

print(jdata["name"])
print(jdata["yas"])

print(jdata) #json formatında basar.

data2 = {"isim":"muhammet",
         "email":"mertsmsk70@gmail.com"}

jdata2 = json.dumps(data2) #python nesneleri dumps ile json olur. kontrol et!!
print(data2)

print(type(data2))
print(type(jdata2))

print(json.dumps("mert"))
print("mert")






