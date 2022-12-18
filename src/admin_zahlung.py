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
from Model_PV import Zahlung
import constants
from __utilities import utilities
from stylestrings import ledStyleString, ledStyleStringDisabled

class Ui_adminZahlung(QDialog):
    def setupUi(self, adminZahlung):
        self.modus = constants.MODUS_NULL
        
        adminZahlung.setObjectName("adminZahlung")
        adminZahlung.resize(400, 376)
        self.buttonBox = QtWidgets.QDialogButtonBox(adminZahlung)
        self.buttonBox.setGeometry(QtCore.QRect(50, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.layoutWidget = QtWidgets.QWidget(adminZahlung)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 181, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lblZahlung = QtWidgets.QLabel(self.layoutWidget)
        self.lblZahlung.setObjectName("lblZahlung")
        self.horizontalLayout.addWidget(self.lblZahlung)
        
        self.ledZahlung = QtWidgets.QLineEdit(self.layoutWidget)
        self.ledZahlung.setEnabled(False)
        self.ledZahlung.setStyleSheet(ledStyleStringDisabled)
        self.ledZahlung.setObjectName("ledZahlung")
        self.horizontalLayout.addWidget(self.ledZahlung)
        
        self.layoutWidget1 = QtWidgets.QWidget(adminZahlung)
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
        self.horizontalLayout_2.addWidget(self.btnLoeschen)
        
        self.tableWidget = QtWidgets.QTableWidget(adminZahlung)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 300, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Zahlung an", "TimeStamp"])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)


        self.retranslateUi(adminZahlung)
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), adminZahlung.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), adminZahlung.reject)
        QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.__neuEintrag)
        QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.__bearbeiteEintrag)
        QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.__loescheEintrag)
        self.tableWidget.itemSelectionChanged.connect(self.__item_Clicked)
#
        QtCore.QMetaObject.connectSlotsByName(adminZahlung)
        
        self.__populate_tableview()
        self.__setButtonsFalse()
        
    def retranslateUi(self, DiaadminAnrede):
        DiaadminAnrede.setWindowTitle(QtWidgets.QApplication.translate("DiaadminZahlung", "Admin - Art", None, -1))
        self.lblZahlung.setText(QtWidgets.QApplication.translate("DiaadminZahlung", "Zahlung:", None, -1))
        self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminZahlung", "Neu", None, -1))
        self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminZahlung", "Bearbeiten", None, -1))
        self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminZahlung", "Löschen", None, -1))

    def __setButtonsTrue(self):
        self.btnBearbeiten.setEnabled(True)
        self.btnLoeschen.setEnabled(True)
        
    def __setButtonsFalse(self):
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        
    def __populate_tableview(self):
        #print("Enter __populate_tableview")
        session = utilities.createSession()
        c = 0
        for zahlung in session.query(Zahlung).order_by(Zahlung.zname):
            #print("ID: ", art.id_art, "Art: ", art.art, "Created: ", art.create_time)
            self.tableWidget.setRowCount(c+1)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(str(zahlung.id_zahlung)))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(zahlung.zname))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(str(zahlung.create_time)))
            c = c + 1
        self.tableWidget.resizeColumnsToContents()
        session.close()
        
    def __neuEintrag(self):
        #print("Enter __neuEintrag")
        self.ledZahlung.setEnabled(True)
        self.ledZahlung.setStyleSheet(ledStyleString)
        self.ledZahlung.setText("")   
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        self.modus = constants.MODUS_NEU
        
    def __save_data(self):
        #print("Enter __save_data: ", self.ledZahlung.text() + " " + str(len(self.ledZahlung.text())))
        session = utilities.createSession()
        if self.modus == constants.MODUS_NEU:
            if len(self.ledZahlung.text()) != 0:
                newAnrede = Zahlung(zname = self.ledZahlung.text())
                session.add(newAnrede)
        elif self.modus == constants.MODUS_BEARBEITEN:
            #print("Modus Bearbeiten")
            fcontent = self.ledZahlung.text()
            session.query(Zahlung).filter(Zahlung.id_zahlung == self.index).update({Zahlung.zname:fcontent}, synchronize_session = False)
        elif self.modus == constants.MODUS_LOESCHEN:
            #print("Modus Löschen")
            session.query(Zahlung).filter(Zahlung.id_zahlung == self.index).delete()    
        utilities.closeSessionCommit(session)
        
    def __bearbeiteEintrag(self):
        #print("Enter __bearbeiteEintrag")
        self.modus = constants.MODUS_BEARBEITEN
        item1 = self.tableWidget.item(self.zeile, 1)
        self.ledZahlung.setText(str(item1.text()))        

    def __loescheEintrag(self):
        #print("Enter __loescheEintrag")
        self.modus = constants.MODUS_LOESCHEN
        
    def __item_Clicked(self):
        #print("Signal ItemSelectionChanged received, Item selected: ")
        self.zeile = self.tableWidget.selectedItems()[0].row()
        item0 = self.tableWidget.item(self.zeile, 0)
        self.index = int(item0.text())
        self.ledZahlung.setEnabled(True)
        self.ledZahlung.setStyleSheet(ledStyleString)
        self.__setButtonsTrue()

        #print (item0.text(), item1.text())
        
 

