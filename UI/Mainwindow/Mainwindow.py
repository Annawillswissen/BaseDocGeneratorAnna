# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pb_Schnittstellen = QPushButton(self.centralwidget)
        self.pb_Schnittstellen.setObjectName(u"pb_Schnittstellen")
        self.pb_Schnittstellen.setGeometry(QRect(30, 100, 131, 41))
        self.pb_Schnittstellen.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(68, 68, 68);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.pb_SoO = QPushButton(self.centralwidget)
        self.pb_SoO.setObjectName(u"pb_SoO")
        self.pb_SoO.setGeometry(QRect(30, 150, 131, 41))
        self.pb_SoO.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(68, 68, 68);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.pb_spare = QPushButton(self.centralwidget)
        self.pb_spare.setObjectName(u"pb_spare")
        self.pb_spare.setGeometry(QRect(30, 200, 121, 41))
        self.pb_spare.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(68, 68, 68);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 191, 481))
        self.widget.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"border-radius: 25px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 400, 191, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius: 0px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(6, 444, 31, 20))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.sw_nav_bar = QStackedWidget(self.centralwidget)
        self.sw_nav_bar.setObjectName(u"sw_nav_bar")
        self.sw_nav_bar.setEnabled(True)
        self.sw_nav_bar.setGeometry(QRect(220, 10, 571, 481))
        font1 = QFont()
        font1.setKerning(True)
        self.sw_nav_bar.setFont(font1)
        self.Interlocks = QWidget()
        self.Interlocks.setObjectName(u"Interlocks")
        self.label1 = QLabel(self.Interlocks)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(10, 70, 49, 16))
        font2 = QFont()
        font2.setBold(True)
        font2.setKerning(True)
        self.label1.setFont(font2)
        self.label_2 = QLabel(self.Interlocks)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 49, 16))
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.Interlocks)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 49, 16))
        self.label_3.setFont(font2)
        self.label_4 = QLabel(self.Interlocks)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 49, 16))
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.Interlocks)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 220, 61, 16))
        self.label_5.setFont(font2)
        self.le_fn_number = QLineEdit(self.Interlocks)
        self.le_fn_number.setObjectName(u"le_fn_number")
        self.le_fn_number.setGeometry(QRect(150, 70, 113, 22))
        self.le_customer = QLineEdit(self.Interlocks)
        self.le_customer.setObjectName(u"le_customer")
        self.le_customer.setGeometry(QRect(150, 100, 201, 22))
        self.le_firstname = QLineEdit(self.Interlocks)
        self.le_firstname.setObjectName(u"le_firstname")
        self.le_firstname.setGeometry(QRect(150, 130, 201, 22))
        self.le_lastname = QLineEdit(self.Interlocks)
        self.le_lastname.setObjectName(u"le_lastname")
        self.le_lastname.setGeometry(QRect(360, 130, 191, 22))
        self.cob_typ = QComboBox(self.Interlocks)
        self.cob_typ.addItem("")
        self.cob_typ.addItem("")
        self.cob_typ.addItem("")
        self.cob_typ.setObjectName(u"cob_typ")
        self.cob_typ.setGeometry(QRect(150, 190, 91, 22))
        self.cob_hardware = QComboBox(self.Interlocks)
        self.cob_hardware.addItem("")
        self.cob_hardware.addItem("")
        self.cob_hardware.addItem("")
        self.cob_hardware.setObjectName(u"cob_hardware")
        self.cob_hardware.setGeometry(QRect(150, 220, 91, 22))
        self.label_11 = QLabel(self.Interlocks)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 250, 131, 16))
        self.label_11.setFont(font2)
        self.cob_interlock_length = QComboBox(self.Interlocks)
        self.cob_interlock_length.addItem("")
        self.cob_interlock_length.addItem("")
        self.cob_interlock_length.setObjectName(u"cob_interlock_length")
        self.cob_interlock_length.setGeometry(QRect(150, 250, 51, 22))
        self.pb_start = QPushButton(self.Interlocks)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setEnabled(True)
        self.pb_start.setGeometry(QRect(10, 320, 131, 51))
        self.label_10 = QLabel(self.Interlocks)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 280, 61, 16))
        self.label_10.setFont(font2)
        self.cob_language = QComboBox(self.Interlocks)
        self.cob_language.addItem("")
        self.cob_language.setObjectName(u"cob_language")
        self.cob_language.setGeometry(QRect(150, 280, 69, 22))
        self.le_email = QLineEdit(self.Interlocks)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setGeometry(QRect(150, 160, 261, 22))
        self.label_15 = QLabel(self.Interlocks)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(50, 10, 430, 50))
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setKerning(True)
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_error = QLabel(self.Interlocks)
        self.lb_error.setObjectName(u"lb_error")
        self.lb_error.setGeometry(QRect(160, 360, 381, 91))
        self.lb_error.setFont(font2)
        self.lb_error.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_error.setWordWrap(True)
        self.le_project_name = QLineEdit(self.Interlocks)
        self.le_project_name.setObjectName(u"le_project_name")
        self.le_project_name.setGeometry(QRect(270, 70, 113, 22))
        self.label_6 = QLabel(self.Interlocks)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 220, 41, 21))
        self.label_6.setFont(font2)
        self.cob_safety = QComboBox(self.Interlocks)
        self.cob_safety.addItem("")
        self.cob_safety.addItem("")
        self.cob_safety.setObjectName(u"cob_safety")
        self.cob_safety.setGeometry(QRect(320, 220, 91, 22))
        self.le_phone = QLineEdit(self.Interlocks)
        self.le_phone.setObjectName(u"le_phone")
        self.le_phone.setGeometry(QRect(420, 160, 131, 22))
        self.sw_nav_bar.addWidget(self.Interlocks)
        self.SoO = QWidget()
        self.SoO.setObjectName(u"SoO")
        self.label_12 = QLabel(self.SoO)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 150, 341, 161))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setKerning(True)
        self.label_12.setFont(font4)
        self.label_16 = QLabel(self.SoO)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 10, 430, 50))
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.sw_nav_bar.addWidget(self.SoO)
        self.spare = QWidget()
        self.spare.setObjectName(u"spare")
        self.label_13 = QLabel(self.spare)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(120, 120, 341, 161))
        self.label_13.setFont(font4)
        self.label_17 = QLabel(self.spare)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 10, 430, 50))
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.sw_nav_bar.addWidget(self.spare)
        MainWindow.setCentralWidget(self.centralwidget)
        self.widget.raise_()
        self.pb_Schnittstellen.raise_()
        self.pb_SoO.raise_()
        self.pb_spare.raise_()
        self.sw_nav_bar.raise_()

        self.retranslateUi(MainWindow)

        self.sw_nav_bar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb_Schnittstellen.setText(QCoreApplication.translate("MainWindow", u"Schnittstellen", None))
        self.pb_SoO.setText(QCoreApplication.translate("MainWindow", u"SoO", None))
        self.pb_spare.setText(QCoreApplication.translate("MainWindow", u"spare", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">LIEBHERR</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>v0.0</p></body></html>", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"Projekt", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kunde", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Kontakt", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Anlage", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hardware", None))
