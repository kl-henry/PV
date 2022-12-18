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
from Model_PV import Anrede, Person, View_person_liste
from sqlalchemy.orm import load_only

class Ui_DiaadminPerson(QDialog):
    def setupUi(self, DiaadminPerson, mode = True):
        self.anrede_list = {}
        self.modus = constants.MODUS_NULL
        self.display_mode = mode
        self.index_to_use = 0

        DiaadminPerson.setObjectName("DiaadminPerson")
        DiaadminPerson.resize(849, 633)
        self.layoutWidget = QtWidgets.QWidget(DiaadminPerson)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 540, 254, 28))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        if self.display_mode:
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

        self.tableWidget = QtWidgets.QTableWidget(DiaadminPerson)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 801, 331))
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        self.columnLabels = ["id","Anrede","Name"]
        self.tableWidget.setHorizontalHeaderLabels(self.columnLabels)

        self.grpName = QtWidgets.QGroupBox(DiaadminPerson)
        self.grpName.setGeometry(QtCore.QRect(20, 20, 621, 81))
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
        self.horizontalLayout.addWidget(self.cbAnrede)

        self.lblVorname = QtWidgets.QLabel(self.layoutWidget1)
        self.lblVorname.setObjectName("lblVorname")
        self.horizontalLayout.addWidget(self.lblVorname)

        self.ledVorname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ledVorname.setStyleSheet(ledStyleString)
        self.ledVorname.setObjectName("ledVorname")
        self.horizontalLayout.addWidget(self.ledVorname)

        self.lblNachname = QtWidgets.QLabel(self.layoutWidget1)
        self.lblNachname.setObjectName("lblNachname")
        self.horizontalLayout.addWidget(self.lblNachname)

        self.ledNachname = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ledNachname.setStyleSheet(ledStyleString)
        self.ledNachname.setObjectName("ledNachname")
        self.horizontalLayout.addWidget(self.ledNachname)

        self.buttonBox = QtWidgets.QDialogButtonBox(DiaadminPerson)
        self.buttonBox.setGeometry(QtCore.QRect(480, 590, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.btnSuchen = QtWidgets.QPushButton(DiaadminPerson)
        self.btnSuchen.setGeometry(QtCore.QRect(741, 130, 80, 26))
        self.btnSuchen.setObjectName("btnSuchen")

        self.populate_comboBox()
        self.__populate_tableview()
        self.retranslateUi(DiaadminPerson)
        if not self.display_mode:
            #print("admin_person, setupUI: displayMode: ", str(self.display_mode))
            self.cbAnrede.setEnabled(False)
            self.ledVorname.setReadOnly(True)
            self.ledVorname.setStyleSheet(ledStyleStringDisabled)
            self.ledNachname.setReadOnly(True)
            self.ledNachname.setStyleSheet(ledStyleStringDisabled)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DiaadminPerson.accept)
        self.accepted.connect(self.__save_data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DiaadminPerson.reject)
        if self.display_mode:
            QtCore.QObject.connect(self.btnNeu, QtCore.SIGNAL("clicked()"), self.clicked_btnNeu)
            QtCore.QObject.connect(self.btnBearbeiten, QtCore.SIGNAL("clicked()"), self.clicked_btnBearbeiten)
            QtCore.QObject.connect(self.btnLoeschen, QtCore.SIGNAL("clicked()"), self.clicked_btnLoeschen)
        QtCore.QObject.connect(self.btnSuchen, QtCore.SIGNAL("clicked()"), self.__btnSuchen)
        self.cbAnrede.currentIndexChanged.connect(self.__cb_currentIndexChanged)
        self.tableWidget.itemSelectionChanged.connect(self.__item_Clicked)
        QtCore.QMetaObject.connectSlotsByName(DiaadminPerson)

        DiaadminPerson.setTabOrder(self.cbAnrede, self.ledVorname)
        DiaadminPerson.setTabOrder(self.ledVorname, self.ledNachname)
        if self.display_mode:
            DiaadminPerson.setTabOrder(self.btnNeu, self.btnBearbeiten)
            DiaadminPerson.setTabOrder(self.btnBearbeiten, self.btnLoeschen)
            DiaadminPerson.setTabOrder(self.btnLoeschen, self.btnSuchen)
        DiaadminPerson.setTabOrder(self.btnSuchen, self.tableWidget)
        if self.display_mode:
            self.btnNeu.setDefault(True)

    def retranslateUi(self, DiaadminPerson):
        DiaadminPerson.setWindowTitle(QtWidgets.QApplication.translate("DiaadminPerson", "Admin - Person", None, -1))
        if self.display_mode:
            self.btnNeu.setText(QtWidgets.QApplication.translate("DiaadminPerson", "Neu", None, -1))
            self.btnBearbeiten.setText(QtWidgets.QApplication.translate("DiaadminPerson", "Bearbeiten", None, -1))
            self.btnLoeschen.setText(QtWidgets.QApplication.translate("DiaadminPerson", "Löschen", None, -1))
            self.grpName.setTitle(QtWidgets.QApplication.translate("DiaadminPerson", "Name", None, -1))
        self.lblAnrede.setText(QtWidgets.QApplication.translate("DiaadminPerson", "Anrede:", None, -1))
        self.lblVorname.setText(QtWidgets.QApplication.translate("DiaadminPerson", "Vorname:", None, -1))
        self.lblNachname.setText(QtWidgets.QApplication.translate("DiaadminPerson", "Nachname:", None, -1))
        self.btnSuchen.setText(QtWidgets.QApplication.translate("DiaadminPerson", "&Suchen", None, -1))

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
        for person in session.query(View_person_liste):
            #print("ID: ", anrede.id_anrede, "Art: ", anrede.anrede, "Created: ", anrede.create_time)
            self.tableWidget.setItem(c, 0, QTableWidgetItem(str(person.id_person)))
            self.tableWidget.setItem(c, 1, QTableWidgetItem(person.anrede))
            self.tableWidget.setItem(c, 2, QTableWidgetItem(person.Name))
            c = c + 1
        self.tableWidget.resizeColumnsToContents()
        session.close()

    def __item_Clicked(self):
        #print("Signal ItemSelectionChanged received, Item selected: ")
        if self.display_mode:
            self.__setButtonsTrue()
        else:
            self.clicked_btnBearbeiten()
            self.zeile = self.tableWidget.selectedItems()[0].row()
            item0 = self.tableWidget.item(self.zeile, 0)
            self.index_to_use = int(item0.text())
        #print("Signal ItemSelectionChanged, Index selected: ", str(self.index_to_use))

    def __cb_currentIndexChanged(self, idx):
        #print('current selected index:', idx, "ID: ", str(Art.id_anrede))
        self.index = idx
        self.index_to_insert = self.anrede_list[self.cbAnrede.currentText()]
        #print("IndexChanged idx: ", self.index, " Index To Update: ", self.index_to_insert)

    def clicked_btnNeu(self):
        #print("clicked_btnNeu start")
        self.modus = constants.MODUS_NEU

    def clicked_btnBearbeiten(self):
        #print("clicked_btnBearbeiten start")
        self.modus = constants.MODUS_BEARBEITEN
        self.zeile = self.tableWidget.selectedItems()[0].row()
        item0 = self.tableWidget.item(self.zeile, 0)
        self.index_to_use = int(item0.text())
        item1 = self.tableWidget.item(self.zeile,1)
        item2 = self.tableWidget.item(self.zeile,2)
        self.cbAnrede.setCurrentText(str(item1.text()));
        self.ledVorname.setText(item2.text().split()[0])
        self.ledNachname.setText(item2.text().split()[1])
        #print("Signal clicked_btnBearbeiten, Index selected: ", str(self.index_to_use))

    def clicked_btnLoeschen(self):
        #print("clicked_btnLoeschen start")
        self.modus = constants.MODUS_LOESCHEN
        self.zeile = self.tableWidget.selectedItems()[0].row()
        item0 = self.tableWidget.item(self.zeile, 0)
        self.index_to_use = int(item0.text())
        print("Signal clicked_btnLoeschen, Index selected: ", str(self.index_to_use))

    def __save_data(self):
        #print("Enter __save_data(Person): ", str(self.modus))
        session = utilities.createSession()
        if self.modus == constants.MODUS_NEU:
            if len(self.ledNachname.text()) != 0:
                newPerson = Person(id_anrede = self.index_to_insert, nachname = self.ledNachname.text(),\
                                   vorname = self.ledVorname.text())
                session.add(newPerson)
            else:
                QMessageBox.information(self, "Hinweis", "Bitte Feld Nachname befüllen")
        elif self.modus == constants.MODUS_BEARBEITEN:
            #print("Modus Bearbeiten, index_anrede: ", self.index_to_insert, " index_person: ", self.index_to_use)
            session.query(Person).filter(Person.id_person == self.index_to_use).update(\
                                        {Person.id_anrede:self.index_to_insert, \
                                         Person.vorname:self.ledVorname.text(),\
                                         Person.nachname:self.ledNachname.text(),\
                                         }, synchronize_session = False)
        elif self.modus == constants.MODUS_LOESCHEN:
            #print("Modus Löschen", self.index_to_use)
            session.query(Person).filter(Person.id_person==self.index_to_use).delete()
        utilities.closeSessionCommit(session)

    def __btnSuchen(self):
        #print("btnSuchen start")
        QMessageBox.information(self, "Information", "Funktion ist in Arbeit")
