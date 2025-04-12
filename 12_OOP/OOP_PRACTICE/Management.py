from Ogrenci import Ogrenci
from Ogretmen import Ogretmen
from KantinGorevlisi import KantinGorevlisi
from SeedData import *


ogrenciler = []
ogrenciler.append(OgrenciOlustur())
ogretmenler = []
ogretmenler.append(OgretmentOlustur())
kantinGorevlileri = []


def Listeleme(parametreListe):
    for idx, itm in enumerate(parametreListe):
        print(f"{idx}-{itm}")


def ListedenSil(parametreListe,idx):
    if len(parametreListe) == 0:
        return "Listede Eleman Yok"
    else:
        parametreListe.pop(idx)
        return "Eleman Başarıyla Silindi."


while(True):
    secim = int(input("1-Ekleme İşlemleri\n2-Silme İşlemleri\n3-Listeleme İşlemleri\n4-Çıkış"))
    if secim == 1:
        eklemeSecim = int(input("1-Öğrenci Ekleme İşlemleri\n2-Öğretmen Ekleme İşlemleri\n3-KantinGörevlisi Ekleme İşlemleri"))
        if eklemeSecim == 1:
            ogrenci = Ogrenci()
            ogrenci.Isim = input("İsim giriniz:")
            ogrenci.SoyIsim = input("Soyisim giriniz:")
            ogrenci.DogumTarihi = input("Doğum Tarihi:")
            ogrenci.Sinif = input("Sınıf Bilgisi:")
            ogrenci.SinifSube = input("Şube:")
            ogrenci.NotOrtalamasi = input("Not Ortalaması:")
            ogrenciler.append(ogrenci)
        elif eklemeSecim == 2:
            ogretmen = Ogretmen()
            ogretmen.Isim = input("İsim:")
            ogretmen.SoyIsim = input("Soyisim")
            ogretmen.DogumTarihi = input("Doğum Tarihi:")
            ogretmen.VerdigiDersSayisi = input("Sahip olunan ders sayisi:")
            ogretmen.OgrenciSayisi = input("Sahip olunan öğrenci sayisi:")
            ogretmenler.append(ogretmen)
        elif eklemeSecim == 3:
            pass
    elif secim == 2:
        silmeSecim = int(input("1-Öğrenci Silme İşlemleri\n2-Öğretmen Silme İşlemleri\n3-KantinGörevlisi Silme İşlemleri"))
        if silmeSecim == 1:
            Listeleme(ogrenciler)
            silinecekIndex = int(input("Index değeri girin:"))
            print(ListedenSil(ogrenciler,silinecekIndex))
        elif silmeSecim == 2:
            Listeleme(ogretmenler)
            silinecekIndex = int(input("Index değeri girin:"))
            print(ListedenSil(ogretmenler, silinecekIndex))
        elif silmeSecim == 3:
            Listeleme(kantinGorevlileri)
            print(ListedenSil(kantinGorevlileri, silinecekIndex))

    elif secim == 3:
        pass
    elif secim == 4:
        break