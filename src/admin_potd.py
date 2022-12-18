# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_potd.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import os
import typing

import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QDialog

from sqlalchemy.orm import load_only
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from MySQlConnectSQLAlchemy import connect_string
from Potd import Potd
from stylestrings import labelStyleString


class Ui_admPOTD(QDialog):

    # def __init__(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = ...,
    #              f: PySide2.QtCore.Qt.WindowFlags = ...):
    #     super().__init__(parent, f)


    def setupUi(self, Dialog):
        self.path = ""
        self.index = 0
        self.potd_list = {}

        Dialog.setObjectName("admPOTD")
        Dialog.resize(600, 300)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.lblImage = QtWidgets.QLabel(Dialog)
        self.lblImage.setGeometry(QtCore.QRect(400, 30, 111, 101))
        self.lblImage.setFrameShape(QtWidgets.QFrame.Box)
        self.lblImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblImage.setText("Leer")
        self.lblImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImage.setObjectName("lblImage")

        self.lblDateiname = QtWidgets.QLabel(Dialog)
        self.lblDateiname.setGeometry(QtCore.QRect(40, 200, 301, 18))
        self.lblDateiname.setObjectName("lblDateiname")

        self.lblDateinameAnzeige = QtWidgets.QLabel(Dialog)
        self.lblDateinameAnzeige.setGeometry(QtCore.QRect(170, 200, 350, 25))
        self.lblDateinameAnzeige.setStyleSheet(labelStyleString)
        self.lblDateinameAnzeige.setObjectName("lblDateinameAnzeige")

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 50, 251, 28))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblPOTDKategorie = QtWidgets.QLabel(self.widget)
        self.lblPOTDKategorie.setObjectName("lblPOTDKategorie")
        self.horizontalLayout.addWidget(self.lblPOTDKategorie)

        self.cbPOTDIndex = QtWidgets.QComboBox(self.widget)
        self.cbPOTDIndex.setObjectName("cbPOTDIndex")
        self.horizontalLayout.addWidget(self.cbPOTDIndex)
        self.populate_comboBox()

        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(30, 160, 181, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.lblPOTDAuswahl = QtWidgets.QLabel(self.widget1)
        self.lblPOTDAuswahl.setObjectName("lblPOTDAuswahl")
        self.horizontalLayout_2.addWidget(self.lblPOTDAuswahl)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.btnDatei = QtWidgets.QToolButton(self.widget1)
        self.btnDatei.setObjectName("btnDatei")
        self.horizontalLayout_2.addWidget(self.btnDatei)

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(Dialog.accept)
        self.accepted.connect(self.__save_selection)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.cbPOTDIndex.currentIndexChanged.connect(self.__cb_currentIndexChanged)
        self.btnDatei.clicked.connect(self.__tbtnDatei_pressed)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, admPOTD):
        _translate = QtCore.QCoreApplication.translate
        admPOTD.setWindowTitle(_translate("admPOTD", "Admin Picture of the Day"))
        self.lblDateiname.setText(_translate("admPOTD", "Dateiname:"))
        self.lblDateinameAnzeige.setText(_translate("admPOTD", "Dateiname"))
        self.lblPOTDKategorie.setText(_translate("admPOTD", "Kategorie:"))
        self.lblPOTDAuswahl.setText(_translate("admPOTD", "Bilddatei auswählen:"))
        self.btnDatei.setText(_translate("admPOTD", "..."))

    def populate_comboBox(self):
        # print("admin_potd: enter populate_comboBox")
        # read database
        engine = create_engine(connect_string, echo=False)
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        self.cbPOTDIndex.addItem("", 0)
        self.potd_all = session.query(Potd).options(load_only("potd_id", "potd_Beschreibung"))
        for potd in self.potd_all:
            # print("ID: ", potd.potd_id, " -- ", "Beschreibung: ", potd.potd_Beschreibung)
            if potd.potd_Beschreibung != None:
                self.cbPOTDIndex.addItem(potd.potd_Beschreibung, potd.potd_id)
                self.potd_list[potd.potd_Beschreibung] = potd.potd_id
        session.close()
        # print(self.potd_list)

    def __cb_currentIndexChanged(self, idx):
        # print('current selected index:', idx)
        self.index = idx

    def __save_selection(self):
        # print( "save selection: index = ", self.index)
        if self.index != 0:
            pfad = os.path.split(self.path)
            dname = pfad[0] + '/'
            fname = pfad[1]
            engine = create_engine(connect_string, echo=False)

            # create a Session
            Session = sessionmaker(bind=engine)
            session = Session()
            id_update = self.potd_list[self.cbPOTDIndex.currentText()]
            # print("Save selection id to update: ", str(id_update))
            session.query(Potd).filter(Potd.potd_id == id_update).update({Potd.potd_fname: fname},
                                                                         synchronize_session=False)
            session.query(Potd).filter(Potd.potd_id == id_update).update({Potd.potd_dname: dname},
                                                                         synchronize_session=False)
            session.commit()

    def __tbtnDatei_pressed(self):
        # print('__tbtnDatei_pressed gewählt')
        doc_path = "/home/hhill/Apps/PV"
        file_dialog = QtWidgets.QFileDialog(
            caption="Save As",
            directory=doc_path,
            filter="Bilder (*.png *.jpg)"
        )
        file_dialog.setLabelText(QtWidgets.QFileDialog.Accept, "Save")
        file_dialog.setLabelText(QtWidgets.QFileDialog.Reject, "Cancel")
        file_dialog.setOption(QtWidgets.QFileDialog.DontResolveSymlinks)
        file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog)
        if not file_dialog.exec_():
            return
        self.path = file_dialog.selectedFiles()[0]
        self.lblDateinameAnzeige.setText(self.path)
        # print('__tbtnDatei_pressed: path=', self.path)

        self.lblImage.setPixmap(QtGui.QPixmap(self.path))
