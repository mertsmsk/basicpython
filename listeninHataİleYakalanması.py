# -*- coding: utf-8 -*-
import sys

array=['mert',0,3,"6"]

    
for x in array:
    try:        
        print("Sayı:",x)
        sonuc=1/int(x)
        print("Sonuç:",sonuc)    

    except:
        print(sys.exc_info()[0])