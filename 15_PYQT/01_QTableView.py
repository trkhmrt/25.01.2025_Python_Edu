import sqlite3

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTableView, QVBoxLayout, QMessageBox
from PyQt6.uic.Compiler.qtproxies import QtWidgets
from tabulate import tabulate


def satirVeSutun(index):
    satir_no = index.row()
    # sutun_no = index.column()
    ogrenci_id = model.item(satir_no, 0).text()

    cevap = QMessageBox.question(window,"Silme Onayı", f"{ogrenci_id}idli öğrenciyi silmek istiyor musunuz ?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    if cevap == QMessageBox.StandardButton.Yes:
        crsr.execute(f"DELETE FROM OGRENCI WHERE OgrenciID = '{ogrenci_id}'")
        con.commit()
        TabloyuGuncelle()
        #model.removeRow(satir_no)
    else:
        print("Öğrenci silmekten vazgeçtiniz.")


def TabloyuGuncelle():
    model.removeRows(0,model.rowCount())
    crsr.execute("SELECT * FROM OGRENCI")
    ogrenciler = crsr.fetchall()
    for item in ogrenciler:
        itemlar = [QStandardItem(str(veri)) for veri in item]
        model.appendRow(itemlar)







con = sqlite3.connect("OkulDB.db")
crsr = con.cursor()

crsr.execute("SELECT * FROM OGRENCI")
ogrenciler = crsr.fetchall()

app = QApplication([])
window = QWidget()

main_layout = QVBoxLayout()

label = QLabel("ORENCİLER TABLOSU")
guncelle_butonu = QPushButton("GÜNCELLE")
table = QTableView()
model = QStandardItemModel()
model.setHorizontalHeaderLabels(["OgrenciID", "OgrenciAd", "OgrenciYas", "OgrenciTC"])
table.setModel(model)

table.doubleClicked.connect(satirVeSutun)
guncelle_butonu.clicked.connect(TabloyuGuncelle)

for item in ogrenciler:
    itemlar = [QStandardItem(str(veri)) for veri in item]
    model.appendRow(itemlar)

main_layout.addWidget(label)
main_layout.addWidget(table)
main_layout.addWidget(guncelle_butonu)

window.setLayout(main_layout)

window.show()

app.exec()
