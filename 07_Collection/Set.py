"""
SET KÜMME OLARAK GEÇER

Benzersiz ve sırasız öğelerden oluşur.
Matematikteki kümelerle benzer bir yapıya sahiptir.

"""

##### KÜME TANIMLAMA #######

###Boş bir küme oluşturma

# kume = set()
# print(type(kume))

# kume = {1,2,3,4,5,6}
# print(kume)

#Küme içerisinde sırasız bir ifade varsa bunları kendisi random olarak sıralayarak Küme içerisinde bize veriyor.
# karisik_kume = {10,2,23,19,18,1,11,22,100,200,0,-29}
# print(karisik_kume)


#Tekrar eden sayılar küme içerisinden silinir.
# karisik_kume = {10,2,23,19,18,1,11,22,100,200,200}
# print(karisik_kume)

#### ELEMAN EKLEME ####
##Eleman ekleme işleminde rastgelelik vardır.Elemanın ekleneceği index belirli değildir.
# karisik_kume.add(150)
# karisik_kume.add(120)
# karisik_kume.add(180)
# print(karisik_kume)
#
# karisik_kume.add(170)
# print(karisik_kume)

#Var olan eleman eklenmek istenirse ekleme  işlemi gerçekleşmez.Çünkü bir elemandan bir adet bulunmalı.
# karisik_kume.add(170)
# print(karisik_kume)


### ELEMAN SİLME ####
##Silinmek istenen eleman küme içerisinde yoksa KeyError hatası verir ve uygulama çöker
# karisik_kume.remove(300)
# print(karisik_kume)

#Silinmek istenen eleman kümede yoksa hata vermez.
# karisik_kume.discard(3000)
# print(karisik_kume)


##### POP ile eleman silme ####
#ELEMAN silme işlemini rastgele olarak sağlar.
# kume = {20,30,11,10,5,45,120}
# print(id(kume))
# silinenEleman = kume.pop()
# print(silinenEleman)
# print(kume)
#silinenEleman = kume.pop()
# print(id(silinenEleman))
# print(silinenEleman)
# while True:
#     silinenEleman = kume.pop()
#     print(silinenEleman)

##### KÜME OPERASYONLARI

## Union
kume1 = {20, 30, 11, 10, 5, 45, 120}
kume2 = {10,34,18,20,5,55,45,19}

# birlesim = kume1.union(kume2)
#
# print(birlesim)
# print(kume1 | kume2)

#İntersection() Kesişim
#
# kume1 = {20, 30, 11, 10, 5, 45, 120}
# kume2 = {10,34,18,20,5,55,45,19}
#
# kesisim = kume1.intersection(kume2)
# print(kesisim)
#
# print(kume1 & kume2)

#FARK Difference()
# kume1 = {20, 30, 11, 10, 5, 45, 120}
# kume2 = {10,34,18,20,5,55,45,19}
#
# fark = kume1.difference(kume2)
# print(fark)
#
# print(kume1 - kume2)

##Simetrik Fark ()
#İki kümenin birbirlerine göre olan farklılıklarını tek bir küme üzerinde toplar.
# kume1 = {20, 30, 11, 10, 5, 45, 120}
# kume2 = {10,34,18,20,5,55,45,19}
#
# simetrikFark = kume1.symmetric_difference(kume2)
# print(simetrikFark)
#
# #print(kume1 ^ kume2)

##### ALT KÜME ÜST KÜME

kume1 = { 1, 2, 3, 4}
kume2 = {1,2}
print(kume1.issuperset(kume2))
print(kume2.issubset(kume1))
