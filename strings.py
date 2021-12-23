#substring (metin parçalama işlemi)

metin="Merhaba Dünya"
print(metin[::-1]) #tersten yazdırır

"""
[a:b:c] 
a başlama indeksi (indeksleme 0 dan başlar)
b bitiş indeksi (b-1 de durur)
c artış miktarı
"""
print(metin[6:2:-2])
print(metin[3:12])
print(metin[3:15]) # son indeksi fazla yazsakta olur, aynı şeydir.

# len() fonksiyonu dizilerde uzunluk bulmaya yarar

#metnin son karakterini yazdırmak istersek
print(metin[(len(metin)-1)])
# -1 yazmamızın nedeni indeksin 0 dan başlamasıdır

# lower(harfleri küçültme) and upper(büyütme)
print(metin.lower())
print(metin.upper())

#replace() fonksiyonu metnin içindeki harfleri değiştirebilmemizi sağlar

isim="mert şimşek"
print(isim.replace("e","a"))
print(isim.replace("mert","muhammet"))

#split and strip
"""
split() fonksiyonu, verilen bir metindeki her kelimeyi 
liste oluşturup içine atar. default olarak boşluğa göre ayırır.Eğer 
başka ayraç kullanmak istersek onu kendimiz fonksiyon içinde belirtiriz
strip() fonksiyonu boşluğu ortadan kaldırır
"""

text="mert şimşek 22 izmir"
print(text.split()) #boşluğu görünce ayır
print(text.split(";")) # ; görünce ayır
print("Adı:"+text.split()[0])