# -*- coding: utf-8 -*-

#%%
import matematikModul as mm

mm.carp(2,5)
mm.topla(2,5)
isim = mm.customer["name"]
print(isim)

#%%
#%%

#eğer modulden tek bir fonksiyon istiyorsak from yazarız.

from matematikModul import topla

topla(2,5)
#%%