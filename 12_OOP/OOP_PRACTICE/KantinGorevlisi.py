from Insan import Insan as insan

class KantinGorevlisi(insan):
    @property
    def UrunAdet(self):
        return self.__urunAdet

    @UrunAdet.setter
    def UrunAdet(self, value):
        self.__urunAdet = value





