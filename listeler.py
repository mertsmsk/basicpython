# -*- coding: utf-8 -*-

liste=list(("mert",2,5,"şimşek"))
print(liste)
print(len(liste))

liste2=[1,2,'a',"mert",5]
print(liste2)
liste2.append(6) #append() listeye eleman ekler
liste2.remove("a") #remove() listeden eleman siler
print(liste2)
#index() girdiğimiz değerin hangi indexte olduğunu söyler
print(liste2.index("mert"))

sehirler=["istanbul","ankara","izmir"]
print("izmir sayısı=",sehirler.count("izmir")) 
#count() girdiğim verinin listede kaç defa olduğunu söyler

liste3=[1,2,3,4,5]
liste3.remove(liste3[1])
print(liste3)
# pop() işleminde verdiğimiz indeksteki eleman silinir.index girmezsek sondakini siler.
print(liste3.pop(),liste3,sep="\n") #sildiği elemanı ekrana basar

#insert() istediğimiz indekse istediğimiz değeri ekler
liste3.insert(1,2)
print(liste3)

#reverse() listeyi tersine çevirir
liste3.reverse()
print(liste3)

"""
diziler referans tiplidir yani liste2=liste dediğimde ikisi de aynı yeri gösterir.
int teki gibi farklı yer ayrılmaz. 
bellekte farklı yer ayırmak için copy() fonksiyonu kullanılır!!!
"""
liste4=liste3.copy()
liste4[3]=0
print(liste3)
print(liste4)

#extend() listeleri birbirine eklemeye yarar
liste3.extend(liste4) #liste4 liste3 e eklendi

#sort() liste elemanlarını küçükten büyüğe doğru sıralar
liste3.sort()
print(liste3)