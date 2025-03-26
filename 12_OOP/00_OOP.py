import random
"""
OOP(Object Oriented Programming)

OOP Prensipleri

INHERITANCE(Miras Alma)
ENCAPSULATION(Kapsülleme)
POLYMORPHISM(Çok biçimlilik)
ABSTRACTION(SOYUTLAMA)


CLASS

Nesnelerin şablonudur.

(OBJECT) Sınıflardan türetilmiş somut varlıklardır.


Class Nasıl Tanımlanır ?
Class içerisinde tanımlanan kapısayısı renk motorgucu gibi değişkenler o classın propertysi olarak geçer

class Araba:
    kapiSayisi = ""
    renk = ""
    motorGucu = 0

Classlar nasıl kullanılır ?

Instance(Örnek oluşturma)



"""



# class Araba:
#     kapiSayisi = ""
#     renk = ""
#     motorGucu = 0
#
#
# yeniAraba = Araba()
# yeniAraba.renk = "Kırmızı"
# yeniAraba.kapiSayisi = "4"
# yeniAraba.motorGucu = "400"
#
#
# print(f"{yeniAraba.renk} {yeniAraba.motorGucu} {yeniAraba.kapiSayisi}")



class Ogrenci:
    isim = ""
    soyisim = ""
    yas = ""



# yeniOgrenci = Ogrenci()
# yeniOgrenci.isim = "Tarık"
# yeniOgrenci.soyisim = "Hamarat"
# yeniOgrenci.yas = "28"
#
#
# yeniOgrenci2 = Ogrenci()
# yeniOgrenci2.isim = "Deniz"
# yeniOgrenci2.soyisim = "Özerdoğan"
# yeniOgrenci2.yas = "30"


# list.append(yeniOgrenci)
# list.append(yeniOgrenci2)

ogrenciIsimler = ["Tarık","Berna","Deniz","Sercan","Yusuf","Halit","Ozan","Yasemin","Furkan","Berfin","Burak","Yağız"]
ogrenciSoyisimler = ["Çalışkan","Yetenekli","Başarılı","Zeki","Çevik","Saygılı","Güneş","Ay","Tar","Öz","Eminoğlu","Ali"]
ogrenciYaslar = ["30","25","13","40","50","20","18","29","40","55","10","20"]

ogrenciListesi = []


for i in range(5):

    rastgeleIsimIndex = random.randint(0, len(ogrenciIsimler)-1)
    rastgeleSoyisimIndex = random.randint(0, len(ogrenciSoyisimler)-1)
    rastgeleYasIndex = random.randint(0, len(ogrenciYaslar)-1)

    yeniOgrenci = Ogrenci()
    yeniOgrenci.isim = ogrenciIsimler[rastgeleIsimIndex]
    yeniOgrenci.soyisim = ogrenciSoyisimler[rastgeleSoyisimIndex]
    yeniOgrenci.yas = ogrenciYaslar[rastgeleYasIndex]
    ogrenciListesi.append(yeniOgrenci)



#Liste içerisindeki nesnelerin ekrana yazdırılması
# for index,ogrenci in enumerate(ogrenciListesi):
#     print(f"{index}-İsim:{ogrenci.isim}-Soyisim:{ogrenci.soyisim}-Yaş:{ogrenci.yas}")

#Liste içerisinde aranan herhangi bir nesnenin ekrana getirilmesi.
# userIndex = int(input("İd giriniz:"))
#
# bulunanOgrenci = ogrenciListesi[userIndex]
#
#
# print(bulunanOgrenci.isim , bulunanOgrenci.soyisim , bulunanOgrenci.yas)

#Alternatif Eleman bulma ve ekrana yazdırma

# userIndex = int(input("İd giriniz:"))
#
# for i in range(len(ogrenciListesi)):
#     if userIndex == i:
#         print(ogrenciListesi[i].isim ,  ogrenciListesi[i].soyisim, ogrenciListesi[i].yas)
#         break


#ALTERNATİF ELEMAN BULMA

# userIndex = int(input("İd giriniz:"))
#
# for index,ogrenci in enumerate(ogrenciListesi):
#     if userIndex == index:
#         print(ogrenci.isim,ogrenci.yas,ogrenci.soyisim)
#         break



##### ELEMAN SİLME ######
# for index,ogrenci in enumerate(ogrenciListesi):
#     print(f"{index}-İsim:{ogrenci.isim}-Soyisim:{ogrenci.soyisim}-Yaş:{ogrenci.yas}")
#
# userIndex = int(input("İd giriniz:"))
#
# ogrenciListesi.remove(ogrenciListesi[userIndex])
#
#
#
# for index,ogrenci in enumerate(ogrenciListesi):
#     print(f"{index}-İsim:{ogrenci.isim}-Soyisim:{ogrenci.soyisim}-Yaş:{ogrenci.yas}")


####### ELEMAN GÜNCELLEME #########
# for index,ogrenci in enumerate(ogrenciListesi):
#      print(f"{index}-İsim:{ogrenci.isim}-Soyisim:{ogrenci.soyisim}-Yaş:{ogrenci.yas}")
#
# userIndex = int(input("İd giriniz:"))
#
# bulunanOgrenci = ogrenciListesi[userIndex]
#
# bulunanOgrenci.isim = input("Yeni isim giriniz")
#
# for index,ogrenci in enumerate(ogrenciListesi):
#      print(f"{index}-İsim:{ogrenci.isim}-Soyisim:{ogrenci.soyisim}-Yaş:{ogrenci.yas}")

















