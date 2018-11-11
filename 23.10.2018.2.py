from PyQt4.QtGui import*
from PyQt4.QtCore import*
class tabloOrnegi(QDialog):
    def __init__(self,ebeveyn=None):
        super(tabloOrnegi,self).__init__(ebeveyn)
        grid=QGridLayout()
        self.tablo=QTableWidget()
        self.tablo.resize(400,250)
        self.tablo.setRowCount(5)
        self.tablo.setColumnCount(3)
        grid.addWidget(self.tablo)
        item=QTableWidgetItem()
        item.setData(Qt.EditRole,1500)
        self.tablo.setItem(0,0,QTableWidgetItem(item))
        self.tablo.show()
        return uyg.exec_()
class tabloListeOrnegi(QDialog):
    def __init__(self,ebeveyn=None):
        super(tabloListeOrnegi,self).__init__(ebeveyn)
        data={'col':['1','2','3'],'col2': ['4','5','6'],'col3':['7','8','9']}
uyg=QApplication([])
pencere=tabloListeOrnegi()
pencere.show()
uyg.exec_
    
