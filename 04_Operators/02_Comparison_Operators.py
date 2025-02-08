
"""
 Aynı veri tipindeki değerlerin karşılaştırılması için kullanılır.

 Bu karışılaştırma sonucunda Geriye True yada False olmak üzere sadece iki cevap dönebilir.

 == ->  Veri tipi ve içinde taşıdığı değer eş mi bakar.

 != -> birbirlerine eşit değiller demektir.

 >  Büyüktür

 <   Küçüktür

 >= büyük veya eşittir.

 <= küçük veya eşittir.

"""
from six import print_

# x = 10
# y = 30
#
#
# print(x==y) # False
# print(x!=y) # True
# print(x>y) #  False
# print(x<y) #  True
# print(x>=y) #  False
# print(x<=y) #  True



#python dili case sensitive (Büyük küçük harf duyarlılığı vardır.)

# isim = "TarıK"
# isim2 = "Tarık"
#
# print(isim==isim2)


#lower()

isim = "TarıK"
isim2 = "Tarık"

isim = isim.lower()
isim2 = isim2.lower()


print(isim==isim2)
