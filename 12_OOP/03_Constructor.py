"""
Constructor Metot

Yapıcı metotdur

Class üzerinde nesne oluşturulduğunda ilk çalışacak metottur.
Bu yüzden en hızlı çalışan metot olarak isimlendirilir.

"""


# class Araba:
#     def __init__(self,color,motorGucu):
#         self.renk = color
#         self.motorGucu = motorGucu
#         print("Ben constructor metodum.Nesne üretildiğinde çalışırım.")
#         print(f"{self.arabaOzelliginiYazdir()} constructorla birlikte bu özellikler gönderildi.")
#
#     def arabaOzelliginiYazdir(self):
#         print(self.renk,self.motorGucu)
#

#
# araba = Araba("Kırmızı","400HP")
# araba2 = Araba("Mavi","500HP")

"""
__str__ ile oluşturulan nesnenin istenilen özellikleri geri döndürülür.
"""
class Araba:
    def __init__(self, color, hp):
        self.renk = color
        self.motorGucu = hp
        self.kapiSayisi = 2

    def __str__(self):
        return f"Renk:{self.renk} motorGucu:{self.motorGucu}"



araba = Araba("Kırmızı","100")


print(araba)







