class Insan:
    @property
    def Isim(self):
        return self.__isim

    @Isim.setter
    def Isim(self, value):
        self.__isim = value

    @property
    def SoyIsim(self):
        return self.__soyIsim

    @SoyIsim.setter
    def SoyIsim(self, value):
        self.__soyIsim = value

    @property
    def DogumTarihi(self):
        return self.__dogumTarihi

    @DogumTarihi.setter
    def DogumTarihi(self, value):
        self.__dogumTarihi = value

def sayHello():
    pass
