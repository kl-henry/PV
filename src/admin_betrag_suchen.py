# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_adminbetrag_suchen.ui',
# licensing of 'ui_adminbetrag_suchen.ui' applies.
#
# Created: Mon May 20 10:37:00 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QDate
from sqlalchemy.orm import load_only
from sqlalchemy import and_
from stylestrings import gbStyleString, ledStyleString, dateeditStyleString
from __utilities import utilities
from Model_PV import Zahlung, Quelle, View_betrag_liste


class Ui_DiaadminBetragSuche(QDialog):
    def setupUi(self, DiaadminBetragSuche):
        self.zahlung_list = {}
        self.quelle_list = {}
        self.index_quelle = 0
        self.index_zahlung = 0
        self.conditions = []
        self.vonDate_changed = False
        self.bisDate_changed = False
        
        DiaadminBetragSuche.setObjectName("DiaadminBetragSuche")
        DiaadminBetragSuche.resize(674, 356)
        
        self.grpName = QtWidgets.QGroupBox(DiaadminBetragSuche)
        self.grpName.setGeometry(QtCore.QRect(20, 0, 291, 81))
        self.grpName.setStyleSheet(gbStyleString)
        self.grpName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.grpName.setObjectName("grpName")
        
        self.layoutWidget = QtWidgets.QWidget(self.grpName)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 251, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lblName = QtWidgets.QLabel(self.layoutWidget)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout.addWidget(self.lblName)
        
        self.ledName = QtWidgets.QLineEdit(self.layoutWidget)
        self.ledName.setReadOnly(False)
        self.ledName.setStyleSheet(ledStyleString)
        self.ledName.setObjectName("ledName")
        self.horizontalLayout.addWidget(self.ledName)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaadminBetragSuche)
        self.buttonBox.setGeometry(QtCore.QRect(300, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gbAnschrift = QtWidgets.QGroupBox(DiaadminBetragSuche)
        self.gbAnschrift.setGeometry(QtCore.QRect(20, 90, 621, 91))
        self.gbAnschrift.setStyleSheet(gbStyleString)
        self.gbAnschrift.setObjectName("gbAnschrift")
        
        self.layoutWidget1 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 20, 131, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.lblWo = QtWidgets.QLabel(self.layoutWidget1)
        self.lblWo.setObjectName("lblWo")
        self.horizontalLayout_4.addWidget(self.lblWo)
        
        self.cbZahlung = QtWidgets.QComboBox(self.layoutWidget1)
        self.cbZahlung.setObjectName("cbZahlung")
        self.horizontalLayout_4.addWidget(self.cbZahlung)
        
        self.layoutWidget2 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 181, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.lblQuelle = QtWidgets.QLabel(self.layoutWidget2)
        self.lblQuelle.setObjectName("lblQuelle")
        self.horizontalLayout_6.addWidget(self.lblQuelle)
        self.cbQuelle = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbQuelle.setObjectName("cbQuelle")
        self.horizontalLayout_6.addWidget(self.cbQuelle)
        
        self.layoutWidget_2 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget_2.setGeometry(QtCore.QRect(430, 20, 131, 28))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.lblVon = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblVon.setObjectName("lblVon")
        self.horizontalLayout_5.addWidget(self.lblVon)
        
        self.deVon = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.deVon.setCalendarPopup(True)
        self.deVon.setDate(QDate.currentDate())
        self.deVon.setStyleSheet(dateeditStyleString)
        self.deVon.setObjectName("deVon")
        self.horizontalLayout_5.addWidget(self.deVon)
        
        self.layoutWidget_4 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget_4.setGeometry(QtCore.QRect(430, 50, 131, 28))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        self.lblBis = QtWidgets.QLabel(self.layoutWidget_4)
        self.lblBis.setObjectName("lblBis")
        self.horizontalLayout_9.addWidget(self.lblBis)
        self.deBis = QtWidgets.QDateEdit(self.layoutWidget_4)
        self.deBis.setCalendarPopup(True)
        self.deBis.setStyleSheet(dateeditStyleString)
        self.deBis.setDate(QDate.currentDate())        
        self.deBis.setObjectName("deBis")
        self.horizontalLayout_9.addWidget(self.deBis)
        
        self.gbBetrag = QtWidgets.QGroupBox(DiaadminBetragSuche)
        self.gbBetrag.setGeometry(QtCore.QRect(20, 200, 621, 80))
        self.gbBetrag.setStyleSheet(gbStyleString)
        self.gbBetrag.setObjectName("gbBetrag")
        self.layoutWidget3 = QtWidgets.QWidget(self.gbBetrag)
        
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 40, 221, 28))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.lblBetragVon = QtWidgets.QLabel(self.layoutWidget3)
        self.lblBetragVon.setObjectName("lblBetragVon")
        self.horizontalLayout_7.addWidget(self.lblBetragVon)
        
        self.ledBetragVon = QtWidgets.QLineEdit(self.layoutWidget3)
        self.ledBetragVon.setObjectName("ledBetragVon")
        self.ledBetragVon.setStyleSheet(ledStyleString)
        self.horizontalLayout_7.addWidget(self.ledBetragVon)
        
        self.layoutWidget_3 = QtWidgets.QWidget(self.gbBetrag)
        self.layoutWidget_3.setGeometry(QtCore.QRect(320, 40, 221, 28))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        
        self.lblBetragBis = QtWidgets.QLabel(self.layoutWidget_3)
        self.lblBetragBis.setObjectName("lblBetragBis")
        self.horizontalLayout_8.addWidget(self.lblBetragBis)
        
        self.ledBetragBis = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.ledBetragBis.setObjectName("ledBetragBis")
        self.ledBetragBis.setStyleSheet(ledStyleString)
        self.horizontalLayout_8.addWidget(self.ledBetragBis)
        
        self.gbEA = QtWidgets.QGroupBox(DiaadminBetragSuche)
        self.gbEA.setGeometry(QtCore.QRect(520, 0, 116, 81))
        self.gbEA.setStyleSheet(gbStyleString)
        self.gbEA.setObjectName("gbEA")
        self.layoutWidget4 = QtWidgets.QWidget(self.gbEA)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 81, 56))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.rbAusgang = QtWidgets.QRadioButton(self.layoutWidget4)
        self.rbAusgang.setChecked(True)
        self.rbAusgang.setObjectName("rbAusgang")
        self.verticalLayout.addWidget(self.rbAusgang)
        
        self.rbEingang = QtWidgets.QRadioButton(self.layoutWidget4)
        self.rbEingang.setObjectName("rbEingang")
        self.verticalLayout.addWidget(self.rbEingang)

        self.retranslateUi(DiaadminBetragSuche)
        self.__populate_comboBox_Quelle()
        self.__populate_comboBox_Zahlung()
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DiaadminBetragSuche.accept)
        self.accepted.connect(self.__build_conditions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DiaadminBetragSuche.reject)
        self.cbQuelle.currentIndexChanged.connect(self.__cb_currentIndexChanged_quelle)
        self.cbZahlung.currentIndexChanged.connect(self.__cb_currentIndexChanged_zahlung)
        self.deVon.dateChanged.connect(self.__von_date_changed)
        self.deBis.dateChanged.connect(self.__bis_date_changed)

        QtCore.QMetaObject.connectSlotsByName(DiaadminBetragSuche)

        DiaadminBetragSuche.setTabOrder(self.ledName, self.ledBetragBis)
        
    def retranslateUi(self, DiaadminBetrag):
        DiaadminBetrag.setWindowTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Admin - Person", None, -1))
        self.grpName.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Name", None, -1))
        self.lblName.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Name:", None, -1))
        self.gbAnschrift.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Zahlung", None, -1))
        self.lblWo.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Wo:", None, -1))
        self.lblQuelle.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "wie bezahlt:", None, -1))
        self.lblVon.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Von:", None, -1))
        self.lblBis.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Bis:", None, -1))
        self.gbBetrag.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Betrag", None, -1))
        self.lblBetragVon.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Betrag von:", None, -1))
        self.lblBetragBis.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Betrag bis:", None, -1))
        self.gbEA.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "E/A", None, -1))
        self.rbAusgang.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Ausgang", None, -1))
        self.rbEingang.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Eingang", None, -1))

    def __von_date_changed(self):
        self.vonDate_changed = True
    def __bis_date_changed(self):
        self.bisDate_changed = True
                
    def __populate_comboBox_Quelle(self):
        session = utilities.createSession() 
        self.cbQuelle.addItem("",0)
        for quelle in session.query(Quelle).order_by(Quelle.qname).options(load_only("id_quelle","qname")):
            #print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbQuelle.addItem(quelle.qname,quelle.id_quelle)
            self.quelle_list[quelle.qname] = quelle.id_quelle
        session.close()
        
    def __populate_comboBox_Zahlung(self):
        session = utilities.createSession() 
        self.cbZahlung.addItem("",0)
        for zahlung in session.query(Zahlung).order_by(Zahlung.zname).options(load_only("id_zahlung","zname")):
            #print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbZahlung.addItem(zahlung.zname,zahlung.id_zahlung)
            self.zahlung_list[zahlung.zname] = zahlung.id_zahlung
        session.close()
 
    def __cb_currentIndexChanged_quelle(self, idx):
        #print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        self.index_quelle = self.quelle_list[self.cbQuelle.currentText()]
        #print("IndexChanged idx: ", self.index, " Index To Update: ", self.index_to_insert)
    
    def __cb_currentIndexChanged_zahlung(self, idx):
        #print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        self.index_zahlung = self.zahlung_list[self.cbZahlung.currentText()]
        #print("IndexChanged idx: ", self.index, " Index To Update: ", self.index_to_insert)
        
    def __date_changed(self):
        self.dateEdit.dateChanged.connect(self.start_date_dateedit)
        
    def __build_conditions(self):
        if len(self.ledName.text()) !=0:
            self.conditions.append(View_betrag_liste.Name.like\
                                        ("%"+self.ledName.text()+"%"))
        if self.index_quelle != 0:
            self.conditions.append(View_betrag_liste.q_id == self.index_quelle)
        if self.index_zahlung != 0:
            self.conditions.append(View_betrag_liste.z_id == self.index_zahlung)
        if self.rbAusgang.isChecked():
            self.conditions.append(View_betrag_liste.EA == "Ausgang")
        else:
            self.conditions.append(View_betrag_liste.EA == "Eingang")
        if (len(self.ledBetragVon.text()) != 0) and (len(self.ledBetragBis.text()) == 0):
            betragVon = float(self.ledBetragVon.text().replace(',', '.'))
            self.conditions.append(View_betrag_liste.betrag == betragVon)
        if (len(self.ledBetragVon.text()) == 0) and (len(self.ledBetragBis.text()) != 0):
            betragBis = float(self.ledBetragBis.text().replace(',', '.'))
            self.conditions.append(View_betrag_liste.betrag == betragBis)
        if (len(self.ledBetragVon.text()) != 0) and (len(self.ledBetragBis.text()) != 0):
            betragVon = float(self.ledBetragVon.text().replace(',', '.'))
            betragBis = float(self.ledBetragBis.text().replace(',', '.'))
            self.conditions.append(and_(View_betrag_liste.betrag >= betragVon, View_betrag_liste.betrag <= betragBis))
        if self.vonDate_changed and self.bisDate_changed:
            self.conditions.append(and_(View_betrag_liste.datum >= self.deVon.date().toString("yyyy-MM-dd"),\
                                        View_betrag_liste.datum <= self.deBis.date().toString("yyyy-MM-dd")))
        else:
            if self.vonDate_changed:
                self.conditions.append(View_betrag_liste.datum == self.deVon.date().toString("yyyy-MM-dd"))
            if self.bisDate_changed:
                self.conditions.append(View_betrag_liste.datum == self.deBis.date().toString("yyyy-MM-dd"))
#             print("build_conditions, date von: ", self.deVon.date().toString("yyyy-MM-dd"))
#             print("build_conditions, date bis: ", self.deBis.date().toString("yyyy-MM-dd"))
#         for condition in self.conditions:
#             print("Betrag suchen, Conditions: ", condition)


