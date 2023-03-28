# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 678)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webMap = QtWebEngineWidgets.QWebEngineView(parent=self.centralwidget)
        self.webMap.setUrl(QtCore.QUrl("about:blank"))
        self.webMap.setObjectName("webMap")
        self.verticalLayout.addWidget(self.webMap)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbSportType = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbSportType.setEditable(False)
        self.cbSportType.setCurrentText("")
        self.cbSportType.setObjectName("cbSportType")
        self.horizontalLayout.addWidget(self.cbSportType)
        self.tbTitle = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tbTitle.setReadOnly(False)
        self.tbTitle.setObjectName("tbTitle")
        self.horizontalLayout.addWidget(self.tbTitle)
        self.btUpload = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btUpload.setObjectName("btUpload")
        self.horizontalLayout.addWidget(self.btUpload)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 32))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setCheckable(False)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOptions = QtGui.QAction(parent=MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionReload = QtGui.QAction(parent=MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionOptions)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FitTrackee Uploader"))
        self.tbTitle.setPlaceholderText(_translate("MainWindow", "Title"))
        self.btUpload.setText(_translate("MainWindow", "Upload"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
from PyQt6 import QtWebEngineWidgets
