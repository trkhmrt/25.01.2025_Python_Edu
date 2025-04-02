"""
Encapsulation Nedir ?

Bir sınıf içindeki verileri veya metotları dışarıdan doğrudan erişime kapatmak ve kontrollü erişim sağlamak için kullanılan bir OOP prensibidir.

Veri saklanır dış müdahelelerden korunur.

Doğrudan erişim kapatılır.İzin verilen metotlarla değiştirilebilir.

Kodu düzenli , bakımı kolay ve güvenli hale getirir.

"""

"""
_ (alt çizgi) ifadesi ile değişken ismi gizlenir.

__(iki alt çizgi) private yapar.Tamamen gizler.
"""
"""
@Getter
@Setter
"""


class Araba:
    _marka = ""
    __renk = ""

    def get_renk(self):
        return self.__renk

    def set_renk(self,color):
        if len(color)>2:
            self.__renk = color



araba = Araba()
#araba._marka = ""
#araba._marka = "BMW"

araba.set_renk("Kırmızı")
print(araba.get_renk())

