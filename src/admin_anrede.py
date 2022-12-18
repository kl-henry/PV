# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_anrede.ui',
# licensing of 'ui_anrede.ui' applies.
#
# Created: Wed Apr 17 11:44:52 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView
from Model_PV import Anrede
import constants
from __utilities import utilities
from stylestrings import ledStyleString, ledStyleStringDisabled

class Ui_adminAnrede(QDialog):
    def setupUi(self, adminAnrede):
        self.modus = constants.MODUS_NULL
        
        adminAnrede.setObjectName("adminAnrede")
        adminAnrede.resize(400, 376)
        self.buttonBox = QtWidgets.QDialogButtonBox(adminAnrede)
        self.buttonBox.setGeometry(QtCore.QRect(50, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.layoutWidget = QtWidgets.QWidget(adminAnrede)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 181, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lblAnrede = QtWidgets.QLabel(self.layoutWidget)
        self.lblAnrede.setObjectName("lblAnrede")
        self.horizontalLayout.addWidget(self.lblAnrede)
        
        self.ledAnrede = QtWidgets.QLineEdit(self.layoutWidget)
        self.ledAnrede.setEnabled(False)
        self.ledAnrede.setStyleSheet(ledStyleStringDisabled)
        self.ledAnrede.setObjectName("ledAnrede")
        self.horizontalLayout.addWidget(self.ledAnrede)
        
        self.layoutWidget1 = QtWidgets.QWidget(adminAnrede)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 280, 254, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.btnNeu = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnNeu.setObjectName("btnNeu")
        self.horizontalLayout_2.addWidget(self.btnNeu)
        
        self.btnBearbeiten = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnBearbeiten.setObjectName("btnBearbeiten")
        self.horizontalLayout_2.addWidget(self.btnBearbeiten)
        
        self.btnLoeschen = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnLoeschen.setObjectName("btnLoeschen")
        self.btnLoeschen.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.btnLoeschen)
        
        self.tableWidget = QtWidgets.QTableWidget(adminAnrede)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 300, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Anrede", "TimeStamp"])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)


        self.retranslateUi(adminAnrede)
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), adminAnrede.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), adminAnrede.reject)
        QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.__neuEintrag)
        QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.__bearbeiteEintrag)
        QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.__loescheEintrag)
        self.tableWidget.itemSelectionChanged.connect(self.__item_Clicked)
#
        QtCore.QMetaObject.connectSlotsByName(adminAnrede)
        
        self.__populate_tableview()
        self.__setButtonsFalse()
        
    def retranslateUi(self, DiaadminAnrede):
        DiaadminAnrede.setWindowTitle(QtWidgets.QApplication.translate("DiaadminAnrede", "Admin - Art", None, -1))
        self.lblAnrede.setText(QtWidgets.QApplication.translate("DiaadminAnrede", "Art:", None, -1))
        self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminAnrede", "Neu", None, -1))
        self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminAnrede", "Bearbeiten", None, -1))
        self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminAnrede", "Löschen", None, -1))

    def __setButtonsTrue(self):
        self.btnBearbeiten.setEnabled(True)
        
    def __setButtonsFalse(self):
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        
    def __populate_tableview(self):
        #print("Enter __populate_tableview")
        session = utilities.createSession()
        c = 0
        for anrede in session.query(Anrede):
            #print("ID: ", anrede.id_anrede, "Art: ", anrede.anrede, "Created: ", anrede.create_time)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(str(anrede.id_anrede)))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(anrede.anrede))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(str(anrede.create_time)))
            c = c + 1
        self.tableWidget.resizeColumnsToContents()
        session.close()
        
    def __neuEintrag(self):
        #print("Enter __neuEintrag")
        self.ledAnrede.setEnabled(True)
        self.ledAnrede.setStyleSheet(ledStyleString)
        self.ledAnrede.setText("")   
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        self.modus = constants.MODUS_NEU
        
    def __save_data(self):
        #print("Enter __save_data: ", self.ledAnrede.text() + " " + str(len(self.ledAnrede.text())))
        session = utilities.createSession()
        if self.modus == constants.MODUS_NEU:
            if len(self.ledAnrede.text()) != 0:
                newAnrede = Anrede(anrede = self.ledAnrede.text())
                session.add(newAnrede)
        elif self.modus == constants.MODUS_BEARBEITEN:
            #print("Modus Bearbeiten")
            fcontent = self.ledAnrede.text()
            session.query(Anrede).filter(Anrede.id_anrede == self.index).update({Anrede.anrede:fcontent}, synchronize_session = False)
        elif self.modus == constants.MODUS_LOESCHEN:
            #print("Modus Löschen")
            session.query(Anrede).filter(Anrede.id_anrede==self.index).delete()    
        utilities.closeSessionCommit(session)
        
    def __bearbeiteEintrag(self):
        #print("Enter __bearbeiteEintrag")
        self.modus = constants.MODUS_BEARBEITEN
        item1 = self.tableWidget.item(self.zeile, 1)
        self.ledAnrede.setText(str(item1.text()))        

    def __loescheEintrag(self):
        #print("Enter __loescheEintrag")
        self.modus = constants.MODUS_LOESCHEN
        
    def __item_Clicked(self):
        #print("Signal ItemSelectionChanged received, Item selected: ")
        self.zeile = self.tableWidget.selectedItems()[0].row()
        item0 = self.tableWidget.item(self.zeile, 0)
        self.index = int(item0.text())
        self.__setButtonsTrue()

        #print (item0.text(), item1.text())
        
 

