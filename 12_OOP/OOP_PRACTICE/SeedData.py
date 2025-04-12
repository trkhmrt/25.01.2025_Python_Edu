from Ogrenci import Ogrenci
from Ogretmen import Ogretmen
from KantinGorevlisi import KantinGorevlisi


def OgrenciOlustur():
    ogrenci = Ogrenci()
    ogrenci.Isim = "Tarık"
    ogrenci.SoyIsim = "Hamarat"
    ogrenci.DogumTarihi = "01/11/1997"
    ogrenci.Sinif = "5"
    ogrenci.SinifSube = "A"
    ogrenci.NotOrtalamasi = "100"

    return ogrenci


def OgretmentOlustur():
    ogretmen = Ogretmen()
    ogretmen.Isim = "Halit"
    ogretmen.SoyIsim = "Özer"
    ogretmen.VerdigiDersSayisi = "10"
    ogretmen.OgrenciSayisi = "100"
    ogretmen.DogumTarihi = "01/11/1994"

    return ogretmen