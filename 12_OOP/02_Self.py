"""
SELF
Bir class'ın içindeki özelliklere ve metotlara erişmek için kullanılan bir referanstır.
O an üretilen nesnenin kendisini temsil eder.
"""

class Araba:
    renk = ""
    motorGucu = ""
    def arabaOzelliginiYazdir(self,motorGucu):
        self.motorGucu = motorGucu
        print(self.renk,self.motorGucu)




araba = Araba()
araba.renk = "Mavi"

araba.arabaOzelliginiYazdir("300HP")









