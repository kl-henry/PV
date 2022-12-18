# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hilfe.ui',
# licensing of 'ui_hilfe.ui' applies.
#
# Created: Fri Apr  5 10:40:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog
from sqlalchemy.orm import load_only
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from MySQlConnectSQLAlchemy import connect_string
from Potd import Potd

class Ui_Hilfe(QDialog):
    def setupUi(self, Dialog):
        #print("Enter Ui_Hilfe")
        #Dialog = QDialog()
        Dialog.setObjectName("Hilfe")
        Dialog.resize(619, 445)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 571, 381))
        self.label.setText("")
        potd_dateiname = self.__get_potd_name()
        #print("Dateiname: ", potd_dateiname)
        self.label.setPixmap(QtGui.QPixmap(potd_dateiname))
        self.label.setObjectName("label")
        #print("SetupUI entered")
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        
    def __get_potd_name(self):
        #read database
        engine = create_engine(connect_string, echo=False)
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
        potd = session.query(Potd).filter(Potd.potd_id == 1).options(load_only("potd_fname","potd_dname")).first()
        #print("Dateiname: ", potd.potd_dname+potd.potd_fname)
        session.close()
        return potd.potd_dname+potd.potd_fname
