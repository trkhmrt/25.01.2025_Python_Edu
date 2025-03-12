"""
Fonksiyonlar

herhangi bir kod bloğu bir yerde birden fazla kez yazılmışsa burada bir sorun var demektir.Biz yazdığımız kodları olabildiğince sade tutmaya çalışırız.Aynı kod satırlarını tekrar etmek istemeyiz.
Çünkü bu kodun okunabilirliğini düşürür.

fonksiyon nasıl tanımlanır.

def fonksiyon_adi():
    fonksiyon çağrılırsa buradaki kodlar çalıştırılacak.


Metotlar Çağrıldıklarında tanımlandıkları yere giderler.Orada çalıştıktan sonra ise çağrıldıkları yere geri dönerler.

Metotlar çağrılmadan çalışmazlar.


METOT TÜRLERİ

1-Geri değer döndüren  ve Geri değer döndürmeyen

Geri değer döndürmeyen => metot çalışır bütün işleri kendi içinde halleder dışarı bir vefri paylaşmaz.
    -  Parametreli
    - Parametresiz
Geri değer döndüren => bu metot türleri istenilen veri tipindeki veriyi çağrıldığı yere taşır.Bunu return keywordu ile yapar.
    -  Parametreli
    -  Parametresiz


"""
####### PARAMETRESİZ METOT #########
print("")
def ekranaMesajYaz():
    print(f"Merhaba Tarık")
    print("Sisteme Hoşgeldiniz")
    print("Bakiyeniz")


# print(f"Merhaba Tarık")
# print("Sisteme Hoşgeldiniz")
# print("Bakiyeniz")
#
#
# print(f"Merhaba Tarık")
# print("Sisteme Hoşgeldiniz")
# print("Bakiyeniz")
#
#
# print(f"Merhaba Tarık")
# print("Sisteme Hoşgeldiniz")
# print("Bakiyeniz")
#
#
# print(f"Merhaba Tarık")
# print("Sisteme Hoşgeldiniz")
# print("Bakiyeniz")

ekranaMesajYaz()
ekranaMesajYaz()
ekranaMesajYaz()
ekranaMesajYaz()


# for i in range(3):
#     ekranaMesajYaz()


####### PARAMETRELİ METOT #######

# def ekranaMesajYaz(isim):
#     print(f"Merhaba {isim}")
#     print("Sisteme Hoşgeldiniz")
#     print("Bakiyeniz")
#
#
#
#
# ekranaMesajYaz("Tarık")
# ekranaMesajYaz("Yusuf")
# ekranaMesajYaz("Ozan")
# ekranaMesajYaz("Sercan")
#



##### GERİ DEĞER DÖNDÜRMEYEN ######
# return kullanmadan metodun kendisini yazdırmak istediğimizde none denen bir hata aldık.
# def sayilariTopla(s1,s2):
#     print(s1+s2)
#
#
# print(sayilariTopla(10,20))


##### GERİ DEĞER DÖNDÜREN METOT #######

# def sayilariTopla(s1,s2):
#     return s1+s2
#
# veri = sayilariTopla(10,20)
#
#
# print(veri)



#### RETURN İFADESİ METOTLARDA BİR ANLAMDA BREAK GİBİ İŞLEV GÖRÜR #######

##Return ifadesiyle karşılaşan metot returnun önündeki değeri çağrıldığı yere taşır bir nevi break gibi çalışır.
# def sayilariTopla(s1,s2):
#     return s1+s2
#     print("Merhaba Dünya")
#
# veri = sayilariTopla(10,20)
#
#
# print(veri)





####### TRY EXCEPT YAPISI İLE METOTLARIN KULLANIMI


# def bolmeIslemi():
#     print(10/0)
#
#
# try:
#     bolmeIslemi()
#     print("Merhaba")
# except:
#     print("Hata meydana geldi.")


# def indexHataMetot():
#     list=[]
#     print(list[10])
#
#
# def bolmeIslemi():
#     print(10/2)
#     indexHataMetot()
#
#
#
#
# try:
#     bolmeIslemi()
#     print("Merhaba")
# except ZeroDivisionError:
#     print("Sıfıra bölünme hatası.")
# except IndexError:
#     print("Liste index aralığı dışında değer.")




#### ÖRNEK #####
"""
Kullanıcıdan 3 adet veri alınız;
1-İsim
2-Yaş
3-Hobiler

Bunları metot metot içerisinde  İsimli kişinin yaşı şudur ve hobileride bunlardır şeklinde string  bir mesaj oluşturun ardından bunu geri döndürün
"""

# def bilgileriYaz(name,age,hobbies):
#     return f"{name} kişisinin yaşı {age}.Hobileri {hobbies}"
#
#
#
# isim = input("İsim giriniz")
#
# yas = input("Yaş giriniz")
#
# hobiler = [input("1.Hobi giriniz"),input("2.Hobi giriniz"),input("3.Hobi giriniz")]
#
#
# print(bilgileriYaz(isim,yas,hobiler))







