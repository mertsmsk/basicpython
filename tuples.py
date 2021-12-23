# listeden farkı değiştirilemez olmasıdır. () ile tanımlanır.
demet=(1,2,3,4,5)
liste=[1,2,3]

print(type(demet))
print(type(liste))

demet2=(1,2,[1,2,3])
demet2[-1][2]=4
print(demet2)

#tek elemanlı tuple tanımlarken parantez yetmez. değerin yanına virgül yazılır.
#tupla da tek eleman ekrana yazdırılırken de elemanın yanına virgül bastırır
demet3=("mert")
print(type(demet3))
demet4=("mert",)
print(type(demet4))
print(demet2[1:2]) #çıktısı (2,) --> sadece indis versek 2 olarak basardı