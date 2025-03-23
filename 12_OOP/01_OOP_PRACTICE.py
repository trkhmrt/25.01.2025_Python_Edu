"""
ÖĞRENCİ KAYIT OTOMASYONU
"""
import os
import random

class Ogrenci:
    isim = ""
    soyisim = ""
    yas = ""
    sehir = ""
    notOrtalaması = 0


ogrenciListesi=[]

ogrenciIsimler = ["Tarık","Berna","Deniz","Sercan","Yusuf","Halit","Ozan","Yasemin","Furkan","Berfin","Burak","Yağız"]
ogrenciSoyisimler = ["Çalışkan","Yetenekli","Başarılı","Zeki","Çevik","Saygılı","Güneş","Ay","Tar","Öz","Eminoğlu","Ali"]
ogrenciYaslar = ["30","25","13","40","50","20","18","29","40","55","10","20"]
ogrenciSehir = ["İstanbul","Ankara","İzmir","Muğla","Antalya","Balıkesir","Eskişehir","Samsun","Kars","Edirne","Sivas","Iğdır"]
ogrenciLiseNotOrtlaması = [100,70,80,74,56,88,65,92,81,72,63,52]



def RastgeleOgrenciUret():
    for i in range(5):
        rastgeleIsimIndex = random.randint(0, len(ogrenciIsimler) - 1)
        rastgeleSoyisimIndex = random.randint(0, len(ogrenciSoyisimler) - 1)
        rastgeleYasIndex = random.randint(0, len(ogrenciYaslar) - 1)
        rastgeleNotIndex = random.randint(0, len(ogrenciYaslar) - 1)
        rastgeleSehirIndex = random.randint(0, len(ogrenciYaslar) - 1)

        yeniOgrenci = Ogrenci()
        yeniOgrenci.isim = ogrenciIsimler[rastgeleIsimIndex]
        yeniOgrenci.soyisim = ogrenciSoyisimler[rastgeleSoyisimIndex]
        yeniOgrenci.notOrtalaması = ogrenciLiseNotOrtlaması[rastgeleNotIndex]
        yeniOgrenci.sehir = ogrenciSehir[rastgeleSehirIndex]
        yeniOgrenci.yas = ogrenciYaslar[rastgeleYasIndex]
        ogrenciListesi.append(yeniOgrenci)


def OgrenciKayit(isim,soyisim,notOrtalaması,sehir,yas):
    yeniKayit = Ogrenci()
    yeniKayit.isim = isim
    yeniKayit.soyisim = soyisim
    yeniKayit.notOrtalaması = notOrtalaması
    yeniKayit.sehir = sehir
    yeniKayit.yas = yas
    ogrenciListesi.append(yeniKayit)

def OgrenciSil(index):
    bulunanOgrenci = OgrenciBul(index)
    ogrenciListesi.remove(bulunanOgrenci)
    return "Öğrenci Silindi"

def OgrenciGuncelle(index):
    bulunanOgrenci = OgrenciBul(index)
    bulunanOgrenci.sehir = input("Yeni şehir bilgisini giriniz")
    return "Öğrenci GÜncellendi"

def OgrenciBul(ogrenciIndex):
    for index,ogrenci in enumerate(ogrenciListesi):
        if index == ogrenciIndex:
            return ogrenci

def OgrenciDetayBilgi(ogrenciIndex):
    for index, ogrenci in enumerate(ogrenciListesi):
        if index == ogrenciIndex:
         print(f"{index}-İsim:{ogrenci.isim}-Soyisim:{ogrenci.soyisim}-Sehir:{ogrenci.sehir}-NorOrt:{ogrenci.notOrtalaması}-Yas:{ogrenci.yas}")

def OgrenciListele():
    for index,ogrenci in enumerate(ogrenciListesi):
        print(f"{index}-{ogrenci.isim}-{ogrenci.soyisim}")


RastgeleOgrenciUret()

while True:
    secim = int(input("Seçim yapınız\n1-Öğrenci Kayıt\n2-Öğrenci Sil\n3-Öğrenci Bilgi Güncelleme\n4-Öğrenci Detay\n5-Çıkış"))
    if secim == 1:
        print("----------ÖĞRENCİ KAYIT EKRANI----------")
        from_user_isim = input("İsim:")
        from_user_soyisim = input("Soy_İsim:")
        from_user_not_ortalamasi = input("Not_Ortalaması(Lise):")
        from_user_sehir = input("Şehir:")
        from_user_yas = input("Yaş:")
        OgrenciKayit(from_user_isim,from_user_soyisim,from_user_not_ortalamasi,from_user_sehir,from_user_yas)

    elif secim == 2:

        OgrenciListele()
        silinecekIndex = int(input("Silinecek Öğrenci Indeksi:"))
        response = OgrenciSil(silinecekIndex)
        print(response)

    elif secim == 3:
        OgrenciListele()
        guncellenecekIndex = int(input("Güncellenecek Öğrenci Indeksi:"))
        response = OgrenciGuncelle(guncellenecekIndex)
        print(response)

    elif secim == 4:
        OgrenciListele()
        detayIndex = int(input("DetayLı bilgi talep edilen Öğrenci Indeksi:"))
        OgrenciDetayBilgi(detayIndex)
    elif secim == 5:
        break