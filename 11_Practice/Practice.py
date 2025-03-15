"""
Sözlük Yapısı
Envanter
{
Urun1:{ÜrünAdı:KapıKolu,Fiyat:123,EnvanterDurumu:"Var"}
Urun2:{ÜrünAdı:KapıKolu,Fiyat:123,EnvanterDurumu:"Var"}
Urun3:{ÜrünAdı:KapıKolu,Fiyat:123,EnvanterDurumu:"Var"}
Urun4:{ÜrünAdı:KapıKolu,Fiyat:123,EnvanterDurumu:"Var"}
}
Ekle,Sil,Güncelle,Ara

Calisanlar
[
"Tarık","Deniz","Sercan"
]
Ekle,Sil,Güncelle,Ara

While True ile MEnü oluşturulacak.
Metotlar kullanılacak.
Ekle,sil,Güncelle bunlar için geri değer döndürmeyen metotlar kullanılacak.
Ara işlemleri geriye değer döndüren metotlarda yazılacak.
"""

# Ürünleri sözlük olarak tanımladık. Key-Value
urunler = {
    "Urun1": {"UrunAdi": "Ayakkabı", "Fiyat": 120, "EnvanterDurumu": "yok"}
    , "Urun2": {"UrunAdi": "Gömlek", "Fiyat": 220, "EnvanterDurumu": "var"},
    "Urun3": {"UrunAdi": "Gözlük", "Fiyat": 450, "EnvanterDurumu": "var"}
}


calisanlar = ["Tarık","Deniz","Sercan"]

def calisanlariListele():
    for index,calisan in enumerate(calisanlar):
        print(f"{index+1}-{calisan}")

def urunleriListele():
    for key,value in urunler.items():
        print(f"{key}:{value}")


#KeyError ve ValueError tryExceptle yakalanacak
while True:
    try:
        ana_menu_secim = int(input("1-Urun İşlemleri\n2-Çalışan İşlemleri\n3-Çıkış Yap"))
        if ana_menu_secim == 1:
            while True:
                ana_menu_secim_1 = int(input("1-Urun Ekle\n2-Ürün Sil\n3-Ürün Güncelle\n4-Bir üst menüye dön"))
                if ana_menu_secim_1 == 1:
                    urunleriListele()
                    yeni_urun_keyi = "Urun" + str(len(urunler) + 1)
                    yeni_urun_adi = input("Yeni ürün adı giriniz")
                    yeni_urun_fiyat = int(input("Yeni ürün fiyatını giriniz"))
                    urunler[yeni_urun_keyi] = {"UrunAdi": yeni_urun_adi, "Fiyat": yeni_urun_fiyat,
                                               "EnvanterDurumu": "var"}
                elif ana_menu_secim_1 == 2:
                    urunleriListele()
                    silinecek_urun_keyi = input("Silinecek ürün keyini giriniz")
                    urunler.pop(silinecek_urun_keyi.capitalize())
                elif ana_menu_secim_1 == 3:
                    urunleriListele()
                    guncellenecek_urun_keyi = input("Güncellenecek ürün keyini giriniz").capitalize()
                    urunler[guncellenecek_urun_keyi]["Fiyat"] = int(input("Güncel fiyatı giriniz"))
                elif ana_menu_secim_1 == 4:
                    break
                else:
                    print("Lütfen geçerli bir tuşa basınız.")
        elif ana_menu_secim == 2:
            while True:
                ana_menu_secim_2 = int(input("1-Çalışan Ekle\n2-Çalışan Sil\n3-Çalışan Güncelle\n4-Çalışan Ara\n5-Bir üst menüye dön"))
                if ana_menu_secim_2 == 1:
                    calisanlariListele()
                    yeni_calisan_ismi = input("Yeni çalışan ismi giriniz")
                    calisanlar.append(yeni_calisan_ismi)
                elif ana_menu_secim_2 == 2:

                    calisanlariListele()
                    silinecek_calisan_sira_no = int(input("Silinecek çalışan sıra numarasını giriniz"))
                    calisanlar.pop(silinecek_calisan_sira_no-1)
                elif ana_menu_secim_2 == 3:
                    calisanlariListele()
                    güncellenecek_calisan_sira_no = int(input("Güncellenecek çalışan sıra numarasını giriniz"))
                    calisanlar[güncellenecek_calisan_sira_no-1] = input("Yeni bir isim değeri giriniz")
                elif ana_menu_secim_2 == 4:
                    aranacak_calisan_sira_no = int(input("Sıra numarasını giriniz"))
                    for i,item in enumerate(calisanlar):
                        if i==aranacak_calisan_sira_no-1:
                            print(item)
                            break


                elif ana_menu_secim_2 == 5:
                    break
                else:
                    print("Lütfen geçerli bir tuşa basınız.")
        elif ana_menu_secim == 3:
            break
        else:
            print("Lütfen geçerli bir tuşa basınız.")
    except IndexError:
        print("Verilen değer listenin uzunluğu dışındaydı.")
    except ValueError:
        print("Girilen verinin veri tipine dikkat edin.")
    except KeyError:
        print("Girilen key değeri sözlükte bulunmuyor.")

