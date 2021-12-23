# -*- coding: utf-8 -*-


sayi = int(input("Sayı girin : "))

asalMi = True

while True:
    if sayi <= 1:
        print("Asal sayılar 2'den başlar!")
        break
    else:
        for i in range(2,sayi):
            if sayi%i == 0:
                asalMi = False
                break

    if asalMi == True:
        print("Asal")
    else:
        print("Asal Değil")
    
    break