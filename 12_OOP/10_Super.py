"""
Classlar içerisinde tekrar eden kod yapısı varsa bu kod bloğu base class içerisinde metota çevirilir ardından diğer classlar içerisinde süper ile kullanılır.
"""
class Insan:
    #Base Class
    Isim = ""
    Soyisim = ""
    DogumTarihi = ""
    DogumYeri = ""

    def bilgiler(self):
        print(f"isim:{self.Isim} Soyisim:{self.Soyisim} {self.DogumTarihi} {self.DogumYeri}")



class Ogrenci(Insan):
    NotOrtalaması = ""
    AldıgıDersler = ["Matematik","Türkçe"]
    SinifSubesi  = ""

    def bilgiler(self):
        super().bilgiler()
        print(f"{self.NotOrtalaması} "
              f"{self.SinifSubesi} "
              f"{self.AldıgıDersler} " )


class Ogretmen(Insan):
    VerdigiDersSayisi = 0
    MezuniyetUni = ""

    def bilgiler(self):
        super().bilgiler()
        print(f"{self.MezuniyetUni} "
              f"{self.VerdigiDersSayisi} " )




class Mudur(Insan):
    ToplantiSayisi = 0

    def bilgiler(self):
        print(f"{self.ToplantiSayisi}")





ogrenci = Ogrenci()
ogrenci.Isim = "Tarık"
ogrenci.Soyisim = "Hamarat"
ogrenci.DogumTarihi = "01.11.1997"
ogrenci.DogumYeri = "Kars"
ogrenci.NotOrtalaması = "70"
ogrenci.SinifSubesi = "A"


ogrenci.bilgiler()

ogretmen = Ogretmen()
ogretmen.Isim = "Halit"
ogretmen.Soyisim = "Özer"
ogretmen.DogumTarihi = "01.11.1994"
ogrenci.DogumYeri = "Ardahan"
ogretmen.MezuniyetUni = "ITU"
ogretmen.VerdigiDersSayisi = 3

ogretmen.bilgiler()





print("")