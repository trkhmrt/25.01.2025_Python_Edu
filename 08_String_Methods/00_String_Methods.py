"""
STRING METHODS
"""

######### BÜYÜK KÜÇÜK HARF DÖNÜŞÜMÜ ########

# title = "merhaba dünya"
#
# print(title.upper())
#
# paragraf = "MERHABA DÜNYA"
#
# print(paragraf.lower())
#
# baslik = "merhaba dünya"
#
# print(baslik.title())

# bas_harf_buyuk = "ankara"
# print(bas_harf_buyuk.capitalize())

# buyuk_kucuk_kucuk_buyuk = "mERHABA dÜNYA"
# print(buyuk_kucuk_kucuk_buyuk.swapcase())


############  PARÇALAMA VE BİRLEŞTİRME ##############

# text = "Merhaba Dünya ben tarık"
#
# kelime_listesi = text.split()
#
# print(type(kelime_listesi))
# print(kelime_listesi)

# text2 = "Merhaba Dünya ben tarık"
#
# kelime_listesi_2 = text2.split("a")
#
# print(kelime_listesi_2)


######## BİRLEŞTİRME ########
#
# kelimeler = ["Tarık","Hoca"]
# ilanno_firmId = ["94349","671"]
#
# print("https://www.hepsiemlak.com/izmir-karsiyaka-yali-satilik/daire/"+"-".join(ilanno_firmId))

###### KARAKTER KONTROL METOTLARI ######

# text = "123456"
#
# text2 = "Tarık1234"
#
# text3 = "TARIK"

# print(text.isdigit()) # Bütün karakterler rakam mı?
# print(text2.isalnum()) #String ifade içerisinde harf veya rakam var mı ? Boşluk veya özel karakter içermemeli _!@#*%& gibi
# print(text3.isalpha()) #İfade sadece harflerden mi oluşuyor ?
#
# print("  ".isspace()) # Tamamen içeride space karakterinin olması lazım yani boşluk

# print(text3.islower())
# print(text3.isupper())




############# BOŞLUK KARAKTERLERİNİ TEMİZLEME ###############

#123456

### RSTRIP() ####  Sağdaki  boşluğu siler
#girdi = "123456 "
#
# print(girdi+"78")
#
# print(girdi.rstrip()+"78")


### LSTRIP() #### Soldaki boşluğu siler
# girdi2 = " 123456"
#
# print("78"+girdi2)
#
# print("78"+girdi2.lstrip())
#

#### STRIP() #####  Sağ ve Sol boşlukları siler.


# girdi2 = " 23456 "
#
# print("01"+girdi2+"78")
#
# print("01"+girdi2.strip()+"78")

###### BULMA VE DEĞİŞTİRME METOTLARI ######

#text = "Merhaba Dünya"

#print(text.find("a",4,13)) #string ifadenin aranmaya başlanacağı indeks değeri default olarak 0 dır.Ancak siz parametre olarak bir başlangıç indeks değeri verirseniz o indeks değeri dahil sağa doğru giderek aranan string ifadeyle ilk karşılaştığı indeks numarasını alır ve ekrana basar.
## NOT !! -> Aranan aralıkta string ifade bulunamazsa cevap olarak -1 döner.


# print(text.rfind("a"))
# print(text.index("D"))
# print(text.replace("a","b"))
#
#
# print(text.startswith("M"))
# print(text.startswith("Mer"))
# print(text.startswith("Merhaba Dünya"))
# print(text.endswith("Merhaba Dünya"))

#######
# ÖDEV
# find metodunu kullanarak text string'i içerisindeki a harflerinin indeks numaralarını yazdırın.
#######



#### DOLDURMA VE HİZALAMA ##########

text = "TARIK"

print(text.zfill(10))













