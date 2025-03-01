"""
DICTIONARY(Sözlük)

"key":"value"


"""

# araba = {"VitesTürü":"Otomatik","KapıSayısı":2}
# print(type(araba))
# print(araba)
#
# kisi = dict(isim="Tarık",yas="30")
# print(kisi)


#Listeyle Dictionary oluşturma
# bilgisayar = [("Marka","Dell"),("Yıl","2018")]
# yeniSozluk = dict(bilgisayar)
#
# print(yeniSozluk)
# print(type(yeniSozluk))



###################### SÖZLÜK VERİLERİNE ERİŞİM ##########################
#araba = {"VitesTürü":"Otomatik","KapıSayısı":2}

#Bu erişim yöntemiyle eğer key değeri sözlükte bulunmuyorsa KeyError hatası alırsınız
#print(araba["TekerSayisi"])
#Get ile birlikte Key değeri arandığında bulunamazsa None cevabını alırsınız.Uygulama çökmez
#print(araba.get("TekerSayisi"))


############___DÖNGÜ İLE ERİŞİM___#########
# for value in araba.values():
#     print(value)

# for key in araba.keys():
#     print(key)


# for key , value in araba.items():
#     print(f"{key}:{value}")



##################### SÖZLÜK İÇERİSİNDE VERİ EKLE/SİL/GÜNCELLE ###############################

#### VERİ EKLEME #####
###NOT : EĞER EKLEMEK İSTEDİĞİNİZ KEY DEĞERİ Sözlük içerisinde yoksa yeni bir key-value eşlemesi olarak eklenir ancak varsa var olan değer güncellenir.
# araba = {"VitesTürü":"Otomatik","KapıSayısı":2}
#
# araba["Renk"] = "Kırmızı"
#
# print(araba)
#
#
# araba["KapıSayısı"] = "4"
#
# print(araba)
#
# araba[2025] = "ModelYılı"
#
# print(araba)
#
#
# #### Update() ile birden fazla eleman güncelleme
#
# araba.update({"VitesTürü":"Manuel","KapıSayısı":5})
#
# print(araba)


########## ELEMAN SİLME İŞLEMLERİ ##############

#ogrenci = {"Ad":"Tarık","Soyadı":"Hamarat","KarneOrtalaması":100 ,"DoğumYılı": 1997 }

####Del kullanırken dikkat edelim.Bellek üzerinden direkt olarak silme işlemi yapar
# del ogrenci["DoğumYılı"]
# del ogrenci
#
# print(ogrenci)
#
# print(ogrenci)

## POP İLE SİLME

# silinenKarneOrtalaması = ogrenci.pop("KarneOrtalaması")
#
# print(ogrenci)
# print(silinenKarneOrtalaması)
#
# ogrenci.clear()
#
# print(ogrenci)
#

##### DICTIONARY İÇ İÇE KULLANIMI #######
ogrenciler = {

    "Tarık":{"Vize":60,"Final":70},
    "Halit":{"Vize":80,"Final":100},
    "Deniz":{"Vize":30,"Final":100}

}

#print(ogrenciler["Tarık"]["Vize"])

for  isim , dersnotu in ogrenciler.items():
    print(f"{isim}:{dersnotu['Vize']}")



