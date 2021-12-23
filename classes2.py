# -*- coding: utf-8 -*-

class Person():
    
    def __init__(self,ad,soyad,yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

person1 = Person("mert","simsek",22)

class Worker(Person): #kalıtım yapmış olduk.
    
    def __init__(self,maas):
        self.maas = maas

class Customer(Person):
    
    def __init__(self,creditNum):
        self.creditNum = creditNum

mert = Worker(0)
ahmet = Customer(0)

mert.maas = 1500
print(mert.maas)