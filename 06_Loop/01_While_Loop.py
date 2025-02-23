"""
While Loop

while kosul:
    Koşul true dönerse belirtilen kodlar burada çalışacak.


"""
from contextlib import nullcontext

# sayi = 11 #Başlangıç değeri
#
# while sayi<30:   # for i in range(11,30,1)
#     print("Merhaba Dünya")
#     sayi+=1



#Başlangıç ve bitiş değerlerini kullanıcıdan aldığınız bir while döngüsü tasarlayın.Artış miktarı tercihinize kalmış.
#
# start = int(input("Başlangıç değeri giriniz:"))
# end = int(input("Bitiş değerini giriniz:"))
#
# while start<end:
#     print(start)
#     start+=1
#


# Şifreyi doğru girebilmesi için 3 hakkı bulunacak.
#Kullanıcnın sifre = .... şeklinde bir değişkeni olsun
#Kullanıcıdan her seferinde şifre girmesini isteyip tanımlanan değişkenle eşitliği kontrol edilsin.
# Her yanlışta hak azaltılacak.
#  Hakkı kalmadığında döngüden hakkınız bitmiştir diyip çıkartılacak.
#  Doğru bilirse Şifre kabul edildi mesajı ekranı bastırılacak ve döngüden çıkarılacak(Bunun için bir komut var anlatacağım.)


# sifre = "t"
# hak = 3
#
#
# while hak>0:
#     entry = input("Şifreyi giriniz:")
#     if entry == sifre:
#         break
#     else:
#         hak-=1
#         print(f"Kalan Hak:{hak}")
#         if hak==0:
#             print("Hakkınız bitmiştir.")
#
# print("Merhaba")

# sayi = ("1")
#
# print(sayi.isdigit())

#Sadece rakamsal ifade giriline kadar kullanıcıdan veri girmesi istensin girilen verinin karesi alınsın.



#
# while True:
#     veri = input("Değer giriniz")
#     if veri.isdigit():
#         print(int(veri) ** 2)
#         break
#     else:
#         print("Lütfen sadece sayısal veri girin.")



#Continue
# i=0
#
# while i<5:
#     if i % 2 == 0:
#         i+=1
#         continue
#     else:
#         print(i)
#         i += 1
#     print("Merhaba")

#Kullanıcıdan sayılar alalım ve bunları herseferinde toplayalım.
#ANCAK sayıların toplanma şartı 3ün katı olmaları olacak.
#girilen sayı 3ün katı değilse kullanıcıdan tekrardan veri girmesi istenecek.Girilen veri sayısı 3 e ulaştığında döngüden toplamı elde edip çıkılsın.


toplam = 0
girilen_sayi_adedi=0

while True:

    if girilen_sayi_adedi==3:
        print(f"Sayıların toplamı:{toplam}")
        break

    sayi = int(input("Lütfen 3ün katı bir sayı giriniz"))

    if sayi%3 != 0:
        continue

    toplam += sayi

    girilen_sayi_adedi +=1



















