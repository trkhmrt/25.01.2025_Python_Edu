class Insan:
    @property
    def isimDegeri(self):
        return self.__isim

    @isimDegeri.setter
    def isimDegeri(self,value):
        self.__isim = value


insan = Insan()
insan.isimDegeri = "Tarık"

print(insan.isimDegeri)

print("")





