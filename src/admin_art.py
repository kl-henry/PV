# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_anrede.ui',
# licensing of 'ui_anrede.ui' applies.
#
# Created: Wed Apr 17 11:44:52 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from Model_PV import Art
import constants
from __utilities import utilities
from stylestrings import ledStyleString

class Ui_adminArt(QDialog):
    def setupUi(self, adminArt):
        self.modus = constants.MODUS_NULL
        
        adminArt.setObjectName("adminArt")
        adminArt.resize(400, 376)
        self.buttonBox = QtWidgets.QDialogButtonBox(adminArt)
        self.buttonBox.setGeometry(QtCore.QRect(50, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.layoutWidget = QtWidgets.QWidget(adminArt)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 181, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lblArt = QtWidgets.QLabel(self.layoutWidget)
        self.lblArt.setObjectName("lblArt")
        self.horizontalLayout.addWidget(self.lblArt)
        
        self.ledArt = QtWidgets.QLineEdit(self.layoutWidget)
        self.ledArt.setEnabled(True)
        self.ledArt.setStyleSheet(ledStyleString)
        self.ledArt.setObjectName("ledArt")
        self.horizontalLayout.addWidget(self.ledArt)
        
        self.layoutWidget1 = QtWidgets.QWidget(adminArt)
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
        
        self.btnSuchen = QtWidgets.QPushButton(adminArt)
        self.btnSuchen.setGeometry(QtCore.QRect(220, 30, 80, 26))
        self.btnSuchen.setObjectName("btnSuchen")
        
        self.tableWidget = QtWidgets.QTableWidget(adminArt)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 300, 141))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Art", "TimeStamp"])
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)


        self.retranslateUi(adminArt)
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), adminArt.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), adminArt.reject)
        QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.__neuEintrag)
        QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.__bearbeiteEintrag)
        QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.__loescheEintrag)
        QtCore.QObject.connect(self.btnSuchen, QtCore.SIGNAL("clicked()"), self.__Suchen)
        self.tableWidget.itemSelectionChanged.connect(self.__item_Clicked)
#
        QtCore.QMetaObject.connectSlotsByName(adminArt)
        
        self.__populate_tableview()
        self.__setButtonsFalse()
        
    def retranslateUi(self, DiaadminAnrede):
        DiaadminAnrede.setWindowTitle(QtWidgets.QApplication.translate("DiaadminArt", "Admin - Art", None, -1))
        self.lblArt.setText(QtWidgets.QApplication.translate("DiaadminArt", "Art:", None, -1))
        self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminArt", "Neu", None, -1))
        self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminArt", "Bearbeiten", None, -1))
        self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminArt", "Löschen", None, -1))
        self.btnSuchen.setText(QtWidgets.QApplication.translate("DiaadminArt", "Suchen", None, -1))

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
        for art in session.query(Art).order_by(Art.aname):
            #print("ID: ", art.id_art, "Art: ", art.art, "Created: ", art.create_time)
            self.tableWidget.setRowCount(c+1)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(str(art.id_art)))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(art.aname))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(str(art.create_time)))
            c = c + 1
        self.tableWidget.resizeColumnsToContents()
        session.close()
        
    def __neuEintrag(self):
        #print("Enter __neuEintrag")
        self.ledArt.setEnabled(True)
        self.ledArt.setStyleSheet(ledStyleString)
        self.ledArt.setText("")   
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        self.modus = constants.MODUS_NEU
        
    def __save_data(self):
        #print("Enter __save_data: ", self.ledArt.text() + " " + str(len(self.ledArt.text())))
        session = utilities.createSession()
        if self.modus == constants.MODUS_NEU:
            if len(self.ledArt.text()) != 0:
                newArt = Art(aname = self.ledArt.text())
                session.add(newArt)
        elif self.modus == constants.MODUS_BEARBEITEN:
            #print("Modus Bearbeiten")
            fcontent = self.ledArt.text()
            session.query(Art).filter(Art.id_art == self.index).update({Art.aname:fcontent}, synchronize_session = False)
        elif self.modus == constants.MODUS_LOESCHEN:
            #print("Modus Löschen")
            session.query(Art).filter(Art.id_art==self.index).delete() 
        else:
            QMessageBox.information(self, "Information", "Keine Funktion gewählt")   
        utilities.closeSessionCommit(session)
        
    def __bearbeiteEintrag(self):
        #print("Enter __bearbeiteEintrag")
        self.modus = constants.MODUS_BEARBEITEN
        item1 = self.tableWidget.item(self.zeile, 1)
        self.ledArt.setText(str(item1.text()))        

    def __loescheEintrag(self):
        #print("Enter __loescheEintrag")
        self.modus = constants.MODUS_LOESCHEN
        
    def __item_Clicked(self):
        #print("Signal ItemSelectionChanged received, Item selected: ")
        self.zeile = self.tableWidget.selectedItems()[0].row()
        item0 = self.tableWidget.item(self.zeile, 0)
        self.index = int(item0.text())
        self.ledArt.setEnabled(True)
        self.ledArt.setStyleSheet(ledStyleString)
        self.__setButtonsTrue()

    def __Suchen(self):
        #print("btnSuchen start")
        session = utilities.createSession()
        c = 0
        for art in session.query(Art).filter(Art.aname.like("%"+self.ledArt.text()+"%")).order_by(Art.aname).all():
            #print("ID: ", art.id_art, "Art: ", art.art, "Created: ", art.create_time)
            self.tableWidget.setRowCount(c+1)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(str(art.id_art)))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(art.aname))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(str(art.create_time)))
            c = c + 1
        self.tableWidget.resizeColumnsToContents()
        session.close()
 
 

