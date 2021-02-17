# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regiscorr.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
import subprocess

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import FigureCanvas
else:
    from matplotlib.backends.backend_qt4agg import FigureCanvas

from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(530, 10, 781, 451))
        self.groupBox.setObjectName("groupBox")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 310, 91, 21))
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 460, 71, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 430, 121, 21))
        self.label_19.setObjectName("label_19")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 131, 21))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 121, 21))
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 340, 71, 21))
        self.label_12.setObjectName("label_12")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 550, 241, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_52 = QtWidgets.QLabel(self.groupBox_5)
        self.label_52.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_5)
        self.label_53.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_5)
        self.label_54.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_54.setObjectName("label_54")
        self.textEdit_67 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_67.setGeometry(QtCore.QRect(120, 20, 110, 20))
        self.textEdit_67.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_67.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_67.setObjectName("textEdit_67")
        self.textEdit_66 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_66.setGeometry(QtCore.QRect(120, 50, 110, 20))
        self.textEdit_66.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_66.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_66.setObjectName("textEdit_66")
        self.textEdit_65 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_65.setGeometry(QtCore.QRect(120, 80, 110, 20))
        self.textEdit_65.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_65.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_65.setObjectName("textEdit_65")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 370, 121, 21))
        self.label_13.setObjectName("label_13")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 490, 71, 21))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(10, 400, 111, 21))
        self.label_21.setObjectName("label_21")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 121, 21))
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 101, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 71, 21))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 121, 21))
        self.label_6.setObjectName("label_6")
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        self.label_59.setGeometry(QtCore.QRect(20, 650, 271, 41))
        self.label_59.setObjectName("label_59")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(20, 680, 201, 16))
        self.label_58.setObjectName("label_58")
        self.textEdit_48 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_48.setGeometry(QtCore.QRect(140, 10, 110, 20))
        self.textEdit_48.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_48.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_48.setObjectName("textEdit_48")
        self.textEdit_49 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_49.setGeometry(QtCore.QRect(140, 40, 110, 20))
        self.textEdit_49.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_49.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_49.setObjectName("textEdit_49")
        self.textEdit_50 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_50.setGeometry(QtCore.QRect(140, 70, 110, 20))
        self.textEdit_50.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_50.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_50.setObjectName("textEdit_50")
        self.textEdit_51 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_51.setGeometry(QtCore.QRect(140, 100, 110, 20))
        self.textEdit_51.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_51.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_51.setObjectName("textEdit_51")
        self.textEdit_52 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_52.setGeometry(QtCore.QRect(140, 130, 110, 20))
        self.textEdit_52.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_52.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_52.setObjectName("textEdit_52")
        self.textEdit_53 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_53.setGeometry(QtCore.QRect(140, 190, 110, 20))
        self.textEdit_53.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_53.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_53.setObjectName("textEdit_53")
        self.textEdit_54 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_54.setGeometry(QtCore.QRect(140, 220, 110, 20))
        self.textEdit_54.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_54.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_54.setObjectName("textEdit_54")
        self.textEdit_55 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_55.setGeometry(QtCore.QRect(140, 160, 110, 20))
        self.textEdit_55.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_55.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_55.setObjectName("textEdit_55")
        self.textEdit_56 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_56.setGeometry(QtCore.QRect(140, 250, 110, 20))
        self.textEdit_56.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_56.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_56.setObjectName("textEdit_56")
        self.textEdit_57 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_57.setGeometry(QtCore.QRect(140, 310, 110, 20))
        self.textEdit_57.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_57.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_57.setObjectName("textEdit_57")
        self.textEdit_58 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_58.setGeometry(QtCore.QRect(140, 340, 110, 20))
        self.textEdit_58.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_58.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_58.setObjectName("textEdit_58")
        self.textEdit_59 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_59.setGeometry(QtCore.QRect(140, 280, 110, 20))
        self.textEdit_59.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_59.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_59.setObjectName("textEdit_59")
        self.textEdit_60 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_60.setGeometry(QtCore.QRect(140, 370, 110, 20))
        self.textEdit_60.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_60.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_60.setObjectName("textEdit_60")
        self.textEdit_61 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_61.setGeometry(QtCore.QRect(140, 430, 110, 20))
        self.textEdit_61.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_61.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_61.setObjectName("textEdit_61")
        self.textEdit_62 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_62.setGeometry(QtCore.QRect(140, 460, 110, 20))
        self.textEdit_62.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_62.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_62.setObjectName("textEdit_62")
        self.textEdit_63 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_63.setGeometry(QtCore.QRect(140, 400, 110, 20))
        self.textEdit_63.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_63.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_63.setObjectName("textEdit_63")
        self.textEdit_64 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_64.setGeometry(QtCore.QRect(140, 490, 110, 20))
        self.textEdit_64.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_64.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_64.setObjectName("textEdit_64")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(590, 1040, 241, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_34 = QtWidgets.QLabel(self.groupBox_3)
        self.label_34.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_34.setObjectName("label_34")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_33.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_34.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox_3)
        self.label_36.setGeometry(QtCore.QRect(10, 100, 81, 31))
        self.label_36.setObjectName("label_36")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_35.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_36.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_37.setObjectName("label_37")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_37.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_38.setObjectName("label_38")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(590, 850, 241, 181))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_28.setObjectName("label_28")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_28.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_29.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_29.setObjectName("label_29")
        self.label_32 = QtWidgets.QLabel(self.groupBox_4)
        self.label_32.setGeometry(QtCore.QRect(10, 100, 81, 31))
        self.label_32.setObjectName("label_32")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_30.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_31.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_39 = QtWidgets.QLabel(self.groupBox_4)
        self.label_39.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_39.setObjectName("label_39")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_32.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label_40 = QtWidgets.QLabel(self.groupBox_4)
        self.label_40.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_40.setObjectName("label_40")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(590, 1230, 241, 111))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_43 = QtWidgets.QLabel(self.groupBox_6)
        self.label_43.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_43.setObjectName("label_43")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_43.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_44.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.label_44 = QtWidgets.QLabel(self.groupBox_6)
        self.label_44.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_44.setObjectName("label_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_45.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_6)
        self.label_46.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_46.setObjectName("label_46")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(280, 10, 241, 181))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_27.setObjectName("label_27")
        self.label_41 = QtWidgets.QLabel(self.groupBox_7)
        self.label_41.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_7)
        self.label_42.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.label_42.setObjectName("label_42")
        self.label_45 = QtWidgets.QLabel(self.groupBox_7)
        self.label_45.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_45.setObjectName("label_45")
        self.label_47 = QtWidgets.QLabel(self.groupBox_7)
        self.label_47.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_47.setObjectName("label_47")
        self.textEdit_72 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_72.setGeometry(QtCore.QRect(110, 50, 110, 20))
        self.textEdit_72.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_72.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_72.setObjectName("textEdit_72")
        self.textEdit_71 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_71.setGeometry(QtCore.QRect(110, 110, 110, 20))
        self.textEdit_71.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_71.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_71.setObjectName("textEdit_71")
        self.textEdit_69 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_69.setGeometry(QtCore.QRect(110, 140, 110, 20))
        self.textEdit_69.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_69.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_69.setObjectName("textEdit_69")
        self.textEdit_70 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_70.setGeometry(QtCore.QRect(110, 80, 110, 20))
        self.textEdit_70.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_70.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_70.setObjectName("textEdit_70")
        self.textEdit_68 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_68.setGeometry(QtCore.QRect(110, 20, 110, 20))
        self.textEdit_68.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_68.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_68.setObjectName("textEdit_68")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(280, 380, 241, 181))
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_82 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_82.setGeometry(QtCore.QRect(110, 50, 110, 20))
        self.textEdit_82.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_82.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_82.setObjectName("textEdit_82")
        self.textEdit_78 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_78.setGeometry(QtCore.QRect(110, 20, 110, 20))
        self.textEdit_78.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_78.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_78.setObjectName("textEdit_78")
        self.textEdit_81 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_81.setGeometry(QtCore.QRect(110, 110, 110, 20))
        self.textEdit_81.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_81.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_81.setObjectName("textEdit_81")
        self.textEdit_80 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_80.setGeometry(QtCore.QRect(110, 80, 110, 20))
        self.textEdit_80.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_80.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_80.setObjectName("textEdit_80")
        self.textEdit_79 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_79.setGeometry(QtCore.QRect(110, 140, 110, 20))
        self.textEdit_79.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_79.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_79.setObjectName("textEdit_79")
        self.label_57 = QtWidgets.QLabel(self.groupBox_8)
        self.label_57.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.label_57.setObjectName("label_57")
        self.label_31 = QtWidgets.QLabel(self.groupBox_8)
        self.label_31.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_31.setObjectName("label_31")
        self.label_55 = QtWidgets.QLabel(self.groupBox_8)
        self.label_55.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_8)
        self.label_56.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_56.setObjectName("label_56")
        self.label_48 = QtWidgets.QLabel(self.groupBox_8)
        self.label_48.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_48.setObjectName("label_48")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(280, 190, 241, 181))
        self.groupBox_9.setObjectName("groupBox_9")
        self.textEdit_73 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_73.setGeometry(QtCore.QRect(110, 20, 110, 20))
        self.textEdit_73.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_73.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_73.setObjectName("textEdit_73")
        self.textEdit_74 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_74.setGeometry(QtCore.QRect(110, 140, 110, 20))
        self.textEdit_74.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_74.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_74.setObjectName("textEdit_74")
        self.textEdit_75 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_75.setGeometry(QtCore.QRect(110, 80, 110, 20))
        self.textEdit_75.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_75.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_75.setObjectName("textEdit_75")
        self.textEdit_76 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_76.setGeometry(QtCore.QRect(110, 110, 110, 20))
        self.textEdit_76.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_76.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_76.setObjectName("textEdit_76")
        self.textEdit_77 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_77.setGeometry(QtCore.QRect(110, 50, 110, 20))
        self.textEdit_77.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_77.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_77.setObjectName("textEdit_77")
        self.label_61 = QtWidgets.QLabel(self.groupBox_9)
        self.label_61.setGeometry(QtCore.QRect(10, 100, 91, 31))
        self.label_61.setObjectName("label_61")
        self.label_51 = QtWidgets.QLabel(self.groupBox_9)
        self.label_51.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_51.setObjectName("label_51")
        self.label_49 = QtWidgets.QLabel(self.groupBox_9)
        self.label_49.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_9)
        self.label_50.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_50.setObjectName("label_50")
        self.label_30 = QtWidgets.QLabel(self.groupBox_9)
        self.label_30.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_30.setObjectName("label_30")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(280, 570, 241, 111))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_66 = QtWidgets.QLabel(self.groupBox_10)
        self.label_66.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.groupBox_10)
        self.label_67.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.groupBox_10)
        self.label_68.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_68.setObjectName("label_68")
        self.textEdit_85 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_85.setGeometry(QtCore.QRect(110, 80, 110, 20))
        self.textEdit_85.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_85.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_85.setObjectName("textEdit_85")
        self.textEdit_83 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_83.setGeometry(QtCore.QRect(110, 50, 110, 20))
        self.textEdit_83.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_83.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_83.setObjectName("textEdit_83")
        self.textEdit_84 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_84.setGeometry(QtCore.QRect(110, 20, 110, 20))
        self.textEdit_84.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_84.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_84.setObjectName("textEdit_84")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(530, 500, 281, 181))
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_69 = QtWidgets.QLabel(self.groupBox_11)
        self.label_69.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_11)
        self.label_70.setGeometry(QtCore.QRect(10, 40, 141, 31))
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.groupBox_11)
        self.label_71.setGeometry(QtCore.QRect(10, 70, 161, 31))
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.groupBox_11)
        self.label_72.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.groupBox_11)
        self.label_73.setGeometry(QtCore.QRect(10, 130, 141, 31))
        self.label_73.setObjectName("label_73")
        self.textEdit_90 = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_90.setGeometry(QtCore.QRect(170, 140, 110, 20))
        self.textEdit_90.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_90.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_90.setObjectName("textEdit_90")
        self.textEdit_87 = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_87.setGeometry(QtCore.QRect(170, 20, 110, 20))
        self.textEdit_87.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_87.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_87.setObjectName("textEdit_87")
        self.textEdit_88 = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_88.setGeometry(QtCore.QRect(170, 110, 110, 20))
        self.textEdit_88.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_88.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_88.setObjectName("textEdit_88")
        self.textEdit_89 = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_89.setGeometry(QtCore.QRect(170, 80, 110, 20))
        self.textEdit_89.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_89.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_89.setObjectName("textEdit_89")
        self.textEdit_86 = QtWidgets.QTextEdit(self.groupBox_11)
        self.textEdit_86.setGeometry(QtCore.QRect(170, 50, 110, 20))
        self.textEdit_86.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_86.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_86.setObjectName("textEdit_86")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(990, 470, 321, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.label_74 = QtWidgets.QLabel(self.centralwidget)
        self.label_74.setGeometry(QtCore.QRect(830, 450, 71, 21))
        self.label_74.setText("")
        self.label_74.setPixmap(QtGui.QPixmap("aaaaaaaaa.png"))
        self.label_74.setScaledContents(True)
        self.label_74.setObjectName("label_74")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 470, 171, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 470, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 630, 71, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(900, 590, 81, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(910, 550, 31, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(870, 470, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 510, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 550, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(950, 510, 31, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(910, 510, 31, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(950, 470, 31, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 590, 71, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(910, 470, 31, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(950, 550, 31, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_75 = QtWidgets.QLabel(self.centralwidget)
        self.label_75.setGeometry(QtCore.QRect(820, 470, 51, 31))
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.centralwidget)
        self.label_76.setGeometry(QtCore.QRect(820, 510, 51, 31))
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.centralwidget)
        self.label_77.setGeometry(QtCore.QRect(820, 550, 51, 31))
        self.label_77.setObjectName("label_77")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(900, 630, 81, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.textEdit_91 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_91.setGeometry(QtCore.QRect(140, 520, 110, 20))
        self.textEdit_91.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_91.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_91.setObjectName("textEdit_91")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 520, 111, 21))
        self.label_22.setObjectName("label_22")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.plotFigLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.plot_static_canvas = FigureCanvas(Figure(figsize=(2, 3)))
        self.plotFigLayout.addWidget(self.plot_static_canvas)

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        self.pushButton.clicked.connect(lambda:self.plotvn())
        self.pushButton_14.clicked.connect(lambda:self.plotmanobra())
        self.pushButton_2.clicked.connect(lambda:self.plotiem('F','./output_aileron.txt', 'aileron'))
        self.pushButton_8.clicked.connect(lambda:self.plotiem('M','./output_aileron.txt', 'aileron'))
        self.pushButton_4.clicked.connect(lambda:self.plotiem('F','./output_profundor.txt', 'profundor'))
        self.pushButton_10.clicked.connect(lambda:self.plotiem('M','./output_profundor.txt', 'profundor'))
        self.pushButton_3.clicked.connect(lambda:self.plotiem('F','./output_cacetinhodearrasto.txt', 'Leme'))
        self.pushButton_9.clicked.connect(lambda:self.plotiem('M','./output_cacetinhodearrasto.txt', 'Leme'))
        self.pushButton_5.clicked.connect(lambda:self.plot_nerv('extradorso', './dados_x_extradorso.txt','./output_cpextradorso.txt' ))
        self.pushButton_6.clicked.connect(lambda:self.plot_nerv('intradorso', './dados_x_intradorso.txt', './output_cpintradorso.txt' ))
        self.pushButton_12.clicked.connect(lambda:self.plotcp3d('leme','./output_cp_cacetinho.txt'))
        self.pushButton_11.clicked.connect(lambda:self.plotcp3d('profundor','./output_cp_profundor.txt'))
        self.pushButton_15.clicked.connect(lambda:self.cargasa())
        self.pushButton_7.clicked.connect(lambda:self.pegar())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Plot"))
        self.label_11.setText(_translate("MainWindow", "Altura da asa (m)"))
        self.label.setText(_translate("MainWindow", "n_max"))
        self.label_18.setText(_translate("MainWindow", "Prop. de peso"))
        self.label_19.setText(_translate("MainWindow", "Angulo de overturn (º)"))
        self.label_4.setText(_translate("MainWindow", "coef cl vs alpha (rads)"))
        self.label_5.setText(_translate("MainWindow", "corda média aerodinâmica"))
        self.label_7.setText(_translate("MainWindow", "Vel. de rajada max (m/s)"))
        self.label_12.setText(_translate("MainWindow", "RHO (kg/m^2)"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Estabilizador Vertical"))
        self.label_52.setText(_translate("MainWindow", "corda na ponta (m)"))
        self.label_53.setText(_translate("MainWindow", "corda na raiz (m)"))
        self.label_54.setText(_translate("MainWindow", "Envergadura (m)"))
        self.label_13.setText(_translate("MainWindow", "Area de referencia (m^2)"))
        self.label_2.setText(_translate("MainWindow", "n_min"))
        self.label_20.setText(_translate("MainWindow", "FS"))
        self.label_21.setText(_translate("MainWindow", "Angulo de tipback (º)"))
        self.label_8.setText(_translate("MainWindow", "Envergadura da asa (m)"))
        self.label_3.setText(_translate("MainWindow", "TOW (kg)"))
        self.label_9.setText(_translate("MainWindow", "Area de asa (m^2)"))
        self.label_10.setText(_translate("MainWindow", "CL"))
        self.label_6.setText(_translate("MainWindow", "Vel. de rajada min (m/s)"))
        self.label_59.setText(_translate("MainWindow", "Desenvolvido por: Geraldo Majella Nunes Junior"))
        self.label_58.setText(_translate("MainWindow", "Email de contato: thiacene@gmail.com"))
        self.groupBox_3.setTitle(_translate("MainWindow", "cacetinho de arrasto"))
        self.label_34.setText(_translate("MainWindow", "corda na ponta"))
        self.label_35.setText(_translate("MainWindow", "corda na raiz"))
        self.label_36.setText(_translate("MainWindow", "Hinge da ponta"))
        self.label_37.setText(_translate("MainWindow", "Envergadura"))
        self.label_38.setText(_translate("MainWindow", "Hinge da raiz"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Profundor"))
        self.label_28.setText(_translate("MainWindow", "corda na ponta"))
        self.label_29.setText(_translate("MainWindow", "corda na raiz"))
        self.label_32.setText(_translate("MainWindow", "Hinge da ponta"))
        self.label_39.setText(_translate("MainWindow", "Envergadura"))
        self.label_40.setText(_translate("MainWindow", "Hinge da raiz"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Estabilizador Horizontal"))
        self.label_43.setText(_translate("MainWindow", "corda na ponta"))
        self.label_44.setText(_translate("MainWindow", "corda na raiz"))
        self.label_46.setText(_translate("MainWindow", "Envergadura"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Aileron"))
        self.label_27.setText(_translate("MainWindow", "corda na ponta (m)"))
        self.label_41.setText(_translate("MainWindow", "corda na raiz (m)"))
        self.label_42.setText(_translate("MainWindow", "Hinge da ponta (m)"))
        self.label_45.setText(_translate("MainWindow", "Envergadura (m)"))
        self.label_47.setText(_translate("MainWindow", "Hinge da raiz (m)"))
        self.groupBox_8.setTitle(_translate("MainWindow", "cacetinho de arrasto"))
        self.label_57.setText(_translate("MainWindow", "Hinge da ponta (m)"))
        self.label_31.setText(_translate("MainWindow", "corda na ponta (m)"))
        self.label_55.setText(_translate("MainWindow", "corda na raiz (m)"))
        self.label_56.setText(_translate("MainWindow", "Envergadura (m)"))
        self.label_48.setText(_translate("MainWindow", "Hinge da raiz (m)"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Profundor"))
        self.label_61.setText(_translate("MainWindow", "Hinge da ponta (m)"))
        self.label_51.setText(_translate("MainWindow", "Envergadura (m)"))
        self.label_49.setText(_translate("MainWindow", "Hinge da raiz (m)"))
        self.label_50.setText(_translate("MainWindow", "corda na raiz (m)"))
        self.label_30.setText(_translate("MainWindow", "corda na ponta (m)"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Estabilizador Horizontal"))
        self.label_66.setText(_translate("MainWindow", "corda na ponta (m)"))
        self.label_67.setText(_translate("MainWindow", "corda na raiz (m)"))
        self.label_68.setText(_translate("MainWindow", "Envergadura (m)"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Dados da nervura"))
        self.label_69.setText(_translate("MainWindow", "Espessura da nervura (m)"))
        self.label_70.setText(_translate("MainWindow", "Distancia entre nervuras (m)"))
        self.label_71.setText(_translate("MainWindow", "Comprimento do extradorso (m)"))
        self.label_72.setText(_translate("MainWindow", "Comprimento do intradorso (m)"))
        self.label_73.setText(_translate("MainWindow", "Velocidade de análise (m/s)"))
        self.pushButton_7.setText(_translate("MainWindow", "CALCULAR!"))
        self.pushButton.setText(_translate("MainWindow", "Plot: Diagrama v-n"))
        self.pushButton_5.setText(_translate("MainWindow", " extradorso"))
        self.pushButton_14.setText(_translate("MainWindow", "Manobra"))
        self.pushButton_10.setText(_translate("MainWindow", "(M)"))
        self.pushButton_2.setText(_translate("MainWindow", "(F)"))
        self.pushButton_3.setText(_translate("MainWindow", "(F)"))
        self.pushButton_4.setText(_translate("MainWindow", "(F)"))
        self.pushButton_12.setText(_translate("MainWindow", "cp"))
        self.pushButton_9.setText(_translate("MainWindow", "(M)"))
        self.pushButton_13.setText(_translate("MainWindow", "cp"))
        self.pushButton_6.setText(_translate("MainWindow", " intradorso"))
        self.pushButton_8.setText(_translate("MainWindow", "(M)"))
        self.pushButton_11.setText(_translate("MainWindow", "cp"))
        self.label_75.setText(_translate("MainWindow", "Aileron"))
        self.label_76.setText(_translate("MainWindow", "Leme"))
        self.label_77.setText(_translate("MainWindow", "Profundor"))
        self.pushButton_15.setText(_translate("MainWindow", "Carga na asa"))
        self.label_22.setText(_translate("MainWindow", "Afilamento da asa"))


    def pegar(self):

        self.analise = []
        self.aileron = []
        self.profundor = []
        self.cacete = []
        self.EV = []
        self.EH = []
        self.TDP = []
        self.nervura =[]
        self.intradorso = []
        self.extradorso = []
        self.canolli = []

        fileID = open('./dados_analise.txt','r')
        self.analise = fileID.read().splitlines()
        fileID.close() 
        ####

        fileID = open('./i_aileron.txt','r')
        self.aileron = fileID.read().splitlines()
        fileID.close() 
        ####

        fileID = open('./i_profundor.txt','r')
        self.profundor= fileID.read().splitlines()
        fileID.close() 
        ####

        fileID = open('./i_cacetinhodearrasto.txt','r')
        self.cacete= fileID.read().splitlines()
        fileID.close() 
        ####

        fileID = open('./i_EV.txt','r')
        self.EV= fileID.read().splitlines()
        fileID.close() 
        ###

        fileID = open('./i_EH.txt','r')
        self.EH= fileID.read().splitlines()
        fileID.close() 
        ###

        fileID = open('./dados_tremdepouso.txt','r')
        self.TDP= fileID.read().splitlines()
        fileID.close() 
        ###

        fileID = open('./dados_nervura.txt','r')
        self.nervura= fileID.read().splitlines()
        fileID.close() 
        ###

        fileID = open('./dados_intradorso.txt','r')
        self.intradorso= fileID.read().splitlines()
        fileID.close() 
        ###

        fileID = open('./dados_extradorso.txt','r')
        self.extradorso= fileID.read().splitlines()
        fileID.close() 
        ###

        fileID = open('./dados_aerodinamicos.txt','r')
        self.canolli= fileID.read().splitlines()
        fileID.close() 

        self.calc()
        return
    
    def calc(self):

        if True:
            try: 
                self.afilamento = float(self.textEdit_91.toPlainText())
            except : 
                self.afilamento = 0.8
                self.textEdit_91.insertPlainText(str(self.afilamento))
            try: 
                self.c_ponta_ail = float(self.textEdit_68.toPlainText())
                self.aileron[0] = self.c_ponta_ail
            except : 
                self.c_ponta_ail = self.aileron[0]
                self.textEdit_68.insertPlainText(str(self.c_ponta_ail))
            try: 
                self.c_raiz_ail = float(self.textEdit_72.toPlainText())
                self.aileron[1] = self.c_raiz_ail
            except : 
                self.c_raiz_ail = self.aileron[1]
                self.textEdit_72.insertPlainText(str(self.c_raiz_ail))
            try: 
                self.enver_ail = float(self.textEdit_70.toPlainText())
                self.aileron[4] = self.enver_ail
            except : 
                self.enver_ail = self.aileron[4]
                self.textEdit_70.insertPlainText(str(self.enver_ail))
            try: 
                self.hinge_tip_ail = float(self.textEdit_71.toPlainText())
                self.aileron[2] = self.hinge_tip_ail
            except : 
                self.hinge_tip_ail = self.aileron[2]
                self.textEdit_71.insertPlainText(str(self.hinge_tip_ail))
            try: 
                self.hinge_raiz_ail = float(self.textEdit_69.toPlainText())
                self.aileron[3] = self.hinge_raiz_ail
            except : 
                self.hinge_raiz_ail = self.aileron[3]
                self.textEdit_69.insertPlainText(str(self.hinge_raiz_ail))
###
            try: 
                self.c_ponta_prof = float(self.textEdit_73.toPlainText())
                self.profundor[0] = self.c_ponta_prof
            except : 
                self.c_ponta_prof = self.profundor[0] 
                self.textEdit_73.insertPlainText(str(self.c_ponta_prof))
            try: 
                self.c_raiz_prof = float(self.textEdit_77.toPlainText())
                self.profundor[1] = self.c_raiz_prof
            except : 
                self.c_raiz_prof = self.profundor[1]
                self.textEdit_77.insertPlainText(str(self.c_raiz_prof))
            try: 
                self.enver_prof = float(self.textEdit_75.toPlainText())
                self.profundor[4] = self.enver_prof
            except : 
                self.enver_prof = self.profundor[4]
                self.textEdit_75.insertPlainText(str(self.enver_prof))
            try: 
                self.hinge_tip_prof = float(self.textEdit_76.toPlainText())
                self.profundor[2] = self.hinge_tip_prof
            except : 
                self.hinge_tip_prof = self.profundor[2]
                self.textEdit_76.insertPlainText(str(self.hinge_tip_prof))
            try: 
                self.hinge_raiz_prof = float(self.textEdit_74.toPlainText())
                self.profundor[3] = self.hinge_raiz_prof
            except : 
                self.hinge_raiz_prof = self.profundor[3]
                self.textEdit_74.insertPlainText(str(self.hinge_raiz_prof))
###
            try: 
                self.c_ponta_cethi = float(self.textEdit_78.toPlainText())
                self.cacete[0] = self.c_ponta_cethi
            except : 
                self.c_ponta_cethi = self.cacete[0]
                self.textEdit_78.insertPlainText(str(self.c_ponta_cethi))
            try: 
                self.c_raiz_cethi = float(self.textEdit_82.toPlainText())
                self.cacete[1] = self.c_raiz_cethi
            except : 
                self.c_raiz_cethi = self.cacete[1]
                self.textEdit_82.insertPlainText(str(self.c_raiz_cethi))
            try: 
                self.enver_cethi = float(self.textEdit_80.toPlainText())
                self.cacete[4] = self.enver_cethi
            except : 
                self.enver_cethi = self.cacete[4]
                self.textEdit_80.insertPlainText(str(self.enver_cethi))
            try: 
                self.hinge_tip_cethi = float(self.textEdit_81.toPlainText())
                self.cacete[2] = self.hinge_tip_cethi
            except : 
                self.hinge_tip_cethi = self.cacete[2]
                self.textEdit_81.insertPlainText(str(self.hinge_tip_cethi))
            try: 
                self.hinge_raiz_cethi = float(self.textEdit_79.toPlainText())
                self.cacete[3] = self.hinge_raiz_cethi
            except : 
                self.hinge_raiz_cethi = self.cacete[3]
                self.textEdit_79.insertPlainText(str(self.hinge_raiz_cethi))
####
            try: 
                self.c_tip_EH = float(self.textEdit_84.toPlainText())
                self.EH[0] = self.c_tip_EH
            except : 
                self.c_tip_EH = self.EH[0]
                self.textEdit_84.insertPlainText(str(self.c_tip_EH))

            try: 
                self.c_raiz_EH = float(self.textEdit_83.toPlainText())
                self.EH[1] = self.c_raiz_EH 
            except : 
                self.c_raiz_EH = self.EH[1]
                self.textEdit_83.insertPlainText(str(self.c_raiz_EH))

            try: 
                self.envergadura_EH = float(self.textEdit_85.toPlainText())
                self.EH[2] = self.envergadura_EH
            except : 
                self.envergadura_EH = self.EH[2]
                self.textEdit_85.insertPlainText(str(self.envergadura_EH))
###
            try: 
                self.c_tip_EV = float(self.textEdit_67.toPlainText())
                self.EV[0] = self.c_tip_EV
            except : 
                self.c_tip_EV = self.EV[0]
                self.textEdit_67.insertPlainText(str(self.c_tip_EV))

            try: 
                self.c_raiz_EV = float(self.textEdit_66.toPlainText())
                self.EV[1] = self.c_raiz_EV
            except : 
                self.c_raiz_EV = self.EV[1]
                self.textEdit_66.insertPlainText(str(self.c_raiz_EV))

            try: 
                self.envergadura_EV = float(self.textEdit_65.toPlainText())
                self.EV[2] = self.envergadura_EV
            except : 
                self.envergadura_EV = self.EV[2]
                self.textEdit_65.insertPlainText(str(self.envergadura_EV))
###
            try: 
                self.nerv_esp = float(self.textEdit_87.toPlainText())
                self.nervura[0] = self.nerv_esp 
            except : 
                self.nerv_esp=self.nervura[0]
                self.textEdit_87.insertPlainText(str(self.nerv_esp))

            try: 
                self.nerv_d = float(self.textEdit_86.toPlainText())
                self.nervura[1] = self.nerv_d
            except : 
                self.nerv_d=self.nervura[1]
                self.textEdit_86.insertPlainText(str(self.nerv_d))

            try: 
                self.nerv_comp_ext = float(self.textEdit_89.toPlainText())
                self.nervura[2] = self.nerv_comp_ext
            except : 
                self.nerv_comp_ext=self.nervura[2]
                self.textEdit_89.insertPlainText(str(self.nerv_comp_ext))
            try: 
                self.nerv_comp_int = float(self.textEdit_88.toPlainText())
                self.nervura[3] = self.nerv_comp_int
            except : 
                self.nerv_comp_int=self.nervura[3]
                self.textEdit_88.insertPlainText(str(self.nerv_comp_int))
            try: 
                self.v_ana = float(self.textEdit_90.toPlainText())
                self.nervura[4] = self.v_ana
            except : 
                self.v_ana=self.nervura[4]
                self.textEdit_90.insertPlainText(str(self.v_ana))
###
            try: 
                self.n_max = float(self.textEdit_48.toPlainText())
                self.analise[0] = self.n_max
            except : 
                self.n_max=self.analise[0]
                self.textEdit_48.insertPlainText(str(self.n_max))

            try: 
                self.n_min = float(self.textEdit_49.toPlainText())
                self.analise[1] = self.n_min
            except : 
                self.n_min=self.analise[1]
                self.textEdit_49.insertPlainText(str(self.n_min))

            try: 
                self.TOW = float(self.textEdit_50.toPlainText())
                self.analise[2] = self.TOW
            except : 
                self.TOW=self.analise[2]
                self.textEdit_50.insertPlainText(str(self.TOW))
            try: 
                self.claplha = float(self.textEdit_51.toPlainText())
                self.analise[3] = self.claplha
            except : 
                self.claplha=self.analise[3]
                self.textEdit_51.insertPlainText(str(self.claplha))
            try: 
                self.c_media = float(self.textEdit_52.toPlainText())
                self.analise[4] = self.c_media
            except : 
                self.c_media=self.analise[4]
                self.textEdit_52.insertPlainText(str(self.c_media))
            try: 
                self.v_rajada_min = float(self.textEdit_55.toPlainText())
                self.analise[5] = self.v_rajada_min
            except : 
                self.v_rajada_min=self.analise[5]
                self.textEdit_55.insertPlainText(str(self.v_rajada_min))
            try: 
                self.v_rajada_max = float(self.textEdit_53.toPlainText())
                self.analise[6] = self.v_rajada_max
            except : 
                self.v_rajada_max=self.analise[6]
                self.textEdit_53.insertPlainText(str(self.v_rajada_max))
            ###
            try: 
                self.enverwing = float(self.textEdit_54.toPlainText())
                self.canolli[2] = self.enverwing
            except : 
                self.enverwing=self.canolli[2]
                self.textEdit_54.insertPlainText(str(self.enverwing))
            try: 
                self.area_wi = float(self.textEdit_56.toPlainText())
                self.canolli[3] = self.area_wi
            except : 
                self.area_wi=self.canolli[3]
                self.textEdit_56.insertPlainText(str(self.area_wi))
            try: 
                self.cl = float(self.textEdit_59.toPlainText())
                self.canolli[9] = self.cl 
            except : 
                self.cl=self.canolli[9]
                self.textEdit_59.insertPlainText(str(self.cl))

            try: 
                self.rho = float(self.textEdit_58.toPlainText())
                self.canolli[19] = self.rho
            except : 
                self.rho=self.canolli[19]
                self.textEdit_58.insertPlainText(str(self.rho))
            try: 
                self.A_ref = float(self.textEdit_60.toPlainText())
                self.canolli[20] = self.A_ref
            except : 
                self.A_ref=self.canolli[20]
                self.textEdit_60.insertPlainText(str(self.A_ref))
            #####
            try: 
                self.h_asa = float(self.textEdit_57.toPlainText())
                self.TDP[1] = self.h_asa 
            except : 
                self.h_asa=self.TDP[1]
                self.textEdit_57.insertPlainText(str(self.h_asa))
            try: 
                self.tip_angle = float(self.textEdit_63.toPlainText())
                self.TDP[0] = self.tip_angle
            except : 
                self.tip_angle=self.TDP[0]
                self.textEdit_63.insertPlainText(str(self.tip_angle))
            try: 
                self.over_angle = float(self.textEdit_61.toPlainText())
                self.TDP[3] = self.over_angle
            except : 
                self.over_angle=self.TDP[3]
                self.textEdit_61.insertPlainText(str(self.over_angle))
            try: 
                self.prop_gagliardi = float(self.textEdit_62.toPlainText())
                self.TDP[2] = self.prop_gagliardi
            except : 
                self.prop_gagliardi=self.TDP[2]
                self.textEdit_62.insertPlainText(str(self.prop_gagliardi))
            try: 
                self.FS = float(self.textEdit_64.toPlainText())
                self.TDP[4] = self.FS
            except : 
                self.FS=self.TDP[4]
                self.textEdit_64.insertPlainText(str(self.FS))
            
        self.JACARE_GIGANTESCO()


    def JACARE_GIGANTESCO(self):

        fileID = open('./dados_analise.txt','w')
        for i in range (len(self.analise)):
            fileID.write("%s \n" % self.analise[i])
        
        fileID.close()
        ####

        fileID = open('./i_aileron.txt','w')

        for i in range (len(self.aileron)):
            fileID.write("%s \n" % self.aileron[i])
        fileID.close()    
        ####

        fileID = open('./i_profundor.txt','w')
        

        for i in range (len(self.profundor)):
            fileID.write("%s \n" % self.profundor[i])
        fileID.close()    
        ####

        fileID = open('./i_cacetinhodearrasto.txt','w')
        

        for i in range (len(self.cacete)):
            fileID.write("%s \n" % self.cacete[i])
        fileID.close()    
        ####

        fileID = open('./i_EV.txt','w')
        

        for i in range (len(self.EV)):
            fileID.write("%s \n" % self.EV[i])
        fileID.close()    
        ###

        fileID = open('./i_EH.txt','w')
        
        for i in range (len(self.EH)):
            fileID.write("%s \n" % self.EH[i])
        fileID.close()    
        ###
        fileID = open('./dados_tremdepouso.txt','w')
        

        for i in range (len(self.TDP)):
            fileID.write("%s \n" % self.TDP[i])
        fileID.close()    
        ###
        fileID = open('./dados_nervura.txt','w')
        

        for i in range (len(self.nervura)):
            fileID.write("%s \n" % self.nervura[i])
        fileID.close()    
        ###
        fileID = open('./dados_intradorso.txt','w')
        

        for i in range (len(self.intradorso)):
            fileID.write("%s \n" % self.intradorso[i])
        fileID.close()    
        ###
        fileID = open('./dados_extradorso.txt','w')
        

        for i in range (len(self.extradorso)):
            fileID.write("%s \n" % self.extradorso[i])
        fileID.close()    
        ###
        fileID = open('./dados_aerodinamicos.txt','w')
        

        for i in range (len(self.canolli)):
            fileID.write("%s \n" % self.canolli[i])
        fileID.close()    

  
        subprocess.call(["./Reginaldo v1.2.exe"])
        self.textBrowser.append('Aguarde 2 segundos')
        #time.sleep(2)

        #proc = subprocess.Popen(["./src", 'Reginaldo v1.2.cpp'])
        #subprocess.call("./a.out")
        #proc.wait()

        self.TDP_a()
        return

    def cargasa(self):
        import numpy as np
        try:
            if self.n_max:
                indio=True
        except:
            self.pegar()
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        x = []
        y = []
        self.ax = self.fig.add_subplot(111)


        n = float(self.n_max)
        W = float(self.TOW)*9.81
        lambdi = float(self.afilamento)
        b = float(self.enverwing)

        x=[]
        a=[]
        bb=[]
        en=[]
        y=0
        for i in range(30):

            x.append(y)

            a.append(2*n*W/((1+lambdi)*b)*(1+(2*y/b*(lambdi-1))))
            bb.append(4*n*W/(3.1415*b)*np.sqrt(1-(2*y/b)**2))
            en.append((a[-1]+bb[-1])/2)

            y = y+ b/30

        self.ax.plot(x[0:15],a[0:15], label='Asa trapezoidal')
        self.ax.plot(x[0:15],bb[0:15], label='Asa elíptica')
        self.ax.plot(x,en, label='Média (aproximação de schrenk)')
        self.ax.set_title('Cacetinho de sustentar')
        self.ax.set_xlabel('posição na envergadura (m)')
        self.ax.set_ylabel('Sustentação (N/m)')
        self.ax.set_xlim(left=0, right=None)
        self.ax.grid()
        self.ax.legend()
        self.fig_canvas.draw()

    def plotcp3d(self, bbb, xx):
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        x = []
        points = []
        self.ax = self.fig.gca(projection='3d')
        
        fileID = open(xx,'r')
        x= fileID.read().splitlines()
        fileID.close()

        for i in range(len(x)):
            points.append(x[i].split())

        for i in range(len(points)):
            a = points[i]
            for j in range(len(a)):
                a[j] = float(a[j])
            points[i] = a

        X=[]
        Y=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
        try:
            if self.c_raiz_prof:
                pass
        except:
            self.pegar()
        ae=1/len(x)
        a=0
        for i in range(len(x)):
            a=a+ae
            X.append(a)
        for i in range(len(Y)):
            if bbb == 'profundor':
                Y[i] = Y[i]*float(self.c_raiz_prof)
            else:
                X[i] = X[i]*float(self.c_raiz_cethi)

        for i in range(len(X)):
            if bbb == 'profundor':
                X[i] = X[i]*float(self.enver_prof)
            else:
                X[i] = X[i]*float(self.enver_cethi)

        X,Y = np.meshgrid(Y,X)
        
        self.ax.contour3D(X,Y, points,175, cmap='binary')
        
        aaaa = 'Distribuição de pressão no'+' '+bbb
        self.ax.set_title(aaaa)
        self.ax.set_ylabel('Envergadura (m)')
        self.ax.set_xlabel('corda (m)')
        self.ax.set_zlabel('Pressão (Pa)')
        self.ax.grid()
        self.fig_canvas.draw()


    def TDP_a(self):
        fileID = open('./output_vels.txt','r')
        self.vels= fileID.read().splitlines()
        fileID = open('./output_ail.txt','r')
        self.aill= fileID.read().splitlines()
        fileID = open('./output_tin.txt','r')
        self.cetin= fileID.read().splitlines()
        fileID = open('./output_EVEH.txt','r')
        self.EVEH= fileID.read().splitlines()
        fileID = open('./output_pro.txt','r')
        self.pro= fileID.read().splitlines()
        fileID = open('./output_tremdepouso.txt','r')
        self.TTDP= fileID.read().splitlines()


        try: self.textBrowser.clear()
        except: pass
        for i in range(len(self.vels)):
            self.textBrowser.append(self.vels[i])
        
        for i in range(len(self.aill)):
            self.textBrowser.append(self.aill[i])
        
        for i in range(len(self.cetin)):
            self.textBrowser.append(self.cetin[i])
        
        for i in range(len(self.EVEH)):
            self.textBrowser.append(self.EVEH[i])
        
        for i in range(len(self.pro)):
            self.textBrowser.append(self.pro[i])
        
        self.textBrowser.append('\n')
        self.textBrowser.append('TREM DE POUSO')
        self.textBrowser.append('\n')

        for i in range(len(self.TTDP)):
            self.textBrowser.append(self.TTDP[i])
        
        return
    def plot_nerv(self, bbb, xx,yy):
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        x = []
        y = []
        self.ax = self.fig.add_subplot(111)

        fileID = open(xx,'r')
        x= fileID.read().splitlines()
        fileID.close()
        for i in range(len(x)):
            x[i]=float(x[i])
        fileID = open(yy,'r')
        y= fileID.read().splitlines()
        fileID.close()
        for i in range(len(y)):
            y[i]=float(y[i])
        
        self.ax.plot(x[2:],y[2:], color='green')
        aaaa = 'Distribuição de pressão no'+' '+bbb
        self.ax.set_title(aaaa)
        self.ax.set_xlabel('posição %')
        self.ax.set_ylabel('Pressão manométrica (Pa)')
        #self.ax.set_xlim(left=0, right=None)
        self.ax.grid()
        self.fig_canvas.draw()

    def plotiem(self,oque,rene,bbb):
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        x = []
        F = []
        M = []
        a = [0,0]
        b = [0,0]
        self.ax = self.fig.add_subplot(111)

        fileID = open(rene,'r')
        self.vn= fileID.read().splitlines()
        fileID.close()
        for i in range (len(self.vn)):
            ern = self.vn[i].split()
            x.append(float(ern[0]))
            F.append(float(ern[1]))
            M.append(float(ern[2]))
        
        if oque == 'F':
            a[0] = x[-1]
            b[0] = 0
            a[1] = x[-1]
            b[1] = F[-1]
            self.ax.plot(a,b, color='black')
            self.ax.plot(x,F, color='black')
            aaaa = 'Distribuição de força no'+' '+bbb
            self.ax.set_title(aaaa)
            self.ax.set_xlabel('posição (m)')
            self.ax.set_ylabel('Força (N/m)')
            self.ax.set_xlim(left=0, right=None)
            self.ax.set_ylim(bottom=0, top=2*max(F))
        else:
            a[0] = x[-1]
            b[0] = 0
            a[1] = x[-1]
            b[1] = M[-1]
            self.ax.plot(a,b, color='red')
            self.ax.plot(x,M, color='red')
            aaaa = 'Distribuição de momento no'+' '+bbb
            self.ax.set_title(aaaa)
            self.ax.set_xlabel('posição (m)')
            self.ax.set_ylabel('Momento (N/m2)')
            self.ax.set_xlim(left=0, right=None)
            self.ax.set_ylim(bottom=0, top=3*max(M))
        self.ax.grid()
        self.fig_canvas.draw()


    def plotvn(self):
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        
        self.ax = self.fig.add_subplot(111)

        fileID = open('./output_vnmsm.txt','r')
        self.vn= fileID.read().splitlines()
        fileID.close() 
        fsdtcurveV=[]
        fsdtcurveN=[]
        nsdtcurveV=[]
        nsdtcurveN=[]
        gg=0
        g=0
        x=False
        lig1V=[]
        lig1N=[]
        lig2V=[]
        lig2N=[]
        lig3V=[]
        lig3N=[]
        lig4V=[]
        lig4N=[]
        lig5V=[]
        lig5N=[]
        lig6V=[]
        lig6N=[]
        h1V=[]
        h1N=[]
        h2V=[]
        h2N=[]
        h3V=[]
        h3N=[]
        k=1000
        for i in range(len(self.vn)):
            if float(self.vn[i][8:]) > 0 and gg != 2:
                fsdtcurveV.append(float(self.vn[i][0:8]))
                fsdtcurveN.append(float(self.vn[i][8:]))
                
            if float(self.vn[i][8:]) < 0 and g != 3:
                nsdtcurveV.append(float(self.vn[i][0:8]))
                nsdtcurveN.append(float(self.vn[i][8:]))
                gg=2
            if float(self.vn[i][8:]) > 0 and gg ==2 and x == False:
                g=3
                k=0
                x = True
            if k==1:
                g=3
                lig5V.append(float(self.vn[i][0:8]))
                lig5N.append(float(self.vn[i][8:]))
            if k == 2 :
                lig5V.append(float(self.vn[i][0:8]))

            if k==6:
                lig1V.append(float(self.vn[i][0:8]))
                lig1N.append(float(self.vn[i][8:]))
                lig4V.append(float(self.vn[i][0:8]))
                lig4N.append(float(self.vn[i][8:]))

            if k==7:
                lig1V.append(float(self.vn[i][0:8]))
                lig1N.append(float(self.vn[i][8:]))
                lig6V.append(float(self.vn[i][0:8]))
            if k==8:
                lig4V.append(float(self.vn[i][0:8]))
                lig4N.append(float(self.vn[i][8:]))
                lig6N.append(float(self.vn[i][8:]))    
            if k==9:
                lig2V.append(float(self.vn[i][0:8]))
                lig2N.append(float(self.vn[i][8:]))
                lig3V.append(float(self.vn[i][0:8]))
                lig3N.append(float(self.vn[i][8:]))
            if k ==10:
                lig2V.append(float(self.vn[i][0:8]))
                lig6V.append(float(self.vn[i][0:8])) 
                lig2N.append(float(self.vn[i][8:]))
                lig5N.append(float(self.vn[i][8:]))
            if k ==11:
                lig3V.append(float(self.vn[i][0:8]))
                lig3N.append(float(self.vn[i][8:]))
                lig6N.append(float(self.vn[i][8:]))
            if k == 12 or k == 13:
                h3V.append(float(self.vn[i][0:8]))
                h3N.append(float(self.vn[i][8:]))
            if k == 14 or k == 15:
                h1V.append(float(self.vn[i][0:8]))
                h1N.append(float(self.vn[i][8:]))
            if k == 16 or k == 17:
                h2V.append(float(self.vn[i][0:8]))
                h2N.append(float(self.vn[i][8:]))

            k=k+1

        self.ax.plot(fsdtcurveV, fsdtcurveN,color='black')
        self.ax.plot(nsdtcurveV, nsdtcurveN,color='black')
        self.ax.plot(h1V, h1N,color='black')
        self.ax.plot(h2V, h2N,color='black')
        self.ax.plot(h3V, h3N,color='black')
        self.ax.plot(lig1V, lig1N, color='silver',ls='--')
        self.ax.plot(lig2V, lig2N, color='silver',ls='--')
        self.ax.plot(lig3V, lig3N, color='silver',ls='--')
        self.ax.plot(lig4V, lig4N, color='silver',ls='--')
        self.ax.plot(lig5V, lig5N, color='silver',ls='--')
        self.ax.plot(lig6V, lig6N, color='silver',ls='--')
        self.ax.set_title('Diagrama Vn')
        self.ax.set_xlabel('Velocidade (m/s)')
        self.ax.set_ylabel('Fator de carga (n)')
        self.ax.set_xlim(left=0, right=None)
        self.ax.grid()

        self.fig_canvas.draw()

    def plotmanobra(self):
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        
        self.ax = self.fig.add_subplot(111)

        fileID = open('./output_vn.txt','r')
        self.vnn= fileID.read().splitlines()
        fileID.close() 
        fsdtcurveV=[]
        fsdtcurveN=[]
        nsdtcurveV=[]
        nsdtcurveN=[]
        gg=0
        g=0
        x=False
        lig1V=[]
        lig1N=[]
        lig2V=[]
        lig2N=[]
        lig3V=[]
        lig3N=[]
        lig4V=[]
        lig4N=[]
        lig5V=[]
        lig5N=[]
        lig6V=[]
        lig6N=[]
        lig7V=[]
        lig7N=[]
        lig8V=[]
        lig8N=[]
        h1V=[]
        h1N=[]
        h2V=[]
        h2N=[]
        h3V=[]
        h3N=[]
        k=1000
        for i in range(len(self.vnn)):
            if float(self.vnn[i][8:]) > 0 and gg != 2:
                fsdtcurveV.append(float(self.vnn[i][0:8]))
                fsdtcurveN.append(float(self.vnn[i][8:]))
                
            if float(self.vnn[i][8:]) < 0 and g != 3:
                nsdtcurveV.append(float(self.vnn[i][0:8]))
                nsdtcurveN.append(float(self.vnn[i][8:]))
                gg=2
            if float(self.vnn[i][8:]) > 0 and gg ==2 and x == False:
                g=3
                k=0
                x = True
            if k==0:
                g=3
                lig1V.append(float(self.vnn[i][0:8]))
                lig1N.append(float(self.vnn[i][8:]))
            if k==1:
                lig1V.append(float(self.vnn[i][0:8]))
                lig1N.append(float(self.vnn[i][8:]))
                lig2V.append(float(self.vnn[i][0:8]))
                lig2N.append(float(self.vnn[i][8:]))
            if k == 2 :
                lig2V.append(float(self.vnn[i][0:8]))
                lig2N.append(float(self.vnn[i][8:]))
            if k == 3 :
                lig3V.append(float(self.vnn[i][0:8]))
                lig3N.append(float(self.vnn[i][8:]))
            if k == 4 :
                lig3V.append(float(self.vnn[i][0:8]))
                lig3N.append(float(self.vnn[i][8:]))
                lig4V.append(float(self.vnn[i][0:8]))
                lig4N.append(float(self.vnn[i][8:]))
            if k == 5 :
                lig4V.append(float(self.vnn[i][0:8]))
                lig4N.append(float(self.vnn[i][8:]))

            if k==6 :
                lig5V.append(float(self.vnn[i][0:8]))
                lig5N.append(float(self.vnn[i][8:]))
                lig8V.append(float(self.vnn[i][0:8]))
                lig8N.append(float(self.vnn[i][8:]))
            if k ==7:
                lig5V.append(float(self.vnn[i][0:8]))
                lig5N.append(float(self.vnn[i][8:]))
            if k ==8:
                lig8V.append(float(self.vnn[i][0:8]))
                lig8N.append(float(self.vnn[i][8:]))
            if k==9:
                lig6V.append(float(self.vnn[i][0:8]))
                lig6N.append(float(self.vnn[i][8:]))
                lig7V.append(float(self.vnn[i][0:8]))
                lig7N.append(float(self.vnn[i][8:])) 
            if k==10:
                lig6V.append(float(self.vnn[i][0:8]))
                lig6N.append(float(self.vnn[i][8:]))
            if k == 11:
                lig7V.append(float(self.vnn[i][0:8]))
                lig7N.append(float(self.vnn[i][8:])) 
            if k == 12 or k== 13:
                h1V.append(float(self.vnn[i][0:8]))
                h1N.append(float(self.vnn[i][8:]))
            if k == 14 or k== 15:
                h2V.append(float(self.vnn[i][0:8]))
                h2N.append(float(self.vnn[i][8:]))             
            if k == 16 or k== 17:
                h3V.append(float(self.vnn[i][0:8]))
                h3N.append(float(self.vnn[i][8:]))        


            k=k+1

        self.ax.plot(fsdtcurveV, fsdtcurveN,color='black')
        self.ax.plot(nsdtcurveV, nsdtcurveN,color='black')
        self.ax.plot(lig1V, lig1N, color='black')
        self.ax.plot(lig2V, lig2N, color='black')
        self.ax.plot(lig3V, lig3N, color='black')
        self.ax.plot(lig4V, lig4N, color='black')
        self.ax.plot(lig5V, lig5N, color='silver',ls='--')
        self.ax.plot(lig6V, lig6N, color='silver',ls='--')
        self.ax.plot(lig7V, lig7N, color='silver',ls='--')
        self.ax.plot(lig8V, lig8N, color='silver',ls='--')
        self.ax.plot(h1V, h1N, color='black',ls='--')
        self.ax.plot(h2V, h2N, color='black',ls='--')
        self.ax.plot(h3V, h3N, color='black')
        self.ax.set_title('Diagrama de manobra')
        self.ax.set_xlabel('Velocidade (m/s)')
        self.ax.set_ylabel('Fator de carga (n)')
        self.ax.set_xlim(left=0, right=None)
        self.ax.grid()

        self.fig_canvas.draw()



#if __name__ == "__main__":
def init():
    #import os
    import sys
    #import win32com.shell.shell as shell
    #ASADMIN = 'Geraldo'
    #if sys.argv[-1] != ASADMIN:
    #    script = os.path.abspath(sys.argv[0])
    #    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    #    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
