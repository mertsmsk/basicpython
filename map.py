# -*- coding: utf-8 -*-
"""
map() fonksiyonu eşitleme yapmak için kullanılır.
"""

sayilar=[1,2,3,4,5,6]

#sayılar için map uygula.
sayilarKareli=list(map(lambda sayi: sayi**2, sayilar))

#data belirli şartlara göre filtrelenir.
sayilarFiltreli=list(filter(lambda sayi: sayi>2, sayilar))

#reduce kümülatif işler yapmaya yarar.örn faktöriyel
from functools import reduce
sayilarFaktoriyel=reduce(lambda x,y: x*y, sayilar)


print(sayilarKareli)
print(sayilarFiltreli)
print(sayilarFaktoriyel)