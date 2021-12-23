# -*- coding: utf-8 -*-

def toplama():
    s1 = int(input("s1:"))
    s2 = int(input("s2:"))
    print("Sonuç:",s1+s2)

def cikarma():
    s1 = int(input("s1:"))
    s2 = int(input("s2:"))
    print("Sonuç:",s1-s2)

def carpma():
    s1 = int(input("s1:"))
    s2 = int(input("s2:"))
    print("Sonuç:",s1*s2)

def bolme():
    s1 = int(input("s1:"))
    s2 = int(input("s2:"))
    
    if s2 == 0:
        print("Tanımsız!")
    else:
        print("Sonuç:",s1/s2)

islem = int(input("""
1- Toplama
2- Çıkarma
3- çarpma
4- Bölme

işlem Seçiniz: """))

if islem == 1:
    toplama()

elif islem == 2:
    cikarma()
    
elif islem == 3:
    carpma()
    
elif islem == 4:
    bolme()

else:
    print("Hatalı işlem!..")
