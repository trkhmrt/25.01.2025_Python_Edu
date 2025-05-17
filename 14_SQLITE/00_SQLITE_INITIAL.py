import sqlite3
from tabulate import tabulate

connection = sqlite3.connect("OkulDB.db")
cursor = connection.cursor()


cursor.execute("SELECT * FROM OGRENCI")

ogrenciler = cursor.fetchall()

"""
if ogrenciler(yada herhangi bir koleksiyon yapısı) demek ogrenciler listesi içinde eleman var mı yok mu bunun kontrolünü yapar.Eleman yoksa false döner.Eleman varsada true döndürecek ve if içerisine girip elemanları yazdıracak.
"""
# if ogrenciler:
#     for ogrenci in ogrenciler:
#         for i in ogrenci:
#             print(i)


###TABULATE İLE
#basliklar = [baslik[0] for baslik in cursor.description]


# if ogrenciler:
#     print(tabulate(ogrenciler,headers=basliklar,tablefmt="grid"))



# cursor.close()
# cursor = connection.cursor()
#
# cursor.execute("SELECT * FROM OGRENCI")
#
# deneme = cursor.fetchall()


#cursor.execute("INSERT INTO OGRENCI (OgrenciAd,OgrenciYas,OgrenciTc) values (?,?,?)",('TEST TEST',56,1111))
#cursor.execute(f"DELETE FROM OGRENCI WHERE OgrenciID = '{5}'")
#connection.commit()



# cursor.execute("UPDATE OGRENCI SET OgrenciTC = ? WHERE OgrenciID = ? ",(323523,6))
# connection.commit()
#





# cursor.execute("SELECT OgrenciAd FROM OGRENCI")
#
# ogrenciler = cursor.fetchall()
# basliklar = [baslik[0] for baslik in cursor.description]
#
# if ogrenciler:
#     print(tabulate(ogrenciler, headers=basliklar, tablefmt="grid"))





