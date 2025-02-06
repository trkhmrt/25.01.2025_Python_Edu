"""
Değişkenler

Değişken Nedir ?

Uygulama içerisinde açığa çıkan ve saklanmak istenen verilere verilen isim.




Veri Tipi

Metinsel Veri Tipleri

Char(Tek bir karakter tutar) - String(Birden fazla karakterin bir araya gelmesiyle oluşturulan metinsel dizi)

'a'  - "abcd"

Sayısal Veri Tipleri


Integer (int)
    - tam sayı ifadeleri temsil eden veri tipidir.    -2450  /  2450

Float (flt)
    - ondalıklı sayıları temsil eder.    75.7 kg / 1.85 cm

Mantıksal Veri Tipleri

Boolean (bool)
    - True(1) , False(0)


Debug Modu
 - Uygulamanın akışının takibi yada herhangi bir hatanın sebebini bulabilmek için debug moduyla çalıştırıp her bir satırın davranışını inceleriz.

Breakpoint
 - Uygulamanın gözlenmek istenilen satırına bırakılır ve uygulama bu noktada durur.Bunu kırılım noktasıda denilebilir.Hata ayıklama için kullanılır.

    !!! Breakpoint noktasında durması için uygulamanın debugger(Böcek simgesi) moduyla çalıştırılması gerekir


type()
 - type ile birlikte değişkenlerin veri tipini öğrenebilirsiniz.


"""

#Kişisel Bilgilerimi Değişken Kullanarak Tanımlıyorum

isim = "Tarık"
soyisim = "Hamarat"
kilo = 73
boy = 1.85
emeklilik = False

# print(type(isim))
# print(type(soyisim)) # String
# print(type(kilo)) # Int
# print(type(boy)) # float
# print(type(emeklilik)) #bool


#print ile birlikte değişkenleri yazdırma

#print(isim)

#print(isim,soyisim,kilo,boy,emeklilik)

#print("İsim:",isim,"Soyisim:",soyisim,"Kilo:",kilo,"Boy:",boy,"Emeklilik Var mı?:",emeklilik)

#Değişken sayısı fazla olduğu durumlarda daha pratik bir yazım yöntemi olarak kullanılabilir.
#Virgül ve tırnak kullanılmadığında daha pratik bir yöntem sunuyor.

#print içinde f(format) kullanarak verileri yazdırma
#print(f"İsim:{isim} Soyisim:{soyisim} Kilo:{kilo} Boy:{boy} Emeklilik:{emeklilik}")


#Kaçış ifadeleriyle print içerisinde mesaj yazdırma
#Escape state
# \n (new line)

#print(f"İsim:{isim}\nSoyisim:{soyisim}\nKilo:{kilo}\nBoy:{boy}\nEmeklilik:{emeklilik}")

#print(f"İsim:{isim}\nSoyisim:{soyisim}\nKilo:{kilo}\nBoy:{boy}\nEmeklilik:{emeklilik}")

# end -> Satır sonunda hangi ifadenin yer alacağını belirtir.
# print("Selam") #Varsayılan olarak print içerisindeki mesajın en sağında \n ifadesi bulunur.
# print("Selam",end="\n") #Burada satırın sonunda hangi ifadenin olacağını değiştirebiliriz.
# print("Merhaba Dünya")#

#sep ->

#print("Tarık","Hoca","Dersi","Bitirecek",sep=",",end=".")


#
# # /t tab(Space tuşuna 3 kez basılmış gibi boşlu bırakır. 3 space = 1 Tab tuşu)
# print("Selam Merhaba\tBiz Eğitimdeyiz.")
# print("Tarık\tHamarat\tBiz Eğitimdeyiz.")
# print("Tarık\tHamarat\tBiz Eğitimdeyiz.")


# print içerisinde 3 tırnak ile birlikte çıktı verme
# print("Tarık "
#       "Hamarat "
#       "Comp Eng")
#
#
# print("""
#     Tarık
#             Hamarat
#     Comp Eng
# """)
#
# print('''
#     Tarık
#             Hamarat
#     Comp Eng
# ''')


































