from Insan import Insan as insan
class Ogrenci(insan):
    @property
    def NotOrtalamasi(self):
        return self.__notOrt

    @NotOrtalamasi.setter
    def NotOrtalamasi(self,value):
        self.__notOrt = value

    @property
    def Sinif(self):
        return self.__sinif

    @Sinif.setter
    def Sinif(self,value):
        self.__sinif = value

    @property
    def SinifSube(self):
        return self.__sinifSube

    @SinifSube.setter
    def SinifSube(self, value):
        self.__sinifSube = value

    def __str__(self):
        return f"İsim:{self.Isim} Soyisim:{self.SoyIsim} DoğumTarihi:{self.DogumTarihi} NotOrtalaması:{self.NotOrtalamasi}"

