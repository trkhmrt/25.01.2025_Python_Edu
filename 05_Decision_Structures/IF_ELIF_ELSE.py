"""
IF-ELIF-ELSE

Kodlama esnasında belirlenmiş olan kurallara göre uygulamanın çalışma esnasında bu kurallardan herhangi birini doğrulaması durumunda uygulama akışını bu kurala uygun olacak şekilde yönlendirmesi.


if kontrol_edilecek_durum(koşul):
    Koşul sonucu true ise if içindeki kod bloğu çalışır.







Dikkat Edilmesi Gerekenler

1-Sadece 1 kez if ve 1 kez Else kullanılabilir.Elif ise istenildiği kadar kullanılabilir.

2-if Bloğu içerisinde herhangi bir koşul sağlanır ve çalıştırılırsa diğer koşulların hiçbirinin kontrolü yapılmaz ve uygulama akışında çalışmaya devam eder.

"""

# sayi = 10
#
# if sayi>11:
#     print("Bu sayı 11 den büyüktür.")
#

# yas = int(input("Yaş giriniz"))
#
#
# if yas>18:
#     print("Ehliyet alabilir")
# elif yas == 18:
#     print("Kişi yaşı 18'dir ehliyet alabilir.")
# elif yas == 90:
#     print("ehliyet almak için biraz geç kalmış gibisiniz.")
# else:
#     print("Kişi yaşı 18 den küçük olduğu için ehliyat alamaz.")
#
#
# print("Merhaba sorun yok")





#ÖRNEK-1 SAYI GİRİLDİĞİNDE HAFTANIN HANGİ GÜNÜNE DENK GELDİĞİNİ BELİRTEN IF_ELIF_ELSE BLOĞUNU YAZINIZ.

# sayi = int(input("Sayi girin ve günü öğrenin"))
#
# if sayi==1:
#     print("Pazartesi")
# elif sayi==2:
#     print("Salı")
# elif sayi==3:
#     print("çarşamba")
# elif sayi==4:
#     print("Perşembe")
# elif sayi==5:
#     print("Cuma")
# elif sayi==6:
#     print("Cumartesi")
# elif sayi==7:
#     print("Pazar")
# else:
#     print("1-7 arasında değer giriniz")


#21:04 MOLA BİTİŞ


#Girilen sayı negatif mi pozitif mi ? Bunu bulan uygulamayı yazınız.
#-12


# sayi = int(input("Kontrol edilecek sayıyı giriniz:"))
#
# if sayi>0:
#     print("Pozitif.")
# elif sayi<0:
#     print("Negatif.")
# else:
#     print("Sayı sıfıra eşittir.")



# Girilen sayı tek mi çift mi ? olduğunu bulan uygulamayı yazınız.

#sayi = int(input("Kontrol edilecek sayıyı giriniz:"))

# if sayi % 2 == 0:
#     print("Sayı çifttir")
# else:
#     print("Sayı tektir.")


# if sayi % 2 != 0:
#     print("Sayı tektir")
# else:
#     print("Sayı çifttir.")


# if not sayi % 2 == 0:             #not önündeki ifadenin mantıksal(True/False) olarak tersini al.
#     print("Sayı tektir")
# else:
#     print("Sayı çifttir.")



#sicaklik = int(input("Sıcaklığı giriniz"))


# if (sicaklik >10 or sicaklik == 10)T and T(sicaklik < 35 or sicaklik == 30):
#     print("Ilık")


#
# if sicaklik >= 10 and sicaklik <=35:
#     print("Ilık")
# elif sicaklik >= 36 and sicaklik <=70:
#     print("Sıcak")
# elif sicaklik >=71 and sicaklik <=100:
#     print("Aşırı Sıcak")


# if 10<=sicaklik<=35:
#     print("Ilık")
# elif 36<=sicaklik<=70:
#     print("Sıcak")
# elif 71<=sicaklik<=100:
#     print("Aşırı Sıcak")


# a , b , c = 10 , 20 , 30
#
# print(a)
# print(b)
# print(c)


"""
Öğrenci otomasyonu
0-44 arası kaldı
45-70 arası geçti
71-84 teşekkürle
85-100 takdir 

buradaki aralık dışında girilen sayılar kabul edilmeyecektir.
hatalı not girdiniz diye uyarı verilsin.
"""

ders_notu = int(input("Not giriniz:"))


if 0<=ders_notu<=44:
    print("Kaldınz")
elif 45<=ders_notu<=70:
    print("Geçti")
elif 71<=ders_notu<=84:
    print("Teşekkürle geçti")
elif 85<=ders_notu<=100:
    print("Takdirle geçti")
else:
    print("0-100 arası değer giriniz.")




