# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_adminbetrag.ui',
# licensing of 'ui_adminbetrag.ui' applies.
#
# Created: Sat Apr 27 13:30:49 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from sqlalchemy.orm import load_only
from sqlalchemy import and_
from Model_PV import Zahlung, Quelle, Betrag, View_betrag_liste, View_eingang_liste, Anrede
from admin_person import Ui_DiaadminPerson
from admin_pos import Ui_DiaadminPos
from admin_betrag_suchen import Ui_DiaadminBetragSuche
import constants
from __utilities import utilities
from stylestrings import ledStyleString, gbStyleString, ledStyleStringDisabled, \
    dateeditStyleString
from PySide2.QtCore import QDate, QSize
import datetime


class Ui_DiaadminBetrag(QDialog):

    def setupUi(self, DiaadminBetrag):
        self.modus = constants.MODUS_NULL
        self.zahlung_list = {}
        self.quelle_list = {}
        self.anrede_list = {}
        # print("Enter DiaAdminBetrag")
        DiaadminBetrag.setObjectName("DiaadminBetrag")
        DiaadminBetrag.resize(849, 633)
        self.layoutWidget = QtWidgets.QWidget(DiaadminBetrag)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 540, 400, 28))
        self.layoutWidget.setObjectName("layoutWidget")
 
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.btnNeu = QtWidgets.QPushButton(self.layoutWidget)
        self.btnNeu.setObjectName("btnNeu")
        self.horizontalLayout_2.addWidget(self.btnNeu)
        
        self.btnBearbeiten = QtWidgets.QPushButton(self.layoutWidget)
        self.btnBearbeiten.setObjectName("btnBearbeiten")
        self.horizontalLayout_2.addWidget(self.btnBearbeiten)

        self.btnLoeschen = QtWidgets.QPushButton(self.layoutWidget)
        self.btnLoeschen.setObjectName("btnLoeschen")
        self.horizontalLayout_2.addWidget(self.btnLoeschen)
        
        self.btnPosition = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPosition.setObjectName("btnPosition")
        self.horizontalLayout_2.addWidget(self.btnPosition)

        self.twBetrag = QtWidgets.QTableWidget(DiaadminBetrag)
        self.twBetrag.setGeometry(QtCore.QRect(20, 300, 801, 231))
        self.twBetrag.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twBetrag.verticalHeader().setVisible(False)
        self.twBetrag.verticalHeader().setHighlightSections(False)
        self.twBetrag.setObjectName("twBetrag")
        self.twBetrag.setColumnCount(9)
        self.twBetrag.setRowCount(0)
        self.columnLabels = ["id", "Anrede", "E/A", "Name", "Betrag", "Datum", "Bemerkung", "Wo", "Zahlungsart"]
        self.twBetrag.setHorizontalHeaderLabels(self.columnLabels)
        
        self.grpName = QtWidgets.QGroupBox(DiaadminBetrag)
        self.grpName.setGeometry(QtCore.QRect(20, 0, 621, 81))
        self.grpName.setStyleSheet(gbStyleString)
        self.grpName.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
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
        self.ledVorname.setReadOnly(True)
        self.ledVorname.setObjectName("ledVorname")
        self.ledVorname.setStyleSheet(ledStyleStringDisabled)
        self.horizontalLayout.addWidget(self.ledVorname)
        
        self.lblNachname = QtWidgets.QLabel(self.layoutWidget1)
        self.lblNachname.setObjectName("lblNachname")
        self.horizontalLayout.addWidget(self.lblNachname)
        
        self.ledNachname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ledNachname.setReadOnly(True)
        self.ledNachname.setObjectName("ledNachname")
        self.ledNachname.setStyleSheet(ledStyleStringDisabled)
        self.horizontalLayout.addWidget(self.ledNachname)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaadminBetrag)
        self.buttonBox.setGeometry(QtCore.QRect(480, 590, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gbAnschrift = QtWidgets.QGroupBox(DiaadminBetrag)
        self.gbAnschrift.setGeometry(QtCore.QRect(20, 100, 621, 80))
        self.gbAnschrift.setStyleSheet(gbStyleString)
        self.gbAnschrift.setObjectName("gbAnschrift")
        self.layoutWidget2 = QtWidgets.QWidget(self.gbAnschrift)
        
        self.layoutWidget2.setGeometry(QtCore.QRect(230, 40, 131, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.lblWo = QtWidgets.QLabel(self.layoutWidget2)
        self.lblWo.setObjectName("lblWo")
        self.horizontalLayout_4.addWidget(self.lblWo)
        
        self.cbZahlung = QtWidgets.QComboBox(self.layoutWidget2)
        self.cbZahlung.setObjectName("cbZahlung")
        self.horizontalLayout_4.addWidget(self.cbZahlung)

        self.layoutWidget3 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 40, 181, 28))
        self.layoutWidget3.setObjectName("layoutWidget3")
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.lblQuelle = QtWidgets.QLabel(self.layoutWidget3)
        self.lblQuelle.setObjectName("lblQuelle")
        self.horizontalLayout_6.addWidget(self.lblQuelle)
        
        self.cbQuelle = QtWidgets.QComboBox(self.layoutWidget3)
        self.cbQuelle.setObjectName("cbQuelle")
        self.horizontalLayout_6.addWidget(self.cbQuelle)
        
        self.layoutWidget_2 = QtWidgets.QWidget(self.gbAnschrift)
        self.layoutWidget_2.setGeometry(QtCore.QRect(430, 40, 131, 28))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.lblWann = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblWann.setObjectName("lblWann")
        self.horizontalLayout_5.addWidget(self.lblWann)
        
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setStyleSheet(dateeditStyleString)
        self.dateEdit.setDisplayFormat("dd.MM.yyyy")
        self.dateEdit.setMinimumSize(QSize(90, 12))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.dateEdit)
        
        self.gbKontakte = QtWidgets.QGroupBox(DiaadminBetrag)
        self.gbKontakte.setGeometry(QtCore.QRect(20, 200, 621, 80))
        self.gbKontakte.setStyleSheet(gbStyleString)
        self.gbKontakte.setObjectName("gbKontakte")
        self.layoutWidget4 = QtWidgets.QWidget(self.gbKontakte)
        
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 40, 591, 28))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.lblBetrag = QtWidgets.QLabel(self.layoutWidget4)
        self.lblBetrag.setObjectName("lblBetrag")
        self.horizontalLayout_7.addWidget(self.lblBetrag)
        
        self.ledBetrag = QtWidgets.QLineEdit(self.layoutWidget4)
        self.ledBetrag.setStyleSheet(ledStyleString)
        self.ledBetrag.setObjectName("ledBetrag")
        self.horizontalLayout_7.addWidget(self.ledBetrag)
        
        self.lblBemerkung = QtWidgets.QLabel(self.layoutWidget4)
        self.lblBemerkung.setObjectName("lblBemerkung")
        self.horizontalLayout_7.addWidget(self.lblBemerkung)
        
        self.ledBemerkung = QtWidgets.QLineEdit(self.layoutWidget4)
        self.ledBemerkung.setStyleSheet(ledStyleString)
        self.ledBemerkung.setObjectName("ledBemerkung")
        self.horizontalLayout_7.addWidget(self.ledBemerkung)
        
        self.btnSuchen = QtWidgets.QPushButton(DiaadminBetrag)
        self.btnSuchen.setGeometry(QtCore.QRect(741, 250, 80, 26))
        self.btnSuchen.setObjectName("btnSuchen")

        self.btnSpeichern = QtWidgets.QPushButton(DiaadminBetrag)
        self.btnSpeichern.setGeometry(QtCore.QRect(740, 540, 80, 26))
        self.btnSpeichern.setObjectName("btnSpeichern")
        
        self.gbEA = QtWidgets.QGroupBox(DiaadminBetrag)
        self.gbEA.setGeometry(QtCore.QRect(680, 100, 116, 81))
        self.gbEA.setStyleSheet(gbStyleString)
        self.gbEA.setObjectName("gbEA")
        self.widget = QtWidgets.QWidget(self.gbEA)
        self.widget.setGeometry(QtCore.QRect(10, 20, 81, 56))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbAusgang = QtWidgets.QRadioButton(self.widget)
        self.rbAusgang.setChecked(True)
        self.rbAusgang.setObjectName("rbAusgang")
        self.verticalLayout.addWidget(self.rbAusgang)
        self.rbEingang = QtWidgets.QRadioButton(self.widget)
        self.rbEingang.setObjectName("rbEingang")
        self.verticalLayout.addWidget(self.rbEingang)

        self.retranslateUi(DiaadminBetrag)
        self.__populate_tableview()
        self.__populate_comboBox_Quelle()
        self.__populate_comboBox_Zahlung()
        self.__populate_comboBox_Anrede()
        self.__setButtonsFalse()
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DiaadminBetrag.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DiaadminBetrag.reject)
        QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.clicked_btnNeu)
        QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.clicked_btnBearbeiten)
        QtCore.QObject.connect(self.btnPosition, QtCore.SIGNAL("clicked()"), self.clicked_position_bearbeiten)
        QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.clicked_btnLoeschen)
        QtCore.QObject.connect(self.btnSuchen, QtCore.SIGNAL("clicked()"), self.__btnSuchen)
        self.cbQuelle.activated.connect(self.__cb_currentIndexChanged_quelle)
        self.cbZahlung.activated.connect(self.__cb_currentIndexChanged_zahlung)
        QtCore.QObject.connect(self.btnSpeichern, QtCore.SIGNAL("clicked()"), self.clicked_btnspeichern)
        self.twBetrag.itemClicked.connect(self.__item_Clicked)
        self.rbAusgang.toggled.connect(self.__rbEA_btnToggled)
        self.rbEingang.toggled.connect(self.__rbEA_btnToggled)

        QtCore.QMetaObject.connectSlotsByName(DiaadminBetrag)
        
        DiaadminBetrag.setTabOrder(self.ledVorname, self.ledNachname)
        DiaadminBetrag.setTabOrder(self.ledNachname, self.ledBetrag)
        DiaadminBetrag.setTabOrder(self.ledBetrag, self.ledBemerkung)
        DiaadminBetrag.setTabOrder(self.ledBemerkung, self.btnNeu)
        DiaadminBetrag.setTabOrder(self.btnNeu, self.btnBearbeiten)
        DiaadminBetrag.setTabOrder(self.btnBearbeiten, self.btnLoeschen)
        DiaadminBetrag.setTabOrder(self.btnLoeschen, self.btnSuchen)
        DiaadminBetrag.setTabOrder(self.btnSuchen, self.twBetrag)
        DiaadminBetrag.setTabOrder(self.btnSpeichern, self.twBetrag)

    def retranslateUi(self, DiaadminBetrag):
        DiaadminBetrag.setWindowTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Admin - Betrag", None, -1))
        self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Neu", None, -1))
        self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Bearbeiten", None, -1))
        self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Löschen", None, -1))
        self.btnPosition.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Pos. bearbeiten", None, -1))
        self.grpName.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Name", None, -1))
        self.lblAnrede.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Anrede:", None, -1))
        self.lblVorname.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Vorname:", None, -1))
        self.lblNachname.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Nachname:", None, -1))
        self.gbAnschrift.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Zahlung", None, -1))
        self.lblWo.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Wo:", None, -1))
        self.lblQuelle.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "wie bezahlt:", None, -1))
        self.lblWann.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Wann:", None, -1))
        self.gbKontakte.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "Betrag", None, -1))
        self.lblBetrag.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Betrag(ges):", None, -1))
        self.lblBemerkung.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Bemerkung:", None, -1))
        self.btnSuchen.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "&Suchen", None, -1))
        self.btnSpeichern.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Speichern", None, -1))
        self.gbEA.setTitle(QtWidgets.QApplication.translate("DiaadminBetrag", "E/A", None, -1))
        self.rbAusgang.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Ausgang", None, -1))
        self.rbEingang.setText(QtWidgets.QApplication.translate("DiaadminBetrag", "Eingang", None, -1))

    def __setButtonsTrue(self):
        self.btnBearbeiten.setEnabled(True)
        self.btnLoeschen.setEnabled(True)
        self.btnPosition.setEnabled(True)
        
    def __setButtonsFalse(self):
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        self.btnPosition.setEnabled(False)

    def __fill_cells(self, c, betrag):
        self.twBetrag.setItem(c, 0, QTableWidgetItem(str(betrag.id_betrag)))
        self.twBetrag.setItem(c, 1, QTableWidgetItem(betrag.EA))
        self.twBetrag.setItem(c, 2, QTableWidgetItem(betrag.anrede))
        self.twBetrag.setItem(c, 3, QTableWidgetItem(betrag.Name))
        self.twBetrag.setItem(c, 4, QTableWidgetItem(str(betrag.betrag)))
        self.twBetrag.setItem(c, 5, QTableWidgetItem((betrag.datum).strftime("%d.%m.%Y")))
        self.twBetrag.setItem(c, 6, QTableWidgetItem(str(betrag.bemerkung)))
        self.twBetrag.setItem(c, 7, QTableWidgetItem(str(betrag.zname)))
        self.twBetrag.setItem(c, 8, QTableWidgetItem(str(betrag.qname)))

    def __populate_tableview(self):
        # print("Enter __populate_tableview")
        self.twBetrag.setRowCount(0)
        # print("__populate_tableview: set RowCount = 0")
        session = utilities.createSession()
        c = 0
        if session.query(View_betrag_liste).count() > 0:
            if self.rbAusgang.isChecked():
                for betrag in session.query(View_betrag_liste).order_by(View_betrag_liste.datum.desc()):
                    # print("ID: ", art.id_art, "Art: ", art.art, "Created: ", art.create_time)
                    self.twBetrag.setRowCount(c + 1)
                    self.__fill_cells(c, betrag)
                    c = c + 1
            else:
                for betrag in session.query(View_eingang_liste).order_by(View_eingang_liste.datum.desc()):
                    # print("ID: ",str(betrag.id_betrag), "Betrag: ", str(betrag.id_betrag), "EA: ", betrag.EA)
                    self.twBetrag.setRowCount(c + 1)
                    self.__fill_cells(c, betrag)
                    c = c + 1            
                    self.twBetrag.resizeColumnsToContents()
        session.close()
        self.twBetrag.clearSelection()
        
    def __cb_currentIndexChanged_quelle(self, idx):
        # print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        self.index_quelle = self.quelle_list[self.cbQuelle.currentText()]

        # print("IndexChanged idx: ", self.index, " Index To Update: ", self.index_to_insert)
    def __cb_currentIndexChanged_zahlung(self, idx):
        # print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        self.index_zahlung = self.zahlung_list[self.cbZahlung.currentText()]

        # print("IndexChanged idx: ", self.index, " Index To Update: ", self.index_to_insert)
    def __cb_currentIndexChanged_anrede(self, idx):
        # print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        self.index_anrede = self.zahlung_list[self.cbAnrede.currentText()]
        
    def __populate_comboBox_Zahlung(self):
        session = utilities.createSession() 
        self.cbZahlung.addItem("", 0)
        for zahlung in session.query(Zahlung).order_by(Zahlung.zname).options(load_only("id_zahlung", "zname")):
            # print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbZahlung.addItem(zahlung.zname, zahlung.id_zahlung)
            self.zahlung_list[zahlung.zname] = zahlung.id_zahlung
        session.close()

    def __populate_comboBox_Quelle(self):
        session = utilities.createSession() 
        self.cbQuelle.addItem("", 0)
        for quelle in session.query(Quelle).order_by(Quelle.qname).options(load_only("id_quelle", "qname")):
            # print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbQuelle.addItem(quelle.qname, quelle.id_quelle)
            self.quelle_list[quelle.qname] = quelle.id_quelle
        session.close()
        
    def __populate_comboBox_Anrede(self):
        session = utilities.createSession() 
        self.cbAnrede.addItem("", 0)
        for anrede in session.query(Anrede).options(load_only("id_anrede", "anrede")):
            # print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbAnrede.addItem(anrede.anrede, anrede.id_anrede)
            self.anrede_list[anrede.anrede] = anrede.id_anrede
        session.close()

    def __setNameTrue(self):
        self.cbAnrede.setEnabled(True)
        self.ledVorname.setStyleSheet(ledStyleString)
        self.ledVorname.setReadOnly(True)
        self.ledNachname.setStyleSheet(ledStyleString)
        self.ledNachname.setReadOnly(True)

    def clicked_btnNeu(self):
        # print("clicked_btnNeu start")
        self.modus = constants.MODUS_NEU
        self.ledBemerkung.clear()
        self.ledBetrag.clear()
        index = self.cbQuelle.findText("", QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.cbQuelle.setCurrentIndex(index)
            self.cbQuelle.setCurrentText("")
            # print("index Quelle = ", str(index))
        self.cbZahlung.setCurrentIndex(0)
        self.dateEdit.setDate(QDate.currentDate())
        self.DiaadminPerson = Ui_DiaadminPerson()
        self.DiaadminPerson.setupUi(self.DiaadminPerson, False)
        if self.DiaadminPerson.exec_():
            self.cbAnrede.setCurrentText(self.DiaadminPerson.cbAnrede.currentText())
            self.ledVorname.setText(self.DiaadminPerson.ledVorname.text())
            self.ledNachname.setText(self.DiaadminPerson.ledNachname.text())
            self.index_anrede = self.DiaadminPerson.index_to_use
            # print("Neu: index_anrede= ", self.index_anrede)
 
    def clicked_btnBearbeiten(self):
        # print("clicked_btnBearbeiten start")
        self.modus = constants.MODUS_BEARBEITEN
        self.zeile = self.twBetrag.selectedItems()[0].row()
        item0 = self.twBetrag.item(self.zeile, 0)
        self.index_to_use = int(item0.text())
        item1 = self.twBetrag.item(self.zeile, 2)
        item2 = self.twBetrag.item(self.zeile, 3)
        self.ledNachname.setText(item2.text().split()[1])
        self.ledVorname.setText(item2.text().split()[0])
        self.cbAnrede.setCurrentText(item1.text())
        self.ledBetrag.setText(self.twBetrag.item(self.zeile, 4).text())
        dto = datetime.datetime.strptime(self.twBetrag.item(self.zeile, 5).text(), "%d.%m.%Y")
        self.dateEdit.setDate(QDate(dto))
        self.ledBemerkung.setText(self.twBetrag.item(self.zeile, 6).text())
        self.cbZahlung.setCurrentText(self.twBetrag.item(self.zeile, 7).text())
        self.cbQuelle.setCurrentText(self.twBetrag.item(self.zeile, 8).text())
        if self.twBetrag.item(self.zeile, 1).text() == "Ausgang":
            self.rbAusgang.setChecked(True)
            self.rbEingang.setChecked(False)
        else:
            self.rbAusgang.setChecked(False)
            self.rbEingang.setChecked(True)
        
        # print("clicked_btnBearbeiten ende:", str(self.index_to_use))

    def clicked_btnLoeschen(self):
        # print("clicked_btnLoeschen start")
        self.modus = constants.MODUS_LOESCHEN
        self.__save_data()
        self.__populate_tableview()

    def clicked_position_bearbeiten(self):
        # print("clicked_position_bearbeiten start")
        if self.rbAusgang.isChecked():
            ea = "Ausgang"
        else:
            ea = "Eingang"
        self.DiaadminPosition = Ui_DiaadminPos()
        self.DiaadminPosition.setupUi(self.DiaadminPosition, self.index_to_use, self.gesamtBetrag, ea)
        self.DiaadminPosition.show()

    def clicked_btnspeichern(self):
        # print("clicked_position_speichern start")
        self.__save_data()
        self.__populate_tableview()

    def __save_data(self):
        # print("Enter __save_data: ", str(self.index_to_use))
        if self.rbAusgang.isChecked():
            ea = "Ausgang"
        else:
            ea = "Eingang"
        session = utilities.createSession()
        if self.modus == constants.MODUS_NEU:
            if len(self.ledBetrag.text()) != 0:
                try:
                    betrag = float(self.ledBetrag.text().replace(',', '.')) * 100
                except ValueError:
                    QMessageBox.information(self, "Information", "Bitte ein Zahl eingeben")
                betrag = betrag / 100
                newBetrag = Betrag(id_zahlung=self.index_zahlung, \
                                   id_quelle=self.index_quelle, \
                                   id_person=self.index_anrede, \
                                   e_a=ea, \
                                   bemerkung=self.ledBemerkung.text(), \
                                   betrag_total=betrag, \
                                   datum=self.dateEdit.date().toString("yyyy-MM-dd"))
                session.add(newBetrag)
        elif self.modus == constants.MODUS_BEARBEITEN:
            # print("Modus Bearbeiten, index_betrag: ", self.index_to_use, " index_person: ", self.index_zahlung, "index_quelle: ", self.index_quelle, "index_zahlung: ", self.index_zahlung)
            betrag = float(self.ledBetrag.text().replace(',', '.')) * 100
            betrag = betrag / 100
            self.index_quelle = self.quelle_list[self.cbQuelle.currentText()]
            self.index_zahlung = self.zahlung_list[self.cbZahlung.currentText()]
            # print("-- Update: ", self.dateEdit.date().toString("yyyy-MM-dd"))
            session.query(Betrag).filter(Betrag.id_betrag == self.index_to_use).update(\
                                        {Betrag.id_quelle:self.index_quelle, \
                                         Betrag.id_zahlung:self.index_zahlung, \
                                         Betrag.e_a:ea, \
                                         Betrag.betrag_total:betrag, \
                                         Betrag.bemerkung:self.ledBemerkung.text(), \
                                         Betrag.datum:self.dateEdit.date().toString("yyyy-MM-dd")\
                                         }, synchronize_session=False)
        elif self.modus == constants.MODUS_LOESCHEN:
            # print("Modus Löschen", self.index_to_use)
            session.query(Betrag).filter(Betrag.id_betrag == self.index_to_use).delete()    
        utilities.closeSessionCommit(session)
        self.modus = constants.MODUS_NULL
 
    def __btnSuchen(self):
        # print("btnSuchen start")
        self.DiaadminBetragSuche = Ui_DiaadminBetragSuche()
        self.DiaadminBetragSuche.setupUi(self.DiaadminBetragSuche)
        if self.DiaadminBetragSuche.exec_():
            # print("Return von Suche, idx_quelle: ", str(self.DiaadminBetragSuche.index_quelle),\
            #       "idx_zahlung: ", str(self.DiaadminBetragSuche.index_zahlung))
            session = utilities.createSession()
            c = 0
            for betrag in session.query(View_betrag_liste).filter(and_(*self.DiaadminBetragSuche.conditions)):
                self.twBetrag.setRowCount(c + 1)
                self.__fill_cells(c, betrag)
                c = c + 1
            utilities.closeSessionCommit(session)

    def __item_Clicked(self):
        # print("Signal ItemSelectionChanged received, Start")
        self.__setButtonsTrue()
        self.zeile = self.twBetrag.selectedItems()[0].row()
        item0 = self.twBetrag.item(self.zeile, 0)
        item1 = self.twBetrag.item(self.zeile, 1)
        self.index_to_use = int(item0.text())
        self.gesamtBetrag = self.twBetrag.item(self.zeile, 4).text()
        if item1.text() == "Ausgang":
            self.btnPosition.setEnabled(True)
        else:
            self.btnPosition.setEnabled(False)
        # print("itemSelctionChanged, Betrag: ", str(float(self.gesamtBetrag)))
        
    def __rbEA_btnToggled(self):
        self.__populate_tableview()
  
