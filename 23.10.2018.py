from PyQt4.QtGui import *
from PyQt4.QtCore import *
class yaziTipiDlg(QDialog):
    def __init__(self,ebeveyn=None):
        super(yaziTipiDlg,self).__init__(ebeveyn)
        grid=QGridLayout()
        grid.addWidget(QLabel("Yazı Tipi:"),0,0)
        self.yaziTipiListe=QComboBox()
        self.yaziTipiListe.addItems(['Arial','Verdana','Comic'])
        grid.addWidget(self.yaziTipiListe,0,1)

        kabulDugme=QPushButton('Tamam')
        redDugme=QPushButton('Vazgeç')
        self.connect(kabulDugme,SIGNAL('pressed()'),self.accept)
        self.connect(redDugme,SIGNAL('pressed()'),self.reject)
        kabulDugme.setDefault(True)
        dugmeKutusu=QHBoxLayout()
        dugmeKutusu.addWidget(kabulDugme)
        dugmeKutusu.addWidget(redDugme)
        grid.addLayout(dugmeKutusu,1,0,1,2)

        self.setLayout(grid)
        self.setWindowTitle("Yazı Tipi Değiştir")
class yaziTipi(QDialog):
    def __init__(self,ebeveyn=None):
        super(yaziTipi,self).__init__(ebeveyn)
        self.yaziTipi='Verdana'
        self.metin='<font face="%s" size="+3">Merhaba Dünya</font>'
        self.etiket=QLabel(self.metin%self.yaziTipi)
        kutu=QVBoxLayout()
        kutu.addWidget(self.etiket)
        yaziTipiDugme=QPushButton('Yazı Tipini Değiştir')
        self.connect(yaziTipiDugme,SIGNAL('pressed()'),self.yaziTipiDegistir)
        kutu.addWidget(yaziTipiDugme)
        self.setLayout(kutu)
        self.setWindowTitle("Yazı tipi dialog penceresi")

    def yaziTipiDegistir(self):
       diyalog=yaziTipiDlg()
       yaziTipiIndex=diyalog.yaziTipiListe.findText(self.yaziTipi)
       diyalog.yaziTipiListe.setCurrentIndex(yaziTipiIndex)
       if diyalog.exec():
            self.yaziTipi=diyalog.yaziTipiListe.currentText()
            self.etiket.setText(self.metin%self.yaziTipi)

uyg=QApplication([])
pencere=yaziTipi()
pencere.show()
uyg.exec
