# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui',
# licensing of 'Mainwindow.ui' applies.
#
# Created: Tue Apr  2 12:26:12 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow
from __utilities import utilities
from ui_hilfe import Ui_Hilfe
from admin_potd import Ui_admPOTD
from admin_anrede import Ui_adminAnrede
from adminmain import Ui_AdminMain
from admin_person import Ui_DiaadminPerson
from admin_art import Ui_adminArt
from admin_kontakt import Ui_DiaadminKontakt
from admin_zahlung import Ui_adminZahlung
from admin_quelle import Ui_adminQuelle
from admin_betrag import Ui_DiaadminBetrag
from admin_pos import Ui_DiaadminPos


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 243)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lblImage = QtWidgets.QLabel(self.centralWidget)
        self.lblImage.setGeometry(QtCore.QRect(180, 30, 111, 101))
        self.lblImage.setFrameShape(QtWidgets.QFrame.Box)
        self.lblImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblImage.setText("")
        icon_name = utilities.get_potd_name(6)
        # print("icon_name= ",icon_name)
        self.lblImage.setPixmap(QtGui.QPixmap(icon_name))
        self.lblImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImage.setObjectName("lblImage")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 540, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_Datei = QtWidgets.QMenu(self.menuBar)
        self.menu_Datei.setObjectName("menu_Datei")
        self.menu_Aktionen = QtWidgets.QMenu(self.menuBar)
        self.menu_Aktionen.setObjectName("menu_Aktionen")
        self.menu_Hilfe = QtWidgets.QMenu(self.menuBar)
        self.menu_Hilfe.setObjectName("menu_Hilfe")
        self.menu_Admin = QtWidgets.QMenu(self.menuBar)
        self.menu_Admin.setObjectName("menu_Admin")

        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_Neu = QtWidgets.QAction(MainWindow)
        self.action_Neu.setObjectName("action_Neu")
        self.action_ffnen = QtWidgets.QAction(MainWindow)
        self.action_ffnen.setObjectName("action_ffnen")
        self.action_Schlie_en = QtWidgets.QAction(MainWindow)
        self.action_Schlie_en.setObjectName("action_Schlie_en")
        self.action_Ende = QtWidgets.QAction(MainWindow)
        self.action_Ende.setObjectName("action_Ende")

        self.actionKontakte = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(utilities.get_potd_name(3)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionKontakte.setIcon(icon)
        self.actionKontakte.setObjectName("actionKontakte")

        self.actionFinanzen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(utilities.get_potd_name(4)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionFinanzen.setIcon(icon1)
        self.actionFinanzen.setObjectName("actionFinanzen")

        self.actionStatistiken = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(utilities.get_potd_name(5)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionStatistiken.setIcon(icon2)
        self.actionStatistiken.setObjectName("actionStatistiken")

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(utilities.get_potd_name(2)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionUeber = QtWidgets.QAction(MainWindow)
        self.actionUeber.setIcon(icon3)
        self.actionUeber.setObjectName("actionUeber")

        self.actionAdmin = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(utilities.get_potd_name(9)), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionAdmin.setIcon(icon4)
        self.actionAdmin.setObjectName("actionAdmin")

        self.actionPicture_of_the_Day_POTD = QtWidgets.QAction(MainWindow)
        self.actionPicture_of_the_Day_POTD.setObjectName("actionPicture_of_the_Day_POTD")
        self.actionArt = QtWidgets.QAction(MainWindow)
        self.actionArt.setObjectName("actionArt")
        self.actionPerson = QtWidgets.QAction(MainWindow)
        self.actionPerson.setObjectName("actionPerson")
        self.actionZahlung = QtWidgets.QAction(MainWindow)
        self.actionZahlung.setObjectName("actionZahlung")
        self.actionQuelle = QtWidgets.QAction(MainWindow)
        self.actionQuelle.setObjectName("actionQuelle")
        self.actionAnrede = QtWidgets.QAction(MainWindow)
        self.actionAnrede.setObjectName("actionAnrede")
        self.actionPosition = QtWidgets.QAction(MainWindow)
        self.actionPosition.setObjectName("actionPosition")

        self.menu_Datei.addAction(self.action_Neu)
        self.menu_Datei.addAction(self.action_ffnen)
        self.menu_Datei.addAction(self.action_Schlie_en)
        self.menu_Datei.addAction(self.action_Ende)
        self.menu_Aktionen.addAction(self.actionFinanzen)
        self.menu_Aktionen.addAction(self.actionStatistiken)
        self.menuBar.addAction(self.menu_Datei.menuAction())
        self.menuBar.addAction(self.menu_Aktionen.menuAction())
        self.menuBar.addAction(self.menu_Hilfe.menuAction())
        self.menu_Aktionen.addAction(self.actionFinanzen)
        self.menu_Aktionen.addAction(self.actionStatistiken)
        self.menu_Admin.addAction(self.actionPicture_of_the_Day_POTD)
        self.menu_Admin.addSeparator()
        self.menu_Admin.addAction(self.actionArt)
        self.menu_Admin.addAction(self.actionPerson)
        self.menu_Admin.addAction(self.actionZahlung)
        self.menu_Admin.addAction(self.actionQuelle)
        self.menu_Admin.addAction(self.actionAnrede)
        self.menu_Admin.addAction(self.actionPosition)

        self.menuBar.addAction(self.menu_Admin.menuAction())
        self.mainToolBar.addAction(self.actionKontakte)
        self.mainToolBar.addAction(self.actionFinanzen)
        self.mainToolBar.addAction(self.actionStatistiken)
        self.mainToolBar.addAction(self.actionUeber)
        self.mainToolBar.addAction(self.actionAdmin)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Ende, QtCore.SIGNAL("clicked()"), MainWindow.close)
        self.actionUeber.triggered.connect(self.show_ueber)
        self.actionKontakte.triggered.connect(self.show_Kontakte)
        self.actionAdmin.triggered.connect(self.admin_main)
        self.actionPicture_of_the_Day_POTD.triggered.connect(self.admin_potd)
        self.actionAnrede.triggered.connect(self.admin_anrede)
        self.actionPerson.triggered.connect(self.admin_person)
        self.actionArt.triggered.connect(self.admin_art)
        self.actionZahlung.triggered.connect(self.admin_zahlung)
        self.actionQuelle.triggered.connect(self.admin_quelle)
        self.actionFinanzen.triggered.connect(self.admin_betrag)
        self.actionPosition.triggered.connect(self.admin_position)
        self.actionPosition.setEnabled(False)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.menu_Datei.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Datei", None, -1))
        self.menu_Aktionen.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Aktionen", None, -1))
        self.menu_Hilfe.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Hilfe", None, -1))
        self.menu_Admin.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Admin", None, -1))
        self.action_Neu.setText(QtWidgets.QApplication.translate("MainWindow", "&Neu", None, -1))
        self.action_ffnen.setText(QtWidgets.QApplication.translate("MainWindow", "&Öffnen", None, -1))
        self.action_Schlie_en.setText(QtWidgets.QApplication.translate("MainWindow", "&Schließen", None, -1))
        self.action_Ende.setText(QtWidgets.QApplication.translate("MainWindow", "&Ende", None, -1))
        self.actionKontakte.setText(QtWidgets.QApplication.translate("MainWindow", "Kontakte", None, -1))
        self.actionFinanzen.setText(QtWidgets.QApplication.translate("MainWindow", "Finanzen", None, -1))
        self.actionStatistiken.setText(QtWidgets.QApplication.translate("MainWindow", "Statistiken", None, -1))
        self.actionStatistiken.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Statistiken", None, -1))
        self.actionUeber.setText(QtWidgets.QApplication.translate("MainWindow", "Über", None, -1))
        self.actionUeber.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Über", None, -1))
        self.actionPicture_of_the_Day_POTD.setText(
            QtWidgets.QApplication.translate("MainWindow", "Picture of the Day(POTD)"))
        self.actionArt.setText(QtWidgets.QApplication.translate("MainWindow", "Art"))
        self.actionPerson.setText(QtWidgets.QApplication.translate("MainWindow", "Person"))
        self.actionZahlung.setText(QtWidgets.QApplication.translate("MainWindow", "Zahlung"))
        self.actionQuelle.setText(QtWidgets.QApplication.translate("MainWindow", "Quelle"))
        self.actionAnrede.setText(QtWidgets.QApplication.translate("MainWindow", "Anrede"))
        self.actionPosition.setText(QtWidgets.QApplication.translate("MainWindow", "Position"))
        self.actionAdmin.setText(QtWidgets.QApplication.translate("MainWindow", "Admin"))

    def show_ueber(self):
        self.nd = Ui_Hilfe()
        self.nd.setupUi(self.nd)
        self.nd.show()

    def show_Kontakte(self):
        self.DiaadminKontakt = Ui_DiaadminKontakt()
        self.DiaadminKontakt.setupUi(self.DiaadminKontakt)
        self.DiaadminKontakt.show()

    def show_Finanzen(self):
        self.nd = Ui_Hilfe()
        self.nd.setupUi(self.nd)
        self.nd.show()

    def show_Statistiken(self):
        self.nd = Ui_Hilfe()
        self.nd.setupUi(self.nd)
        self.nd.show()

    def admin_main(self):
        self.DiaadmMain = Ui_AdminMain()
        self.DiaadmMain.setupUi(self.DiaadmMain)
        self.DiaadmMain.show()

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
