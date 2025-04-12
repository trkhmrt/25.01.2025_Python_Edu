from Insan import Insan as insan

class KantinGorevlisi(insan):
    @property
    def UrunAdet(self):
        return self.__urunAdet

    @UrunAdet.setter
    def UrunAdet(self, value):
        self.__urunAdet = value


    def __str__(self):
        return f"{super().__str__()} UrunAdet:{self.UrunAdet}"




