# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminmain_ui.ui',
# licensing of 'adminmain_ui.ui' applies.
#
# Created: Sat Apr 20 15:27:29 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QDialog
from admin_anrede import Ui_adminAnrede
from admin_potd import Ui_admPOTD
from admin_person import Ui_DiaadminPerson
from admin_art import Ui_adminArt
from admin_zahlung import Ui_adminZahlung
from admin_quelle import Ui_adminQuelle
from admin_betrag import Ui_DiaadminBetrag
from admin_pos import Ui_DiaadminPos
from __utilities import utilities

class Ui_AdminMain(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(151, 440)
        
        self.fraButtons = QtWidgets.QFrame(Dialog)
        self.fraButtons.setGeometry(QtCore.QRect(0, 10, 120, 341))
        self.fraButtons.setFrameShape(QtWidgets.QFrame.Panel)
        self.fraButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraButtons.setLineWidth(5)
        self.fraButtons.setObjectName("fraButtons")
        self.fraButtons.setStyleSheet("color: transparent; background-color:red")
        self.layoutWidget = QtWidgets.QWidget(self.fraButtons)

        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 82, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pbnAnrede = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnAnrede.setIcon(icon)
        self.pbnAnrede.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnAnrede.setObjectName("pbnAnrede")
        self.verticalLayout.addWidget(self.pbnAnrede)
 
        self.pbnPerson = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnPerson.setIcon(icon)
        self.pbnPerson.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnPerson.setObjectName("pbnPerson")
        self.verticalLayout.addWidget(self.pbnPerson)
        
        self.pbnArt = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnArt.setIcon(icon)
        self.pbnArt.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnArt.setObjectName("pbnArt")
        self.verticalLayout.addWidget(self.pbnArt)
        
        self.pbnZahlung = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnZahlung.setIcon(icon)
        self.pbnZahlung.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnZahlung.setObjectName("pbnZahlung")
        self.verticalLayout.addWidget(self.pbnZahlung)
        
        self.pbnQuelle = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnQuelle.setIcon(icon)
        self.pbnQuelle.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnQuelle.setObjectName("pbnQuelle")
        self.verticalLayout.addWidget(self.pbnQuelle)
        
        self.pbnPotd = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnPotd.setIcon(icon)
        self.pbnPotd.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnPotd.setObjectName("pbnPotd")
        self.verticalLayout.addWidget(self.pbnPotd)
        
        self.pbnPos = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.pbnPos.setIcon(icon)
        self.pbnPos.setStyleSheet("Text-align:left; background-color: white; color: black");
        self.pbnPos.setObjectName("pbnPos")
        self.verticalLayout.addWidget(self.pbnPos)
         
        self.pbnEnde = QtWidgets.QPushButton(Dialog)
        self.pbnEnde.setGeometry(QtCore.QRect(20, 380, 80, 26))
        self.pbnEnde.setObjectName("pbnEnde")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pbnEnde, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QObject.connect(self.pbnAnrede, QtCore.SIGNAL("clicked()"), self.admin_anrede)
        QtCore.QObject.connect(self.pbnPotd, QtCore.SIGNAL("clicked()"), self.admin_potd)
        QtCore.QObject.connect(self.pbnPerson, QtCore.SIGNAL("clicked()"), self.admin_person)
        QtCore.QObject.connect(self.pbnArt, QtCore.SIGNAL("clicked()"), self.admin_art)
        QtCore.QObject.connect(self.pbnZahlung, QtCore.SIGNAL("clicked()"), self.admin_zahlung)
        QtCore.QObject.connect(self.pbnQuelle, QtCore.SIGNAL("clicked()"), self.admin_quelle)
        QtCore.QObject.connect(self.pbnPos, QtCore.SIGNAL("clicked()"), self.admin_position)
        self.pbnPos.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Administration", None, -1))
        self.pbnAnrede.setText(QtWidgets.QApplication.translate("Dialog", "Anrede", None, -1))
        self.pbnPerson.setText(QtWidgets.QApplication.translate("Dialog", "Person", None, -1))
        self.pbnArt.setText(QtWidgets.QApplication.translate("Dialog", "Art", None, -1))
        self.pbnZahlung.setText(QtWidgets.QApplication.translate("Dialog", "Zahlung", None, -1))
        self.pbnQuelle.setText(QtWidgets.QApplication.translate("Dialog", "Quelle", None, -1))
        self.pbnPotd.setText(QtWidgets.QApplication.translate("Dialog", "POTD", None, -1))
        self.pbnPos.setText(QtWidgets.QApplication.translate("Dialog", "Position", None, -1))
        self.pbnEnde.setText(QtWidgets.QApplication.translate("Dialog", "&Ende", None, -1))
        
    def admin_potd(self):
        self.DiaadmPOTD = Ui_admPOTD()
        self.DiaadmPOTD.setupUi(self.DiaadmPOTD)
        self.DiaadmPOTD.show()

    def admin_anrede(self):
        self.DiaadmAnrede = Ui_adminAnrede()
        self.DiaadmAnrede.setupUi(self.DiaadmAnrede)
        self.DiaadmAnrede.show()
        
    def admin_person(self):
        self.Ui_DiaadminPerson = Ui_DiaadminPerson()
        self.Ui_DiaadminPerson.setupUi(self.Ui_DiaadminPerson)
        self.Ui_DiaadminPerson.show()

    def admin_art(self):
        self.Ui_DiaadminArt = Ui_adminArt()
        self.Ui_DiaadminArt.setupUi(self.Ui_DiaadminArt)
        self.Ui_DiaadminArt.show()

    def admin_zahlung(self):
        self.Ui_DiaadminZahlung = Ui_adminZahlung()
        self.Ui_DiaadminZahlung.setupUi(self.Ui_DiaadminZahlung)
        self.Ui_DiaadminZahlung.show()

    def admin_quelle(self):
        self.Ui_DiaadminQuelle = Ui_adminQuelle()
        self.Ui_DiaadminQuelle.setupUi(self.Ui_DiaadminQuelle)
        self.Ui_DiaadminQuelle.show()

    def admin_betrag(self):
        self.Ui_DiaadminBetrag = Ui_DiaadminBetrag()
        self.Ui_DiaadminBetrag.setupUi(self.Ui_DiaadminBetrag)
        self.Ui_DiaadminBetrag.show()

    def admin_position(self):
        self.Ui_DiaadminPos = Ui_DiaadminPos()
        self.Ui_DiaadminPos.setupUi(self.Ui_DiaadminPos)
        self.Ui_DiaadminPos.show()




