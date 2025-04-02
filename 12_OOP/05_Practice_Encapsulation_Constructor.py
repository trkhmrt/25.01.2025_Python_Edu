###OGRENCI OTOMASYON####

"""
Ogrenci
isim
Soyisim
Telefon
Tc
NotOrtalaması
"""

class Ogrenci:
    isim = ""
    soyisim = ""
    telefon = ""
    __tc = None
    NotOrtalaması = 0

    def __init__(self,name,lastname,phone,avarage):
        self.isim = name
        self. soyisim = lastname
        self.telefon = phone
        self.NotOrtalaması = avarage


    def get_tc(self):
        return self.__tc

    def set_tc(self,id):
        if len(id)!=11:
            print("Hatalı TC")
        else:
            self.__tc = id

    #__str__ ile oluşturulan nesnenin istenilen özellikleri geri döndürülür.
    def __str__(self):
        return f"İsim : {self.isim} Soyisim : {self.soyisim} TC: {self.tc}"


#ogrenciler = []

ogrenci = Ogrenci("Tarık","Hamarat","05537696362",95)
ogrenci.set_tc("12345678901")
print(ogrenci.get_tc())

# ogrenci2 = Ogrenci("Deniz","ÖzErdoğan","05537696362","111111111",95)
# ogrenci3 = Ogrenci("Berna","Seren","05537696362","111111111",95)
#
# ogrenciler.append(ogrenci)
# ogrenciler.append(ogrenci2)
# ogrenciler.append(ogrenci3)
#
#
# for ogr in ogrenciler:
#     print(ogr)

