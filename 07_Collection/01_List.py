"""
List

İçinde farklı veri tiplerine ait veriler barındıran koleksiyon yapılarıdır.

isimler = []


Listelerde index mantığı geçerlidir.

ilk eleman indeks numarası 0 dır.

"""

# isimler = ["Tarık"]

#print(type(isimler)) #isimlerin bir liste olduğunu ispatladık.

# print(isimler[0])
# print(isimler[1])
# print(isimler[2])
# print(isimler[3])
# print(isimler[4])
# print(isimler[5])
# print(isimler[6])
# print(isimler[7])
# print(isimler[8])
# print(isimler[9])
# print(isimler[10])

# for i in range(12):
#     print(isimler[i])

#Listenin elemean sayısını öğrenme len(listenin_kendisi_buraya_verilir)

# print(len(isimler))
#
#
# for i in range(len(isimler)):
#     print(isimler[i])



############################ İlk eleman ve Son eleman #######################################

#sayilar = [20,85,12,33,99,120]

# print(sayilar[0])
#
# #Son eleman
# print(sayilar[-1])
#
# print(sayilar[len(sayilar)-1])

# print(sayilar[-1])
# print(sayilar[-2])
# print(sayilar[-3])
# print(sayilar[-4])
# print(sayilar[-5])
# print(sayilar[-6])


############################### Liste Dilimleme(Slicing) #####################################

# sayilar = [20,85,12,33,99,120]
# #Başlangıçtaki değer dahil edilir ama bitiş dahil edilmez.
# print(sayilar[:]) #Başlangıçtan bitişe kadar bütün elemanları alır.
# print(sayilar[:3])
# print(sayilar[2:5]) #12 33 99 #2.indeksden başla(2.indeks dahil) 5.indekse kadar(5.indeks dahil değil) elemanları al
# print(sayilar[2:]) #12 33 99 120
# print(sayilar[::2]) #Başlangıçtan itibaren ilk elemandan sonra kaçıncı elemanın alınacağını belirtiyoruz.
#



################################ Liste Elemanlarını EKLEME/SİLME/GÜNCELLEME ################################

# sayilar = [20,85,12,33,99,120]
#
# print(sayilar)
#print(sayilar[0])

#sayilar[0] = 280

#print(sayilar[0])

##### Append ile Ekleme #####
#Append ile listenin sonuna eleman eklenir.
# sayilar.append(91)
#
# print(sayilar)
#
# ##### insert() ile Ekleme #####
# #İnsert ile istenilen indekse eleman eklenir.
# sayilar.insert(1,66)
#
# print(sayilar)


############# Extend ile liste içerisine başka bir liste ekleme #########

# sayilar1 = [20,85,12,33,99,120]
# sayilar2 = [89,11,38,92,71,54]
#
# print(sayilar1)
# print(sayilar2)
#
# sayilar1.extend(sayilar2)
#
# print(sayilar1)

############ Pop ile eleman kaldırma işlemi ###########

#sayilar = [20,85,12,33,99,120]
#print(sayilar)



#pop ile birlikte listenin belirtilen indeksindeki eleman silinir.Belirtilmezse Listenin sonundaki eleman silinir.
# sayilar.pop()
# print(sayilar)

#Belirtilen aralıkta eleman silebilmek için del komutunu kullanalım
# del sayilar[3:5]
# print(sayilar)


#Clear ile listenin tamamı silinir.

#sayilar.clear()

#print(sayilar)

############# Remove ile birlikte ##############
#Liste içerisindeki elemanın kendisinin parametre olarak verilmesi durumunda silinmesini sağlar.
# sayilar.remove(33)
# print(sayilar)


############ LİSTE İÇERİSİNDE ELEMAN ARAMA ##########

#Elemanın index numarasını öğrenebiliriz.
# sayilar = [20,85,12,33,99,120]
# print(sayilar.index(120))
#
# #Count ile liste içerisindeki elemandan kaç adet olduğunu öğrenmek için kullanılır.
#
# isimler =  ["Tarık","Tarık","Ahmet"]
#
# print(isimler.count("Ahmet"))

