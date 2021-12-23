#benzersiz elemanlardan oluşur. hepsi farklıdır.
#sırasız elemanlardır.
#süslü parantezle tanımlanır {} ya da set() keywordu ile tanımlanır.

studentsSet={"mert","ali","anıl"}
print(studentsSet)

for i in studentsSet:
    print(i)

if "mert" in studentsSet:
    print("listede var")

print("salim" in studentsSet) #boolean döndürür.

studentsSet.add("salim")
print(studentsSet)

studentsSet.update(["yusuf","sülo"])
print(studentsSet)

print(len(studentsSet))
studentsSet.remove("yusuf")
print(len(studentsSet))
studentsSet.discard("yusuf")
print(len(studentsSet)) 
#remove, değeri bulamayınca hata verir.
#hata almak istemiyorsak discard metodunu kullanırız.

print(studentsSet.pop()) #son elemanı siler ve ekrana basar.
studentsSet.clear() #setin içini temizler.
del studentsSet #seti bellekten siler.

"""
set union işlemi, setler arasındaki ortak verileri bir kez yazıp veri tekrarını kaldırır.
"""
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}
print(setA.union(setB))
# YA DA
print(setA | setB)

"""
intersection ise kesişim kümelerini yazdırır.
"""
print(setA.intersection(setB))
# YA DA
print(setA & setB)

"""
set difference farklı olan elemanları bastırır.
"""
print(setA.difference(setB))
print(setA - setB)
print(setB.difference(setA))

"""
symmetric difference iki kümenin farklarını birleştirip basar.
"""
print(setA.symmetric_difference(setB))
print(setA ^ setB)
