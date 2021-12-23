# -*- coding: utf-8 -*-

sayi = int(input("Sayı: "))

faktoriyel = 1

if sayi < 0:
    print("negatif sayıların faktöriyeli olmaz!")
elif sayi == 0:
    print(sayi,"ın faktöriyeli 1 dir")
else:
    for i in range(1,sayi+1):
        faktoriyel *= i
    print(sayi,"sayısının faktöriyeli:",faktoriyel)
