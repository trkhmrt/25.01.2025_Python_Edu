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

# urunler=["Pantolon","Ayakkabı","Tshirt"]
# urun_fiyatlari=[100,50,20]
#
#
# for i in range(len(urunler)):
#     print(f"{i+1}.ürün->{urunler[i]}-{urun_fiyatlari[i]}₺")
#
#
#
# eklenecek_urun = input("Eklenecek ürün adını giriniz:")
# urunler.append(eklenecek_urun)
# eklenecek_urun_fiyati = int(input("Eklenecek ürün fiyatını giriniz:"))
# urun_fiyatlari.append(eklenecek_urun_fiyati)
#
#
#
# for i in range(len(urunler)):
#     print(f"{i+1}.ürün->{urunler[i]}-{urun_fiyatlari[i]}₺")
#
#
# silinecek_urun_sira_no = int(input("Silinecek ürün numarasını giriniz:"))
# urunler.pop(silinecek_urun_sira_no-1)
# urun_fiyatlari.pop(silinecek_urun_sira_no-1)
#
# for i in range(len(urunler)):
#     print(f"{i+1}.ürün->{urunler[i]}-{urun_fiyatlari[i]}₺")
#
#
#
# guncellenecek_urun_sira_no = int(input("Güncellenecek ürün numarasını giriniz:"))
# urun_fiyatlari[guncellenecek_urun_sira_no-1] = int(input("Güncel fiyatı giriniz:"))
#
# print(urunler)
# print(urun_fiyatlari)


urunler=["Pantolon","Ayakkabı","Tshirt"]
urun_fiyatlari=[100,50,20]


while True:
    print("""
    Butik Otomasyonuna Hoşgeldiniz...
        
        Ürünlerimizin Listesini Aşağıda görebilirsiniz...
    """)

    for i in range(len(urunler)):
         print(f"{i+1}.ürün->{urunler[i]}-{urun_fiyatlari[i]}₺")

    print("""
             1-Ürün Ekleme
             2-Ürün Çıkarma
             3-Ürün Güncelleme 
             4-Çıkış...      
            """)

    islem_no = int(input("Yapmak istediğiniz işlemi seçiniz"))

    if islem_no == 1:
         while True:
             eklenecek_urun = input("Eklenecek ürün adını giriniz:")
             if len(eklenecek_urun)<3:
                 print("""!!!Lütfen 3 karakterden uzun bir ürün ismi giriniz...!!!""")
             else:
                 urunler.append(eklenecek_urun)
                 eklenecek_urun_fiyati = int(input("Eklenecek ürün fiyatını giriniz:"))
                 urun_fiyatlari.append(eklenecek_urun_fiyati)
                 break

    elif islem_no == 2:

        silinecek_urun_sira_no = int(input("Silinecek ürün numarasını giriniz:"))
        urunler.pop(silinecek_urun_sira_no-1)
        urun_fiyatlari.pop(silinecek_urun_sira_no-1)

    elif islem_no == 3:

         guncellenecek_urun_sira_no = int(input("Güncellenecek ürün numarasını giriniz:"))
         urun_fiyatlari[guncellenecek_urun_sira_no-1] = int(input("Güncel fiyatı giriniz:"))

    elif islem_no == 4:

        break
    else:
        print("""
        
                !!!Lütfen Geçerli Bir İşlem Giriniz...
        """)



#Tuple,Set(Küme),Dictionary "İsim":"Tarık"
#Object oriented Programming (12_OOP)

