from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
class AnaPencere(QMainWindow):
    def __init__(self,p=None):
        super(AnaPencere,self).__init__(p)
        self.setWindowTitle("Logo Muhasebe Uygulamaları")
        self.setGeometry(200,200,800,400)
        self.menuEkleme()
        self.form_widget=FormWidget(self)
        self.setCentralWidget(self.form_widget)
        
    def menuEkleme(self):
        menubar=self.menuBar()
        stokMenu=menubar.addMenu("&Stok")
        stokEkle=stokMenu.addAction("&Stok Ekle")
        stokEkle.triggered.connect(self.stokEkleFonksiyon)
        stokCikar=stokMenu.addAction("&Stok Çıkar")
        stokGoster=stokMenu.addAction("&Stok Göster")
        siparisMwnu=menubar.addMenu("&Sipariş")
        faturaMenu=menubar.addMenu("&Fatura")
        cariMenu=menubar.addMenu("&Cari Hesap")
        kasaMenu=menubar.addMenu("&Kasa")
        bankaMenu=menubar.addMenu("&Banka")
        cekMenu=menubar.addMenu("&Çek")
        topluMenu=menubar.addMenu("&Toplu İşlemler")
        sistemMenu=menubar.addMenu("&Sistem İşlemleri")
    def stokEkleFonksiyon(self):
        self.stokEkle=StokEkle()
        self.stokEkle.show()
            
class FormWidget(QWidget):
    def __init__(self,p=None):
        super(FormWidget,self).__init__(p)
        #Frame 1 ve 2 Yaratıldı
        frame=QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame2=QFrame()
        frame2.setFrameStyle(QFrame.Panel)
        
        #Widget Yaratıldı
        fisWidget=QWidget()
        fisNo=QLineEdit()
        fisTarih=QLineEdit()
        fisGetir=QPushButton()
        formLayout=QFormLayout()
        formLayout.addRow("Fiş No",fisNo)
        formLayout.addRow("Fiş Tarih",fisTarih)
        fisWidget.setLayout(formLayout)
        fisWidget.show()
        
        ozelKodWidget=QWidget()
        ozelKod=QLineEdit()
        yetkiKod=QLineEdit()
        ozelKodGoster=QPushButton("Göster")
        formLayout2=QFormLayout()
        formLayout2.addRow("Özel Kod:",ozelKod)
        formLayout2.addRow("Yetki Kod:",yetkiKod)
        formLayout2.addRow(ozelKodGoster)
        ozelKodWidget.setLayout(formLayout2)
        ozelKodWidget.show()

        #DockWidget yaratıldı yukarıdaki fisWidget bağlandı
        dockWidget=QDockWidget("Fiş No'ya Göre Göster",self)
        dockWidget.setFeatures(dockWidget.NoDockWidgetFeatures)
        dockWidget.setWidget(fisWidget)

        dockWidget2=QDockWidget("Özel Koda Göre Göster",self)
        dockWidget2.setFeatures(dockWidget.NoDockWidgetFeatures)
        dockWidget2.setWidget(ozelKodWidget)
        
        izgara=QGridLayout()
        izgara.addWidget(dockWidget)
        frame.setLayout(izgara)
        izgara2=QGridLayout()
        izgara2.addWidget(dockWidget2)
        frame2.setLayout(izgara2)
        
        
        yatay=QHBoxLayout()
        yatay.addWidget(frame)
        yatay.addWidget(frame2)
        yatay.setAlignment(Qt.AlignLeft)

        izgara3=QGridLayout()
        tablo=QTableWidget()
        aciklama=QLineEdit()
        tablo.resize(600,250)
        tablo.setRowCount(5)
        tablo.setColumnCount(6)
        tablo.setHorizontalHeaderLabels(['Hesap Kodu','Hesap Adı','İşlem Türü','Cari Kodu','Tutar','İşlem Tarihi'])
        izgara3.addWidget(tablo,0,0)
        izgara3.addWidget(aciklama,1,0)
        tablo.show()

        dikey=QVBoxLayout()
        dikey.addLayout(yatay)
        dikey.addLayout(izgara3)
        self.setLayout(dikey)
        self.setGeometry(0,0,100,100)

class StokEkle(QDialog):
    def __init__(self,p=None):
        super(StokEkle,self).__init__(p)
        stokForm=QGridLayout()
        barkod=QLineEdit()
        adi=QLineEdit()
        departman=QLineEdit()
        miktar=QLineEdit()
        alisFiyati=QLineEdit()
        kod=QLineEdit()
        kdv=QLineEdit()
        birim=QLineEdit()
        satiFiyati=QLineEdit()
        kaydet=QPushButton()
        vazgec=QPushButton()
        stokForm.addWidget(QLabel("Barkod"),0,0)
        stokForm.addWidget(barkod,0,1)
        stokForm.addWidget(QLabel("Kod"),0,2)
        stokForm.addWidget(kod,0,3)
        stokForm.addWidget(QLabel("Adı"),1,0)
        stokForm.addWidget(adi,1,1)
        stokForm.addWidget(QLabel("Deprtman",2,0))
        stokForm.addWidget(departman,2,1)
        stokForm.addWidget(QLabel("KDV",2,2))
        stokForm.addWidget(kdv,2,3)
        stokForm.addWidget(QLabel("Miktar",3,0))
        stokForm.addWidget(miktar,3,1)
        stokForm.addWidget(QLabel("Birim",3,2))
        stokForm.addWidget(birim,3,3)
        stokForm.addWidget(QLabel("Alış Fiyatı",4,0))
        stokForm.addWidget(alisFiyati,4,1)
        stokForm.addWidget(QLabel("Satış Fiyatı",4,2))
        stokForm.addWidget(satisFiyati,4,3)
        stokForm.addWidget(kaydet,5,0)
        stokForm.addWidget(vazgec,5,1)
        self.setLayout(stokForm)
        self.setWindowTitle("Stok Ekleme Ekranı")
        
        
        
uyg=QApplication(sys.argv)
ana=AnaPencere()
ana.show()
