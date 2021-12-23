# sözlük yapısıdır. {} ya da dict ile tanımlanır.

sozluk={
        "book":"kitap",
        "table":"masa"  }
#ilk değişken=anahtar(key)
#ikinci değişken=değer(value)

sozluk["key"]="anahtar" #yeni kelime ekler.
print(sozluk)

sozluk["book"]="kitap 1" #book değerini değiştirir.
print(sozluk)

sozluk2=dict(pencil="kalem",shoes="ayakkabı")
print(sozluk2)

del(sozluk["book"]) #sözlükten book silinir
print(sozluk)
