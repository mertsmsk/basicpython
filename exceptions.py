# -*- coding: utf-8 -*-

try:
    sayi=int(input("sayı gir:"))
    print("devam")
    
except ValueError:
    print("ValueError:Lütfen sayı giriniz!")

except:
    print("hata oluştu!")