# -*- coding: utf-8 -*-


s1=int(input("sayı:"))
s2=int(input("sayı:"))
s3=int(input("sayı:"))

if s1>=s2 and s1>=s3:
    enBuyuk=s1
elif s2>=s1 and s2>=s3:
    enBuyuk=s2
else:
    enBuyuk=s3

print("En büyük sayı:",enBuyuk)