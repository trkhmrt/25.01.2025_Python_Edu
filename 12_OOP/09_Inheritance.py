"""
INHERITANCE(MIRAS ALMA)
Bir sınıfın başka bir sınfın özelliklerini miras alması ve kendi içerisinde kullanmasıdır.
Elimizde birden fazla class varsa ve bu classlar içerisinde aynı özellikler tekrar ediyorsa bu özellikleri tek ve üst bir classta toplarız.Ardından bu classların miras almasını sağlarız
"""

class Insan:
    İsim = ""
    Soyisim = ""
    DogumTarihi = ""
    DogumYeri = ""



class Ogrenci(Insan):
    NotOrtalaması = ""
    AldıgıDersler = []
    SinifSubesi  = ""


class Ogretmen(Insan):
    VerdigiDersSayisi = 0
    MezuniyetUni = ""


class Mudur(Insan):
    ToplantiSayisi = 0


ogrenci = Ogrenci()
ogrenci.İsim = "Tarık"
ogrenci.Soyisim = "Hamarat"
ogrenci.NotOrtalaması = "70"


print(ogrenci.İsim , ogrenci.Soyisim , ogrenci.NotOrtalaması)

print("")