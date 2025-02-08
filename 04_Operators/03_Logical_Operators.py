
"""
Mantıksal Operatörler

 birden fazla önermenin bir arada bulunduğu durumlarda.
 Birbirlerine göre olan son durumu verir.

 or(+)  -  and(*)


 And bağlacı

 Kullanıcı username ve password bilgilerini giriyor.Girilen bilgiler veri tabanındaki kullanıcı verileriyle karşılaştırılıyor.
 Her bir senaryo aşağıda and bağlacı ile birbirine bağlanmıştır.

 userName(inputtandan gelen) == veriTabanıUserName(Veri tabanından gelen)
 userPassword(inputtandan gelen) == veriTabanıUserPassword(Veri tabanından gelen)

 False(0)  True(1)


 userName  And   userPassword     Sonuç
    0               0               0
    1               0               0
    1               1               1
    0               1               0


 OR Bağlacı


 ( userName  or email ) and password   sonuç
     1          0       and   1          1
     0          1       and   1          1
     0          0       and   1          0

     1          1       and   1          1



    0,9  10luk
    0,4  5lik
    0,1  2lik

"""
#
# userNameDB,passwordDB,emailDB = "t","1","trk"
#
# kullanicidan_username,kullanicidan_email,kullanicidan_password = input("Kullanıcı adı:"),input("Kullanıcı Email"),input("Şifre:")
#
#
# print(kullanicidan_username == userNameDB or kullanicidan_email == emailDB and kullanicidan_password == passwordDB)



#ÖRNEK-1 Kullanıcıdan doğum yılını girmesini isteyin daha sonrasında yaşını hesaplayıp 18 den büyük olup olmadığını kontrol ettirin.


dogum_yili = int(input("Dogum yili:"))

yas = 2025 - dogum_yili

print(yas)

print(yas > 18)





