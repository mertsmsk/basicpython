# -*- coding: utf-8 -*-
 
#değişken ismi verip open komutuyla dosya adını yazarız.
#virgülden sonra default olarak r vardır.dosyayı açar.
#dosya yoksa hata verir.
#w koyarsak okuma işlemi yapar.dosya yoksa oluşturur.
#a koyarsak hem okur hem değiştirme yapılır.
#x yazarsak dosyayı oluştur demektir.
#r read,a append,w write,x create

#%%
f = open("musteriler.txt")
print(f.readline()) #ilk satırı okuduk

for line in f:
    print(line) #kalan satırları okuduk.

#okunan satırı tekrar okumadı.

f.close() #dosyayı kapatır.
#%%

#%%
fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("Muhammet\n")
fileToAppend.write("Mert")
fileToAppend.close()
#%%

#%%
fileToAppend = open("ogrenciler.txt","w")
fileToAppend.write("Muhammet\n")
fileToAppend.write("Mert")
fileToAppend.close()
#%%

#dosyaları silmek için os modülü kullanılır.

import os

if os.path.exists("dosyaAdi.txt"):
    os.remove()
else:
    print("Dosya yok!")

#klasör silmek için rmdir kullanılır.(remove directory)

#os.rmdir("klasör adı")
#%%