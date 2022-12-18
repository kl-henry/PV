# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_adminperson.ui',
# licensing of 'ui_adminperson.ui' applies.
#
# Created: Mon Apr 22 09:28:07 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from __utilities import utilities
from stylestrings import ledStyleString, gbStyleString, ledStyleStringDisabled
import constants
from Model_PV import Anrede, Kontakt, View_kontakt_liste
from admin_person import Ui_DiaadminPerson
from sqlalchemy.orm import load_only

class Ui_DiaadminKontakt(QDialog):
    def setupUi(self, DiaadminKontakt):
        self.anrede_list = {}
        self.modus = constants.MODUS_NULL
        DiaadminKontakt.setObjectName("DiaadminKontakt")
        DiaadminKontakt.resize(849, 633)
        self.layoutWidget = QtWidgets.QWidget(DiaadminKontakt)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 540, 254, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.btnNeu = QtWidgets.QPushButton(self.layoutWidget)
        self.btnNeu.setObjectName("btnNeu")
        self.horizontalLayout_2.addWidget(self.btnNeu)
        
        self.btnBearbeiten = QtWidgets.QPushButton(self.layoutWidget)
        self.btnBearbeiten.setEnabled(True)
        self.btnBearbeiten.setAutoDefault(False)
        self.btnBearbeiten.setObjectName("btnBearbeiten")
        
        self.horizontalLayout_2.addWidget(self.btnBearbeiten)
        self.btnLoeschen = QtWidgets.QPushButton(self.layoutWidget)
        self.btnLoeschen.setObjectName("btnLoeschen")
        self.horizontalLayout_2.addWidget(self.btnLoeschen)
        
        self.tableWidget = QtWidgets.QTableWidget(DiaadminKontakt)
        self.tableWidget.setGeometry(QtCore.QRect(20, 300, 801, 231))
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(10)
        self.columnLabels = ["id","Art","Name","PLZ","Ort","Strasse","Email","Telefon","Mobil"]
        self.tableWidget.setHorizontalHeaderLabels(self.columnLabels)
        
        self.grpName = QtWidgets.QGroupBox(DiaadminKontakt)
        self.grpName.setGeometry(QtCore.QRect(20, 0, 621, 81))
        self.grpName.setStyleSheet(gbStyleString)
        self.grpName.setObjectName("grpName")
        
        self.layoutWidget1 = QtWidgets.QWidget(self.grpName)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 538, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lblAnrede = QtWidgets.QLabel(self.layoutWidget1)
        self.lblAnrede.setObjectName("lblAnrede")
        self.horizontalLayout.addWidget(self.lblAnrede)
        
        self.cbAnrede = QtWidgets.QComboBox(self.layoutWidget1)
        self.cbAnrede.setObjectName("cbAnrede")
        self.cbAnrede.setEnabled(False)
        self.horizontalLayout.addWidget(self.cbAnrede)
        
        self.lblVorname = QtWidgets.QLabel(self.layoutWidget1)
        self.lblVorname.setObjectName("lblVorname")
        self.horizontalLayout.addWidget(self.lblVorname)
        
        self.ledVorname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ledVorname.setStyleSheet(ledStyleStringDisabled)
        self.ledVorname.setObjectName("ledVorname")
        self.ledVorname.setReadOnly(True)
        self.horizontalLayout.addWidget(self.ledVorname)
        
        self.lblNachname = QtWidgets.QLabel(self.layoutWidget1)
        self.lblNachname.setObjectName("lblNachname")
        self.horizontalLayout.addWidget(self.lblNachname)

        self.ledNachname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ledNachname.setStyleSheet(ledStyleStringDisabled)
        self.ledNachname.setObjectName("ledNachname")
        self.ledNachname.setReadOnly(True)
        self.horizontalLayout.addWidget(self.ledNachname)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaadminKontakt)
        self.buttonBox.setGeometry(QtCore.QRect(480, 590, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gbAnschrift = QtWidgets.QGroupBox(DiaadminKontakt)
        self.gbAnschrift.setGeometry(QtCore.QRect(20, 100, 621, 80))
        self.gbAnschrift.setStyleSheet(gbStyleString)
        self.gbAnschrift.setObjectName("gbAnschrift")
        
        self.layoutWidget2 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget2.setGeometry(QtCore.QRect(460, 40, 157, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.lblOrt = QtWidgets.QLabel(self.layoutWidget2)
        self.lblOrt.setObjectName("lblOrt")
        self.horizontalLayout_5.addWidget(self.lblOrt)
        
        self.ledOrt = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ledOrt.setStyleSheet(ledStyleString)
        self.ledOrt.setObjectName("ledOrt")
        self.horizontalLayout_5.addWidget(self.ledOrt)
        
        self.layoutWidget3 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget3.setGeometry(QtCore.QRect(350, 40, 91, 28))
        self.layoutWidget3.setObjectName("layoutWidget3")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.lblPLZ = QtWidgets.QLabel(self.layoutWidget3)
        self.lblPLZ.setObjectName("lblPLZ")
        self.horizontalLayout_3.addWidget(self.lblPLZ)
        
        self.ledPLZ = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ledPLZ.setStyleSheet(ledStyleString)
        self.ledPLZ.setObjectName("ledPLZ")
        self.horizontalLayout_3.addWidget(self.ledPLZ)
        
        self.layoutWidget4 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget4.setGeometry(QtCore.QRect(200, 40, 101, 28))
        self.layoutWidget4.setObjectName("layoutWidget4")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.lblHausnr = QtWidgets.QLabel(self.layoutWidget4)
        self.lblHausnr.setObjectName("lblHausnr")
        self.horizontalLayout_4.addWidget(self.lblHausnr)
        
        self.ledHausnr = QtWidgets.QLineEdit(self.layoutWidget4)
        self.ledHausnr.setStyleSheet(ledStyleString)
        self.ledHausnr.setObjectName("ledHausnr")
        self.horizontalLayout_4.addWidget(self.ledHausnr)
        
        self.layoutWidget5 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 40, 181, 28))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.lblStrasse = QtWidgets.QLabel(self.layoutWidget5)
        self.lblStrasse.setObjectName("lblStrasse")
        self.horizontalLayout_6.addWidget(self.lblStrasse)
        
        self.ledStrasse = QtWidgets.QLineEdit(self.layoutWidget5)
        self.ledStrasse.setStyleSheet(ledStyleString)
        self.ledStrasse.setObjectName("ledStrasse")
        self.horizontalLayout_6.addWidget(self.ledStrasse)
        
        self.gbKontakte = QtWidgets.QGroupBox(DiaadminKontakt)
        self.gbKontakte.setGeometry(QtCore.QRect(20, 200, 621, 80))
        self.gbKontakte.setStyleSheet(gbStyleString)
        self.gbKontakte.setObjectName("gbKontakte")
        self.widget = QtWidgets.QWidget(self.gbKontakte)
        self.widget.setGeometry(QtCore.QRect(10, 40, 531, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.lblEmail = QtWidgets.QLabel(self.widget)
        self.lblEmail.setObjectName("lblEmail")
        self.horizontalLayout_7.addWidget(self.lblEmail)
        
        self.ledEmail = QtWidgets.QLineEdit(self.widget)
        self.ledEmail.setStyleSheet(ledStyleString)
        self.ledEmail.setObjectName("ledEmail")
        self.horizontalLayout_7.addWidget(self.ledEmail)
        
        self.lblTelefon = QtWidgets.QLabel(self.widget)
        self.lblTelefon.setObjectName("lblTelefon")
        self.horizontalLayout_7.addWidget(self.lblTelefon)
        
        self.ledTelefon = QtWidgets.QLineEdit(self.widget)
        self.ledTelefon.setStyleSheet(ledStyleString)
        self.ledTelefon.setObjectName("ledTelefon")
        self.horizontalLayout_7.addWidget(self.ledTelefon)
        
        self.lblMobil = QtWidgets.QLabel(self.widget)
        self.lblMobil.setObjectName("lblMobil")
        self.horizontalLayout_7.addWidget(self.lblMobil)
        
        self.ledMobil = QtWidgets.QLineEdit(self.widget)
        self.ledMobil.setStyleSheet(ledStyleString)
        self.ledMobil.setObjectName("ledMobil")
        self.horizontalLayout_7.addWidget(self.ledMobil)
        
        self.btnSuchen = QtWidgets.QPushButton(DiaadminKontakt)
        self.btnSuchen.setGeometry(QtCore.QRect(741, 250, 80, 26))
        self.btnSuchen.setObjectName("btnSuchen")
        
        self.populate_comboBox()
        self.__populate_tableview()
        self.retranslateUi(DiaadminKontakt)
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DiaadminKontakt.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DiaadminKontakt.reject)
        QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.clicked_btnNeu)
        QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.clicked_btnBearbeiten)
        QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.clicked_btnLoeschen)
        QtCore.QObject.connect(self.btnSuchen, QtCore.SIGNAL("clicked()"), self.__btnSuchen)
        self.cbAnrede.currentIndexChanged.connect(self.__cb_currentIndexChanged)
        self.tableWidget.itemSelectionChanged.connect(self.__item_Clicked)
        QtCore.QMetaObject.connectSlotsByName(DiaadminKontakt)

        DiaadminKontakt.setTabOrder(self.ledStrasse, self.ledHausnr)
        DiaadminKontakt.setTabOrder(self.ledHausnr, self.ledPLZ)
        DiaadminKontakt.setTabOrder(self.ledPLZ, self.ledOrt)
        DiaadminKontakt.setTabOrder(self.ledOrt, self.ledEmail)
        DiaadminKontakt.setTabOrder(self.ledEmail, self.ledTelefon)
        DiaadminKontakt.setTabOrder(self.ledTelefon, self.ledMobil)
        DiaadminKontakt.setTabOrder(self.ledMobil, self.btnNeu)
        DiaadminKontakt.setTabOrder(self.btnNeu, self.btnBearbeiten)
        DiaadminKontakt.setTabOrder(self.btnBearbeiten, self.btnLoeschen)
        DiaadminKontakt.setTabOrder(self.btnLoeschen, self.btnSuchen)
        DiaadminKontakt.setTabOrder(self.btnSuchen, self.tableWidget)
        self.btnNeu.setDefault(True)


    def retranslateUi(self, DiaadminKontakt):
        DiaadminKontakt.setWindowTitle(QtWidgets.QApplication.translate("DiaadminKontakt", "Admin - Person", None, -1))
        self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Neu", None, -1))
        self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Bearbeiten", None, -1))
        self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Löschen", None, -1))
        self.grpName.setTitle(QtWidgets.QApplication.translate("DiaadminKontakt", "Name", None, -1))
        self.lblAnrede.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Anrede:", None, -1))
        self.lblVorname.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Vorname:", None, -1))
        self.lblNachname.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Nachname:", None, -1))
        self.gbAnschrift.setTitle(QtWidgets.QApplication.translate("DiaadminKontakt", "Anschrift", None, -1))
        self.lblOrt.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Ort:", None, -1))
        self.lblPLZ.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "PLZ:", None, -1))
        self.lblHausnr.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Hausnr.:", None, -1))
        self.lblStrasse.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Strasse:", None, -1))
        self.gbKontakte.setTitle(QtWidgets.QApplication.translate("DiaadminKontakt", "Kontakte", None, -1))
        self.lblEmail.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Email:", None, -1))
        self.lblTelefon.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Telefon:", None, -1))
        self.lblMobil.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "Mobil:", None, -1))
        self.btnSuchen.setText(QtWidgets.QApplication.translate("DiaadminKontakt", "&Suchen", None, -1))

    def __setButtonsTrue(self):
        self.btnBearbeiten.setEnabled(True)
        self.btnLoeschen.setEnabled(True)
        
    def __setButtonsFalse(self):
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
 
    def populate_comboBox(self):
        session = utilities.createSession() 
        self.cbAnrede.addItem("",0)
        for anrede in session.query(Anrede).options(load_only("id_anrede","anrede")):
            #print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbAnrede.addItem(anrede.anrede,anrede.id_anrede)
            self.anrede_list[anrede.anrede] = anrede.id_anrede
        session.close()

    def __populate_tableview(self):
        #print("Enter __populate_tableview")
        session = utilities.createSession()
        c = 0
        for kontakt in session.query(View_kontakt_liste):
            #print("ID: ", kontakt.anrede, "Art: ", kontakt.plz, "Created: ", kontakt.id_person)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(str(kontakt.id_kontakt)))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(kontakt.anrede))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(kontakt.Name))
            self.tableWidget.setItem(c, 3, QTableWidgetItem(kontakt.plz))
            self.tableWidget.setItem(c, 4, QTableWidgetItem(kontakt.strasse))
            self.tableWidget.setItem(c, 5, QTableWidgetItem(kontakt.ort))
            self.tableWidget.setItem(c, 6, QTableWidgetItem(kontakt.email))
            self.tableWidget.setItem(c, 7, QTableWidgetItem(kontakt.telefon))
            self.tableWidget.setItem(c, 8, QTableWidgetItem(kontakt.mobil))
            c = c + 1
        self.tableWidget.resizeColumnsToContents()
        session.close()
        
    def __item_Clicked(self):
        #print("Signal ItemSelectionChanged received, Item selected: ")
        self.__setButtonsTrue()
        #print("Signal ItemSelectionChanged, Index selected: ", str(self.index_to_use))
   
    def __cb_currentIndexChanged(self, idx):
        #print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        #print("IndexChanged idx: ", self.index, " Index To Update: ", self.index_to_insert)
    def __setNameTrue(self):
        self.cbAnrede.setEnabled(False)
        self.ledVorname.setStyleSheet(ledStyleStringDisabled)
        self.ledVorname.setReadOnly(True)
        self.ledNachname.setStyleSheet(ledStyleStringDisabled)
        self.ledNachname.setReadOnly(True)

    def clicked_btnNeu(self):
        #print("clicked_btnNeu start")
        self.modus = constants.MODUS_NEU
        self.__setNameTrue()
        self.DiaadminPerson = Ui_DiaadminPerson()
        self.DiaadminPerson.setupUi(self.DiaadminPerson, False)
        if self.DiaadminPerson.exec_():
            self.cbAnrede.setCurrentText(self.DiaadminPerson.cbAnrede.currentText())
            self.ledVorname.setText(self.DiaadminPerson.ledVorname.text())
            self.ledNachname.setText(self.DiaadminPerson.ledNachname.text())
            self.index_anrede = self.DiaadminPerson.index_to_use
          
    def clicked_btnBearbeiten(self):
        #print("clicked_btnBearbeiten start")
        self.modus = constants.MODUS_BEARBEITEN
        self.zeile = self.tableWidget.selectedItems()[0].row()
        item0 = self.tableWidget.item(self.zeile, 0)
        self.index_to_use = int(item0.text())
        item1 = self.tableWidget.item(self.zeile,1)
        item2 = self.tableWidget.item(self.zeile,2)
        self.ledNachname.setText(item2.text().split()[1])
        self.ledVorname.setText(item2.text().split()[0])
        self.cbAnrede.setCurrentText(str(item1.text()));
        item3 = self.tableWidget.item(self.zeile,3)
        self.ledPLZ.setText(item3.text())
        if len(self.tableWidget.item(self.zeile,4).text()) != 0: 
            self.ledStrasse.setText(self.tableWidget.item(self.zeile,4).text().split()[0])
            self.ledHausnr.setText(self.tableWidget.item(self.zeile,4).text().split()[1])
        item5 = self.tableWidget.item(self.zeile,5)
        self.ledOrt.setText(item5.text())
        item6 = self.tableWidget.item(self.zeile,6)
        self.ledEmail.setText(item6.text())
        item7 = self.tableWidget.item(self.zeile,7)
        self.ledTelefon.setText(item7.text())
        item8 = self.tableWidget.item(self.zeile,8)
        self.ledMobil.setText(item8.text())

    def clicked_btnLoeschen(self):
        #print("clicked_btnLoeschen start")
        self.modus = constants.MODUS_LOESCHEN

    def __save_data(self):
        #print("Enter __save_data: ", str(self.index_to_use))
        session = utilities.createSession()
        if self.modus == constants.MODUS_NEU:
            if len(self.ledPLZ.text()) != 0:
                newKontakt = Kontakt(strasse = self.ledStrasse.text(), hausnr = self.ledHausnr.text(),\
                                   plz = self.ledPLZ.text(), ort = self.ledOrt.text(),\
                                   email = self.ledEmail.text(), telefon = self.ledTelefon.text(), mobil = self.ledMobil.text())
                session.add(newKontakt)
        elif self.modus == constants.MODUS_BEARBEITEN:
            print("Modus Bearbeiten, index_kontakt: ", self.index_to_use, "len(Ort): ", len(self.ledOrt.text()))
            session.query(Kontakt).filter(Kontakt.id_kontakt == self.index_to_use).update(\
                                        {Kontakt.ort:self.ledOrt.text(),\
                                         Kontakt.plz:self.ledPLZ.text(),\
                                         Kontakt.strasse:self.ledStrasse.text(),\
                                         Kontakt.hausnr:self.ledHausnr.text(),\
                                         Kontakt.email:self.ledEmail.text(),\
                                         Kontakt.telefon:self.ledTelefon.text(),\
                                         Kontakt.mobil:self.ledMobil.text(),\
                                         }, synchronize_session = False)
        elif self.modus == constants.MODUS_LOESCHEN:
            #print("Modus Löschen", self.index_to_use)
            session.query(Kontakt).filter(Kontakt.id_kontakt==self.index_to_use).delete()    
        utilities.closeSessionCommit(session)
 
    def __btnSuchen(self):
        #print("btnSuchen start")
        QMessageBox.information(self, "Information", "Funktion ist in Arbeit")
