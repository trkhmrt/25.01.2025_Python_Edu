import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QLineEdit, QCheckBox

app = QApplication([])
window = QWidget()
#layout = QVBoxLayout() #pencere içerisindeki elemanlar dikey olarak hizalanacak bir yerleşim alanı oluşturulur.
main_layout = QVBoxLayout() # V-> Vertical
layout = QHBoxLayout() # H -> Horizontal
layout2 = QVBoxLayout()

label = QLabel("Merhaba Dünya!")
label2 = QLabel("Bu PQYT6 Dersi!")
label3 = QLabel("Bu PQYT6 Dersi!")
label4 = QLabel("Bu PQYT6 Dersi!")
label5 = QLabel()
inputArea = QLineEdit()
inputArea.setPlaceholderText("Adınızı giriniz")
button = QPushButton("Tıkla")
button_kayit_ol = QPushButton("Kayıt Ol")

checkBox = QCheckBox("Onaylıyorum")
checkBox.setChecked(True)


def MesajYazdir():
    print("Butona tıklandı")
    label.setText("Tarık Hamarat")
    print(inputArea.text())
    checkBox.setChecked(False)

def KayitOl():
    if checkBox.isChecked():
        label5.setText(f"{inputArea.text()} isimli öğrenci kayıt edildi.")
    else:
        label5.setText("Lütfen şartlarını kabul ettiğinizi onaylayın!")




button.clicked.connect(MesajYazdir)
button_kayit_ol.clicked.connect(KayitOl)


layout.addWidget(label)
layout.addWidget(label2)
layout.addWidget(button)
layout.addWidget(inputArea)

layout2.addWidget(label3)
layout2.addWidget(label4)
layout2.addWidget(checkBox)
layout2.addWidget(button_kayit_ol)
layout2.addWidget(label5)

main_layout.addLayout(layout)
main_layout.addLayout(layout2)


window.setLayout(main_layout)

window.show()

app.exec()

# Ui



