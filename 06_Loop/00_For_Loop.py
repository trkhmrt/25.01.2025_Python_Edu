"""

Tekrar etmesi gereken , Tekrar sayısının başlangıç ve bitişi bulunan kod bloklarının çalıştırılması için kullanılır.


for i in range():

range(Başlangıç,Bitiş,Artış_Miktarı)

Eğer range içerisinde bu parametreler tanımlanmazsa yani range(20) şeklinde bırakılırsa;
- Default olarak -> Başlangıç_değeri = 0   Artış_Miktarı -> 1

"""

#Range ifadesinde hiçbir değer belirtilmezse başlangıç değeri 0 olur.Son değer hiçbir zaman dahil edilmez.
# for i in range(10):
#     print(i)
#

#Başlangıç değerini biz tanımlayabiliriz(Başlangıç,bitiş)
# for i in range(5,20):
#     print(i)


#range(Başlangıç,Bitiş,Artış_Miktarı)
# for i in range(5,20,2):
#     print(i)




#örnek-1  3 adımlı bir döngü tanımlayın.Her adımda sizden bir isim istesin.Girmiş olduğunuz isimleri aynı zamanda ekrana yazdırın.

# for i in range(3):
#     isim = input("isim giriniz")
#     print(isim)


#Sepetin toplam tutarı

# sepet_tutar = 0
# print(f"Sepet tutarı:{sepet_tutar}")
#
#
# adet = int(input("Kaç adet ürün sepete eklenecek"))
#
# #(başlangıç_bitiş_artışMiktarı)
#
# for i in range(adet):
#     sepet_tutar += int(input("ürün Fiyatı:"))
#     sepet_tutar = sepet_tutar + int(input("ürün Fiyatı:"))
#
# print(f"Sepet tutarı:{sepet_tutar}")
#

#Örnek-2   1-100 arası çift sayıları  ekrana yazdırın.

# for i in range(1,100):
#     if(i%2==0):
#         print("Çift",i)
#     else:
#         print("Tek",i)


#Başlangıç ve bitiş değerlerini ve artış miktarını kullanıcıdan alarak belirlediğiniz for döngüsünde  3'ün katları olan sayıları ekrana yazdırın.

start = int(input("Başlangıç değeri giriniz:"))
end = int(input("Bitiş değeri giriniz:"))
increament = int(input("Artış değeri giriniz:"))


if start > end:
    end , start = start , end

if increament < 0:
    increament *=-1

for i in range(start,end,increament):
    if i%3==0:
        print(i)








