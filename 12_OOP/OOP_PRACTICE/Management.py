from Ogrenci import Ogrenci
from Ogretmen import Ogretmen
from KantinGorevlisi import KantinGorevlisi

ogrenciler = []
ogretmenler = []
kantinGorevlileri = []



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
            for idx,itm in enumerate(ogrenciler):
                print(f"{idx}-{itm}")
        elif silmeSecim == 2:
            pass
        elif silmeSecim == 3:
            pass

    elif secim == 3:
        pass
    elif secim == 4:
        break