############ LİSTE İÇERİSİNDE SIRALAMA ##########
#Liste içeriisndeki elemanları küçükten büyüğe doğru sırılar.Alfabetik olarakta küçükten büyüğe doğru sıralama yapar.
#sayilar = [20,85,12,33,99,120]

#sayilar.sort()
#Büyükten küçüğe doğru sıralaması için
#sayilar.sort(reverse=True)

#Reverse listeyi ters çevirir.
# sayilar.reverse()
# print(sayilar)


############## LİSTE KOPYALAMA ###########
#Referans Tip / Listelerde Referans Adresş kopyalanması.  Heap/Stack
# sayilar = [20,85,12,33,99,120]
#
# sayilar2 = []
#
# sayilar2 = sayilar
#
# sayilar.pop(1)
#
# print(sayilar)
# print(sayilar2)
#
# sayilar2.pop(4)
#
# print(sayilar)
# print(sayilar2)

#Copy()
#
# copy_sayi1 = [20,85,12,33,99,120]
# copy_sayi2 = []
#
# copy_sayi2 = copy_sayi1.copy()
#
# print(f"Kopya Liste ilk hali:{copy_sayi2}")
#
# copy_sayi2[0] = 10
#
# print(f"Kopya Liste değişim:{copy_sayi2}")
# print(f"Asıl Liste:{copy_sayi1}")
#

################ ÖDEV ##########################
"""
Eşyalar Listesi ->  "Pantolon" , "Ayakkabı" , "Tshirt"
3 ürün
String isim
Eşya Fiyat Listesi->  100         200           50
Eleman sayısı->3 fiyat 
Fiyat->float/int    

Eşya listesinde 0.indekste bulunan eşyanın fiyatı fiyat listesinde 0.indekste bulunacak.

Ekleme
Listeye bir ürün eklendğinde fiyatınıda fiyat listesine aynı indekse ekliyor olacaksınız.
Silme
Eşyalar lsitesinden silinen herhangi bir ürünün fiyatıda fiyat listesinden silinecek
GÜncelleme 
Eşyalar listesindeki güncellenmek istenen herhangi bir ürünün sadece fiyatı fiyat listesinde güncellenecek.



1.operaasyon Ekleme 
2. "         Güncelleme
3. "         Silme

....
....

Operasyonlardan sonra ürünler ve fiyatlar listesini mutlaka yazdırıp kullanıcıya gösterin


Bütün işlemler bittiğinde listenin son halini yazdırın.
"""



"""
CHALLENGE

1 adet boş liste tanımlayın.

Kullanıcıdan alınan değerlerden sadece tek olanlar bu liste içerisine kabul edilsin.

Liste uzunluğu 10 olana kadar ekleme işlemi devam etsin.

Liste uzunluğu 10 olduğunda işlemi sonlandırın.Listeyi ekrana yazdırın.
"""

# liste = []
#
# while len(liste)<10:
#     number = int(input("Bir sayı girin"))
#
#     if number%2 == 1:
#         liste.append(number)
#     else:
#         print("Lütfen Tek Sayı giriniz.")
#
#     print(f"Liste Uzunluğu:{len(liste)}")
#
# print(liste)


######### LİSTE ELEMANLARINI DÖNGÜYLE YAZDIRMA ###########


#aralik = range(0,10)

#print(aralik)

#aralik_listesi = [0,1,2,3,4,5,6,7,8,9]

isimler = ["Tarık","Berna","Deniz","Yasemin"]

# for i in range(len(isimler)):
#     print(isimler[i])


# for i in isimler:
#     print(i)


######## ENUMERATE #######
#Start=1 ifadesi arka planda tutulan indeks numaralarını değiştirmez.Sadece daha anlaşılır bir sıralama için ilk elemanı 1 den başlatır.
for index,item in enumerate(isimler,start=2):
    print(index,item)
    print(isimler.index(item))







