from Insan import Insan as insan

class Ogretmen(insan):
    @property
    def VerdigiDersSayisi(self):
        return self.__verdigiDersSayisi

    @VerdigiDersSayisi.setter
    def VerdigiDersSayisi(self,value):
        self.__verdigiDersSayisi = value

    @property
    def OgrenciSayisi(self):
        return self.__ogrenciSayisi

    @OgrenciSayisi.setter
    def OgrenciSayisi(self,value):
        self.__ogrenciSayisi = value