#if QT_CONFIG(tooltip)
        self.le_fn_number.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_fn_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FN-Nummer", None))
        self.le_customer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"z.B. Mercedes-Benz AG", None))
        self.le_firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vorname", None))
        self.le_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nachname", None))
        self.cob_typ.setItemText(0, QCoreApplication.translate("MainWindow", u"ladeportal", None))
        self.cob_typ.setItemText(1, QCoreApplication.translate("MainWindow", u"phs", None))
        self.cob_typ.setItemText(2, QCoreApplication.translate("MainWindow", u"roboter", None))

        self.cob_hardware.setItemText(0, QCoreApplication.translate("MainWindow", u"profinet", None))
        self.cob_hardware.setItemText(1, QCoreApplication.translate("MainWindow", u"profibus", None))
        self.cob_hardware.setItemText(2, QCoreApplication.translate("MainWindow", u"hardwired", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"L\u00e4nge Interlock in Byte", None))
        self.cob_interlock_length.setItemText(0, QCoreApplication.translate("MainWindow", u"32", None))
        self.cob_interlock_length.setItemText(1, QCoreApplication.translate("MainWindow", u"64", None))

        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"Generiere Dokumente", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sprache", None))
        self.cob_language.setItemText(0, QCoreApplication.translate("MainWindow", u"Deutsch", None))

        self.le_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Schnittstellenbeschreibung", None))
        self.lb_error.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.le_project_name.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.le_project_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Projekt Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Safety", None))
        self.cob_safety.setItemText(0, QCoreApplication.translate("MainWindow", u"24-pol", None))
        self.cob_safety.setItemText(1, QCoreApplication.translate("MainWindow", u"Profisafe", None))

        self.le_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"not programmed yet", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Systembeschreibung", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"not programmed yet", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"spare", None))
    # retranslateUi

