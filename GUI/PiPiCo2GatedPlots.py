# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PiPiCo2GatedPlots.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PiPiCo2GatedPlots(object):
    def setupUi(self, PiPiCo2GatedPlots):
        PiPiCo2GatedPlots.setObjectName(_fromUtf8("PiPiCo2GatedPlots"))
        PiPiCo2GatedPlots.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PiPiCo2GatedPlots)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Tof = QtGui.QVBoxLayout()
        self.Tof.setObjectName(_fromUtf8("Tof"))
        self.verticalLayout_3.addLayout(self.Tof)
        self.XY = QtGui.QVBoxLayout()
        self.XY.setObjectName(_fromUtf8("XY"))
        self.verticalLayout_3.addLayout(self.XY)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.XT = QtGui.QVBoxLayout()
        self.XT.setObjectName(_fromUtf8("XT"))
        self.verticalLayout_7.addLayout(self.XT)
        self.YT = QtGui.QVBoxLayout()
        self.YT.setObjectName(_fromUtf8("YT"))
        self.verticalLayout_7.addLayout(self.YT)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.PiPiCo = QtGui.QVBoxLayout()
        self.PiPiCo.setObjectName(_fromUtf8("PiPiCo"))
        self.verticalLayout_4.addLayout(self.PiPiCo)
        self.eXY = QtGui.QVBoxLayout()
        self.eXY.setObjectName(_fromUtf8("eXY"))
        self.verticalLayout_4.addLayout(self.eXY)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        PiPiCo2GatedPlots.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PiPiCo2GatedPlots)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PiPiCo2GatedPlots.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PiPiCo2GatedPlots)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PiPiCo2GatedPlots.setStatusBar(self.statusbar)

        self.retranslateUi(PiPiCo2GatedPlots)
        QtCore.QMetaObject.connectSlotsByName(PiPiCo2GatedPlots)

    def retranslateUi(self, PiPiCo2GatedPlots):
        PiPiCo2GatedPlots.setWindowTitle(_translate("PiPiCo2GatedPlots", "PiPiCo2GatedPlots", None))

