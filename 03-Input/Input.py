"""
Input metoduyla birlikte kullanıcının console üzerinden veri girmesi sağlanır.

Uygulamada input ifadesi ile karşılaşıldığında değer girip enter'a basana kadar uygulama bekletilir.



"""

#isim = "Tarık"

#print("")


#Output -> print

#isim = input("İsim giriniz")
#soyisim = input("Soyisim giriniz")

#print("İsminiz:",isim)

#print(f"Ad: {isim}\nSoyad: {soyisim}")



# f ifadesi ile birlikte python tarafından tanımlanmış olan özel yazdırma tekniğini kullanacağımızı söylüyoruz.Bu sayede { } içerisinde istenilen değişkenlerin verileri direkt olarak yazdırılabilir. f-> Format demek. Kısaca  print ile birlikte özel bir formatda yazdırmak istiyorum anlamına geliyor.

# print(f"""
#         Ad: {isim}
#
# Soyad: {soyisim}
#
# """)



#


#String ifadelerde + işareti iki stringi birleştirmek için kullanılır.

# sayi1 = input("Sayi 1 giriniz")
# sayi2 = input("Sayi 2 giriniz")
#
# print(sayi1 + sayi2)




#BOXING İLE TİP DÖNÜŞÜMÜ


#sayi1 = input("Sayi 1 giriniz")
#sayi1 = int(sayi1)



sayi1 = int(input("Sayi 1 giriniz"))
sayi2 = int(input("Sayi 2 giriniz"))


print(sayi1 + sayi2)




