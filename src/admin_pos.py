# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_adminbetrag.ui',
# licensing of 'ui_adminbetrag.ui' applies.
#
# Created: Sat Apr 27 13:30:49 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QDialog, QTableWidgetItem,QMessageBox,QAbstractItemView
from sqlalchemy.orm import load_only
from Model_PV import Art, Position, View_pos_liste
import constants
from __utilities import utilities
from stylestrings import ledStyleString, gbStyleString, ledStyleStringDisabled

class Ui_DiaadminPos(QDialog):
    def setupUi(self, DiaadminPosition, id_betrag = 0, gesBetrag = 0.0, ea = ""):
        self.idBetrag = id_betrag
        self.gesamtBetrag = gesBetrag
        self.ea = ea
        self.modus = constants.MODUS_NULL
        self.art_list = {}
        self.newPos_list = []
        self.index_art = 0
        
        DiaadminPosition.setObjectName("DiaadminPosition")
        DiaadminPosition.resize(849, 545)
        
        self.layoutWidget = QtWidgets.QWidget(DiaadminPosition)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 450, 254, 28))
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
        
        self.twPosition = QtWidgets.QTableWidget(DiaadminPosition)
        self.twPosition.setGeometry(QtCore.QRect(19, 210, 801, 231))
        self.twPosition.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.twPosition.verticalHeader().setVisible(False)
        self.twPosition.verticalHeader().setHighlightSections(False)
        self.twPosition.setObjectName("twPosition")
        self.twPosition.setColumnCount(4)
        self.twPosition.setRowCount(0)
        self.columnLabels = ["id","Art", "Betrag", "Bemerkung"]
        self.twPosition.setHorizontalHeaderLabels(self.columnLabels)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(DiaadminPosition)
        self.buttonBox.setGeometry(QtCore.QRect(479, 500, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.gbPosition = QtWidgets.QGroupBox(DiaadminPosition)
        self.gbPosition.setGeometry(QtCore.QRect(19, 10, 201, 80))
        self.gbPosition.setStyleSheet(gbStyleString)
        self.gbPosition.setObjectName("gbPosition")
        self.layoutWidget1 = QtWidgets.QWidget(self.gbPosition)
        
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 141, 28))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.lblArt = QtWidgets.QLabel(self.layoutWidget1)
        self.lblArt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblArt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblArt.setObjectName("lblArt")
        self.horizontalLayout_6.addWidget(self.lblArt)

        self.cbArt = QtWidgets.QComboBox(self.layoutWidget1)
        self.cbArt.setObjectName("cbQuelle")
        self.cbArt.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.cbArt)

        self.gbBetrag = QtWidgets.QGroupBox(DiaadminPosition)
        self.gbBetrag.setGeometry(QtCore.QRect(19, 110, 621, 80))
        self.gbBetrag.setStyleSheet(gbStyleString)
        self.gbBetrag.setObjectName("gbBetrag")
        self.layoutWidget2 = QtWidgets.QWidget(self.gbBetrag)
        
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 591, 28))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.lblBetrag = QtWidgets.QLabel(self.layoutWidget2)
        self.lblBetrag.setObjectName("lblBetrag")
        self.horizontalLayout_7.addWidget(self.lblBetrag)
        
        self.ledBetrag = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ledBetrag.setObjectName("ledBetrag")
        self.ledBetrag.setEnabled(False)
        self.ledBetrag.setStyleSheet(ledStyleStringDisabled)
        self.horizontalLayout_7.addWidget(self.ledBetrag)
        
        self.lblBemerkung = QtWidgets.QLabel(self.layoutWidget2)
        self.lblBemerkung.setObjectName("lblBemerkung")
        self.horizontalLayout_7.addWidget(self.lblBemerkung)
        
        self.ledBemerkung = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ledBemerkung.setStyleSheet(ledStyleStringDisabled)
        self.ledBemerkung.setEnabled(False)
        self.ledBemerkung.setObjectName("ledBemerkung")
        self.horizontalLayout_7.addWidget(self.ledBemerkung)
        
        self.btnSuchen = QtWidgets.QPushButton(DiaadminPosition)
        self.btnSuchen.setGeometry(QtCore.QRect(740, 160, 80, 26))
        self.btnSuchen.setObjectName("btnSuchen")

        self.btnUebernehmen = QtWidgets.QPushButton(DiaadminPosition)
        self.btnUebernehmen.setEnabled(False)
        self.btnUebernehmen.setGeometry(QtCore.QRect(729, 450, 91, 26))
        self.btnUebernehmen.setObjectName("btnUebernehmen")

        self.gbBetrag_2 = QtWidgets.QGroupBox(DiaadminPosition)
        self.gbBetrag_2.setGeometry(QtCore.QRect(370, 10, 271, 91))
        self.gbBetrag_2.setStyleSheet(gbStyleString)
        self.gbBetrag_2.setObjectName("gbBetrag_2")
        
        self.layoutWidget3 = QtWidgets.QWidget(self.gbBetrag_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 30, 221, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.lblZwSumme = QtWidgets.QLabel(self.layoutWidget3)
        self.lblZwSumme.setObjectName("lblZwSumme")
        
        self.verticalLayout_2.addWidget(self.lblZwSumme)
        self.lblGesamtBetrag = QtWidgets.QLabel(self.layoutWidget3)
        self.lblGesamtBetrag.setObjectName("lblGesamtBetrag")
        
        self.verticalLayout_2.addWidget(self.lblGesamtBetrag)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.lblZwischensumme = QtWidgets.QLabel(self.layoutWidget3)
        self.lblZwischensumme.setObjectName("lblZwischensumme")
        self.lblZwischensumme.setText("0,0")
        self.verticalLayout.addWidget(self.lblZwischensumme)
        
        self.lblGesBetrag = QtWidgets.QLabel(self.layoutWidget3)
        self.lblGesBetrag.setObjectName("lblGesBetrag")
        self.lblGesBetrag.setText(str("%.2f"%float(self.gesamtBetrag)).replace(".",","))
        self.verticalLayout.addWidget(self.lblGesBetrag)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.retranslateUi(DiaadminPosition)
        self.__populate_tableview()
        self.__populate_comboBox_Art()
        self.__setButtonsFalse()
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DiaadminPosition.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DiaadminPosition.reject)
        QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.clicked_btnNeu)
        QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.clicked_btnBearbeiten)
        QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.clicked_btnLoeschen)
        QtCore.QObject.connect(self.btnUebernehmen, QtCore.SIGNAL("clicked()"), self.clicked_btnUebernehmen)
        self.cbArt.currentIndexChanged.connect(self.__cb_currentIndexChanged_art)
        self.twPosition.itemClicked.connect(self.__item_Clicked)

        QtCore.QMetaObject.connectSlotsByName(DiaadminPosition)
        
        DiaadminPosition.setTabOrder(self.ledBetrag, self.ledBemerkung)
        DiaadminPosition.setTabOrder(self.ledBemerkung, self.btnNeu)
        DiaadminPosition.setTabOrder(self.btnNeu, self.btnBearbeiten)
        DiaadminPosition.setTabOrder(self.btnBearbeiten, self.btnLoeschen)
        DiaadminPosition.setTabOrder(self.btnLoeschen, self.btnSuchen)
        DiaadminPosition.setTabOrder(self.btnUebernehmen, self.btnSuchen)
        DiaadminPosition.setTabOrder(self.btnSuchen, self.twPosition)

    def retranslateUi(self, DiaadminPosition):
        DiaadminPosition.setWindowTitle(QtWidgets.QApplication.translate("DiaadminPosition", "Admin -Position", None, -1))
        self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Neu", None, -1))
        self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Bearbeiten", None, -1))
        self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Löschen", None, -1))
        self.gbPosition.setTitle(QtWidgets.QApplication.translate("DiaadminPosition", "Position", None, -1))
        self.lblArt.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Art:", None, -1))
        self.gbBetrag.setTitle(QtWidgets.QApplication.translate("DiaadminPosition", "Betrag", None, -1))
        self.lblBetrag.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Betrag:", None, -1))
        self.lblBemerkung.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Bemerkung:", None, -1))
        self.btnSuchen.setText(QtWidgets.QApplication.translate("DiaadminPosition", "&Suchen", None, -1))
        self.btnUebernehmen.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Übernehmen", None, -1))
        self.gbBetrag_2.setTitle(QtWidgets.QApplication.translate("DiaadminPosition", "Summe", None, -1))
        self.lblZwSumme.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Zwischensumme:", None, -1))
        self.lblGesamtBetrag.setText(QtWidgets.QApplication.translate("DiaadminPosition", "Gesamtbetrag:", None, -1))

    def __setButtonsTrue(self):
        self.btnBearbeiten.setEnabled(True)
        self.btnLoeschen.setEnabled(True)
        self.btnUebernehmen.setEnabled(True)
        
    def __setButtonsFalse(self):
        self.btnBearbeiten.setEnabled(False)
        self.btnLoeschen.setEnabled(False)
        self.btnUebernehmen.setEnabled(False)
    
    def __berechne_zwischensumme(self):
        #print("berechne_zwischensumme, start")
        lastRow = self.twPosition.rowCount()
        #print("berechne_zwischensumme, lastRow: ", str(lastRow))
        zwSumme = 0.0
        for c in range (0, lastRow):
            #print("Betrag: ", str(position.po_betrag))
            item = self.twPosition.item(c, 2)
            betrag = float(item.text().replace(",","."))
            zwSumme = zwSumme + float(betrag)            
            #print("berechne_zwischensumme, betrag: ", str(betrag), " zwSumme: ", str(zwSumme), "item: ", item.text())
        return zwSumme
    
    def __populate_tableview(self):
        #print("Enter __populate_tableview, Position. IdBetrag: ", str(self.idBetrag))
        session = utilities.createSession()
        self.zwSumme = 0.0
        c = 0
        for position in session.query(View_pos_liste).order_by(View_pos_liste.betrag).filter(View_pos_liste.id_betrag == self.idBetrag).order_by(View_pos_liste.betrag.desc()):
            #print("Betrag: ", str(position.po_betrag))
            self.twPosition.setRowCount(c+1)
            self.twPosition.setItem(c, 0, QTableWidgetItem(str(position.id_pos)))
            self.twPosition.setItem(c, 1, QTableWidgetItem(position.art))
            self.twPosition.setItem(c, 2, QTableWidgetItem(str(position.betrag).replace(".",",")))
            self.twPosition.setItem(c, 3, QTableWidgetItem(position.bemerkung))
            c = c + 1
        self.twPosition.resizeColumnsToContents()
        session.close()
        self.lblZwischensumme.setText(str("%.2f"%self.__berechne_zwischensumme()).replace(".",","))

    def __cb_currentIndexChanged_art(self, idx):
        #print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        if idx != 0:
            self.index_art = self.art_list[self.cbArt.currentText()]
        self.btnUebernehmen.setEnabled(True)
        
    def __populate_comboBox_Art(self):
        session = utilities.createSession() 
        self.cbArt.addItem("",0)
        for art in session.query(Art).order_by(Art.aname.asc()).options(load_only("id_art","aname")):
            #print("ID: ", anrede.id_anrede, " -- ", "Art: ", anrede.anrede)
            self.cbArt.addItem(art.aname,art.id_art)
            self.art_list[art.aname] = art.id_art
        session.close()

    def __clear_input(self):
        index = self.cbArt.findText("")
        #print("clear_input index: ", str(index))
        self.cbArt.setCurrentIndex(index)
        self.ledBetrag.setText("")
        self.ledBemerkung.setText("")

    def __enable_input(self):
        self.cbArt.setEnabled(True)
        self.ledBetrag.setEnabled(True)
        self.ledBetrag.setStyleSheet(ledStyleString)
        self.ledBemerkung.setEnabled(True)
        self.ledBemerkung.setStyleSheet(ledStyleString)

    def clicked_btnNeu(self):
        #print("clicked_btnNeu start")
        self.modus = constants.MODUS_NEU
        self.__enable_input()
        self.__clear_input()

    def clicked_btnBearbeiten(self):
        #print("clicked_btnBearbeiten start")
        self.modus = constants.MODUS_BEARBEITEN
        self.__enable_input()
        self.curRow = self.twPosition.currentRow()
        self.zeile = self.twPosition.selectedItems()[0].row()
        item0 = self.twPosition.item(self.zeile, 0)
        self.index_to_use = int(item0.text())
        self.cbArt.setCurrentText(self.twPosition.item(self.zeile,1).text())
        self.ledBetrag.setText(self.twPosition.item(self.zeile,2).text().replace(".",",")) 
        if len(str(self.twPosition.item(self.zeile,3).text())) !=0:
            self.ledBemerkung.setText(self.twPosition.item(self.zeile,3).text())
        else:
            self.ledBemerkung.setText("--")
        #print("clicked_btnBearbeiten ende:", str(self.index_to_use))

    def clicked_btnLoeschen(self):
        #print("clicked_btnLoeschen start")
        self.modus = constants.MODUS_LOESCHEN

    def clicked_btnUebernehmen(self):
        #print("clicked_btnLoeschen start")
        #print("Start clicked_btnUebernehmen, TableRowCount: ", self.twPosition.rowCount())
        if (self.modus == constants.MODUS_NEU) or (self.modus == constants.MODUS_GESPEICHERT):
            if self.__check_input_data():    
                rowcount = self.twPosition.rowCount()
                self.twPosition.setRowCount(rowcount+1)
                #print("self.cbArt.currentText()",self.cbArt.currentText(), "Neu Rowcount: ", str(rowcount), "ID Art: ", str(self.index_art))
                self.twPosition.setItem(rowcount, 0, QTableWidgetItem(""))
                self.twPosition.setItem(rowcount, 1, QTableWidgetItem(self.cbArt.currentText()))
                self.twPosition.setItem(rowcount, 2, QTableWidgetItem(self.ledBetrag.text().replace(".",",")))
                self.twPosition.setItem(rowcount, 3, QTableWidgetItem(self.ledBemerkung.text()))
                betrag = float(self.ledBetrag.text().replace(',', '.'))*100
                betrag = betrag / 100
                newPos = Position(id_art = self.index_art, id_betrag = self.idBetrag,\
                                  bemerkung = self.ledBemerkung.text(), pos_betrag = betrag)
                self.newPos_list.append(newPos)
                self.lblZwischensumme.setText(str("%.2f"%self.__berechne_zwischensumme()).replace(".",","))
                self.__clear_input()
                self.modus = constants.MODUS_GESPEICHERT
        elif self.modus == constants.MODUS_BEARBEITEN:
            self.twPosition.setItem(self.curRow, 1, QTableWidgetItem(self.cbArt.currentText()))
            self.twPosition.setItem(self.curRow, 2, QTableWidgetItem(self.ledBetrag.text()))
            self.twPosition.setItem(self.curRow, 3, QTableWidgetItem(self.ledBemerkung.text()))
            self.lblZwischensumme.setText(str("%.2f"%self.__berechne_zwischensumme()).replace(".",","))
        
    def __save_data(self):
        #print("Enter __save_data(Position), modus", str(self.modus), "idBetrag: ", str(self.idBetrag))
        session = utilities.createSession()
        if (self.modus == constants.MODUS_NEU) or (self.modus == constants.MODUS_GESPEICHERT):
            if self.__check_input_data():
                #print("Enter __save_data(Position), ledBetrag", self.ledBetrag.text(), "index_art: ", str(self.index_art), "Länge Liste: ",len(self.newPos_list))            
                if (len(self.newPos_list) != 0):
                    session.add_all(self.newPos_list)
                    self.newPos_list.clear()
                if (len(self.ledBetrag.text()) != 0) and (self.index_art != 0):
                    betrag = float(self.ledBetrag.text().replace(',', '.'))*100
                    betrag = betrag / 100
                    newPosition = Position(id_art = self.index_art, id_betrag = self.idBetrag,\
                                       bemerkung = self.ledBemerkung.text(), pos_betrag = betrag)
                    self.newPos_list.append(newPosition)
                    session.add(newPosition)
        elif self.modus == constants.MODUS_BEARBEITEN:
            betrag = float(self.ledBetrag.text().replace(',', '.'))*100
            betrag = betrag / 100
            #print("Modus Bearbeiten, index_pos: ", self.index_to_use, " betrag: ", betrag)
            session.query(Position).filter(Position.id_pos == self.index_to_use).update(\
                                            {Position.id_art:self.index_art, \
                                             Position.pos_betrag:betrag,\
                                             Position.bemerkung:self.ledBemerkung.text(),\
                                             }, synchronize_session = False)
        elif self.modus == constants.MODUS_LOESCHEN:
                #print("Modus Löschen", self.index_to_use)
            session.query(Position).filter(Position.id_pos==self.index_to_use).delete()    
        utilities.closeSessionCommit(session)
 
    def __btnSuchen(self):
        #print("btnSuchen start")
        QMessageBox.information(self, "Information", "Funktion ist in Arbeit")
        
    def __item_Clicked(self):
        #print("Signal ItemSelectionChanged received, Item selected: ")
        self.__setButtonsTrue()
        self.zeile = self.twPosition.selectedItems()[0].row()
        item0 = self.twPosition.item(self.zeile, 0)
        if item0.text() != '':
            self.index_to_use = int(item0.text())

    def __check_input_data(self):
        error = True
        if self.modus != constants.MODUS_GESPEICHERT:
            try:
                float(self.ledBetrag.text().replace(',', '.'))
            except ValueError:
                QMessageBox.information(self, "Information", "Bitte eine Zahl eingeben")
                self.ledBetrag.setFocus()
                self.ledBetrag.setText("")
                error = False
        return error
