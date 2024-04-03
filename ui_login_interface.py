# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_login_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from  Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(861, 479)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 30)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 9, 0)
        self.close_window_button = QPushButton(self.header)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(24, 24))
        self.close_window_button.setMaximumSize(QSize(24, 24))
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon)
        self.close_window_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close_window_button, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.horizontalLayout = QHBoxLayout(self.mainBody)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QCustomQStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#stackedWidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0.455, y1:0.46, x2:1, y2:1, stop:0 rgba(0, 128, 128, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-top-right-radius: 100px;\n"
"border-bottom-right-radius: 100px;}\n"
"\n"
"#stackedWidget *{\n"
"	background-color: transparent;}\n"
"")
        self.welcome_to_login_pg = QWidget()
        self.welcome_to_login_pg.setObjectName(u"welcome_to_login_pg")
        self.verticalLayout_3 = QVBoxLayout(self.welcome_to_login_pg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.welcome_to_login_pg)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.SplitVCursor))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.to_signup = QPushButton(self.frame)
        self.to_signup.setObjectName(u"to_signup")
        self.to_signup.setMinimumSize(QSize(100, 35))
        self.to_signup.setFont(font)
        self.to_signup.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.to_signup, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.welcome_to_login_pg)
        self.welcome_to_signup_pg = QWidget()
        self.welcome_to_signup_pg.setObjectName(u"welcome_to_signup_pg")
        self.verticalLayout_5 = QVBoxLayout(self.welcome_to_signup_pg)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.welcome_to_signup_pg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_6)

        self.to_login = QPushButton(self.frame_2)
        self.to_login.setObjectName(u"to_login")
        self.to_login.setMinimumSize(QSize(100, 35))
        self.to_login.setFont(font)
        self.to_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.to_login, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.welcome_to_signup_pg)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.stackedWidget_2 = QCustomQStackedWidget(self.mainBody)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pg = QWidget()
        self.login_pg.setObjectName(u"login_pg")
        self.verticalLayout_6 = QVBoxLayout(self.login_pg)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.login_pg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(250, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setFont(font)

        self.verticalLayout_7.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_7.addWidget(self.lineEdit_2)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8.setOpenExternalLinks(True)

        self.verticalLayout_7.addWidget(self.label_8)

        self.loginBtn = QPushButton(self.frame_4)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(150, 35))
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.loginBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.google = QPushButton(self.frame_8)
        self.google.setObjectName(u"google")
        self.google.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_brands/icons/font_awesome/brands/google-plus-g.png", QSize(), QIcon.Normal, QIcon.Off)
        self.google.setIcon(icon1)
        self.google.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.google)

        self.twitter = QPushButton(self.frame_8)
        self.twitter.setObjectName(u"twitter")
        self.twitter.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_brands/icons/font_awesome/brands/x-twitter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.twitter.setIcon(icon2)
        self.twitter.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.twitter)

        self.facebook = QPushButton(self.frame_8)
        self.facebook.setObjectName(u"facebook")
        self.facebook.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/facebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.facebook.setIcon(icon3)
        self.facebook.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.facebook)

        self.instagram = QPushButton(self.frame_8)
        self.instagram.setObjectName(u"instagram")
        self.instagram.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/instagram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instagram.setIcon(icon4)
        self.instagram.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.instagram)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget_2.addWidget(self.login_pg)
        self.signup_pg = QWidget()
        self.signup_pg.setObjectName(u"signup_pg")
        self.verticalLayout_11 = QVBoxLayout(self.signup_pg)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.signup_pg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(250, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)

        self.verticalLayout_10.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.lineEdit_5)

        self.signUpBtn = QPushButton(self.frame_6)
        self.signUpBtn.setObjectName(u"signUpBtn")
        self.signUpBtn.setMinimumSize(QSize(150, 35))
        self.signUpBtn.setFont(font)
        self.signUpBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.signUpBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.google_2 = QPushButton(self.frame_7)
        self.google_2.setObjectName(u"google_2")
        self.google_2.setIcon(icon1)
        self.google_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.google_2)

        self.twitter_2 = QPushButton(self.frame_7)
        self.twitter_2.setObjectName(u"twitter_2")
        self.twitter_2.setIcon(icon2)
        self.twitter_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.twitter_2)

        self.facebook_2 = QPushButton(self.frame_7)
        self.facebook_2.setObjectName(u"facebook_2")
        self.facebook_2.setIcon(icon3)
        self.facebook_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.facebook_2)

        self.instagram_2 = QPushButton(self.frame_7)
        self.instagram_2.setObjectName(u"instagram_2")
        self.instagram_2.setIcon(icon4)
        self.instagram_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.instagram_2)


        self.verticalLayout_9.addWidget(self.frame_7)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.stackedWidget_2.addWidget(self.signup_pg)

        self.horizontalLayout.addWidget(self.stackedWidget_2)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_window_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Hi, Welcome!!</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter your details to login or login with social media apps.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Not registered? Click below button to register.", None))
        self.to_signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Hi, Welcome!!</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Enter your details to register, You can also register using the social media apps.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Already registered? Click below button to login.", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Sign In</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"google.com\"><span style=\" text-decoration: underline; color:#0063b1;\">Forgot Password</span></a></p></body></html>", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Or Login with social media", None))
        self.google.setText("")
        self.twitter.setText("")
        self.facebook.setText("")
        self.instagram.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Sign Up</span></p></body></html>", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.signUpBtn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Or Register with social media", None))
        self.google_2.setText("")
        self.twitter_2.setText("")
        self.facebook_2.setText("")
        self.instagram_2.setText("")
    # retranslateUi

