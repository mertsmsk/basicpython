# -*- coding: utf-8 -*-

class Matematik():
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
    
    def topla(self):
        return self.s1 + self.s2
    
    def cikar(self):
        return self.s1 - self.s2
    
    def carp(self):
        return self.s1 * self.s2
    
    def bol(self):
        return self.s1 / self.s2

mat = Matematik()

sonuc = mat.bol(2,5)
print(sonuc)