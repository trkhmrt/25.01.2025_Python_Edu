"""
Try-Except
Hata yakalama için kullanılan kod bloğudur.
Farklı hata tiplerinde uygulamanın çökmesi söz konusu olabilir.Bunun önüne geçmek ve hataların detaylarını daha net görebilmek için bu kod bloğundan faydalanırız.

try:
    Hata alma ve uygulamayı çökertme potansiyeline sahip kodlar try içerisinde çalıştırılır.
except:
    Hata meydana geldiğinde çalıştırılacak kodlar burada yer alır.

HataTürleri

ZeroDivisionError => Bir sayıyı sıfıra bölerken bu hata alınır.

IndexError => Listelerde geçersiz indeks numarası kullanıldığında bu hata alınır.

ValueError => Talep edilen veri tipiyle yada dönüştürülmek istenen veri tipiyle okunan verinin uyumsuz olduğu durumlarda bu hata döndürülür.

TypeError => Birbiriyle uyumsuz veri tiplerinin işleme sokulması sonucu alınır.

ModuleNotFoundError => dahil edilmek istenen modül bulunmuyorsa bu hata alınır.

FileNotFounderror => Dosya bulunamadığında oluşur.

SyntaxError => Python aid kodların söz diziminde hata yapıldığında alınır

IndentationError => if , def , while , try gibi indentation kuralına uyulması gereken yerlrde uyulmadığında bu hata alınır.

"""

####### ZeroDivisionError #######
# sayi1 = 10
# sayi2 = 0
#
# print(sayi1/sayi2)
# print("Merhaba")

# try:
#     sayi1 = 10
#     sayi2 = 0
#     print(sayi1 / sayi2)
#     print("Merhaba")
# except:
#     print("Sıfıra bölünme hatası")


######## IndexError #########

# list = [10,20]
# print(list[10])
# try:
#     print(list[10])
# except:
#     print("Hata meydana geldi")
#
# print("Başarılı şekilde sonlandırıldı.")


######## ValueError #########
# try:
#     sayi = int(input("Bir sayı giriniz"))
# except:
#     print("Hata meydana geldi")



####### TYPE ERROR ########
#sayi = 10
#isim = "Tarık"
#
#sonuc = sayi + isim



######## ModuleNotFoundError  ######
#import trk

# try:
#     import trk
# except:
#     print("Hata meydana geldi")


##### FileNotFoundError ######
#dosya = open("1.txt","r",encoding="utf-8")
# dosya_icerigi = dosya.readlines()
# print(dosya_icerigi)
# try:
#     dosya = open("olmayan_dosya.txt","r")
# except:
#     print("Bir hata meydana geldi")



#
# ###### Exception as e ile hata mesajı içeriğini görüntüleme #######
# try:
#     sayi1 = 10
#     sayi2 = 0
#     print(sayi1 / sayi2)
#     list = []
#     print(list[0])
# except Exception as e:
#     print("Hata meydana geldi.",e)



###### HATA TÜRLERİNİ AYRI EXCEPTIONLARDA ELE ALMA ##########
# try:
#     sayi1 = 10
#     sayi2 = 0
#     print(sayi1 / sayi2)
#     list = []
#     print(list[0])
# except ZeroDivisionError:
#     print("Bölen Sayı sıfır olamaz...")
# except IndexError:
#     print("Lütfen dizi sınırları içerisinde index numarası veriniz.")


####### FINALLY BLOĞU (Uygulamada hata alınsada alınmasada finally çalışır.) #######
# try:
#     list = []
#     #print(list[0])
#     print("Herhangi bir hata meydana gelmedi")
# except:
#     print("Hata meydana geldi")
# finally:
#     print("Hatalı hatasız her türlü ben çalışırım.")


######## SyntaxError   #####
#print(



######## IndentationError  ########
 # if True:
 #  print("Merhaba")


####### KEYERROR => Sözlükte olmayan bir anahtar çağrıldığında hata verir ######
#
# sozluk = {"ad":"Tarık"}
# print(sozluk["yas"])


###### ATTRIBUTEERROR => olmayan bir metodu veya özelliği çağırmaya çalıştığımızda ######
# yas = 100
# print(yas.count("0"))

######## NAME_ERROR => Tanımlanmamış Değişken kullanıldığında  #######
#print(x)  #x herhangi bir yerde tanımlı değil




######## RAISE İLE BİRLİKTE KENDİ HATALARIMIZI FIRLATMA #######




# try:
#     yas = 17
#     if yas < 18:
#         raise ValueError("Yaş 18 den küçük")
# except ValueError as e:
#     print(e)










