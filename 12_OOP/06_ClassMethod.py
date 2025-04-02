"""
ClassMethod

cls

"""

class Sınıf:
    sini_mevcudu = 10
    ogrenci_isim = ""
    @classmethod
    def sinifMevcudunuGuncelle(cls,sinifMevcudu):
        cls.sini_mevcudu = sinifMevcudu

    def OrtalamaHesapla(self,notlarToplami,name):
        self.ogrenci_isim = name
        print(self.ogrenci_isim)
        return notlarToplami/self.sini_mevcudu






sinif = Sınıf()
sinif2 = Sınıf()

response = sinif.OrtalamaHesapla(700,"Tarık")
response2 = sinif2.OrtalamaHesapla(600,"Deniz")

print(response)
print(response2)


Sınıf.sinifMevcudunuGuncelle(8)


response = sinif.OrtalamaHesapla(700,"Tarık")
response2 = sinif2.OrtalamaHesapla(600,"Deniz")


print(response)
print(response2)









