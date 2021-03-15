# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaTemperaturaManual.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TemperaturaManual(object):
    def setupUi(self, TemperaturaManual):
        TemperaturaManual.setObjectName("TemperaturaManual")
        TemperaturaManual.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TemperaturaManual)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pB_medirTemp = QtWidgets.QPushButton(self.centralwidget)
        self.pB_medirTemp.setObjectName("pB_medirTemp")
        self.verticalLayout.addWidget(self.pB_medirTemp)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.sB_tref = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sB_tref.setMaximum(199.99)
        self.sB_tref.setObjectName("sB_tref")
        self.horizontalLayout.addWidget(self.sB_tref)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lcd_sensor = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_sensor.setObjectName("lcd_sensor")
        self.horizontalLayout.addWidget(self.lcd_sensor)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.ventanaPlot = PlotWidget(self.centralwidget)
        self.ventanaPlot.setObjectName("ventanaPlot")
        self.verticalLayout_2.addWidget(self.ventanaPlot)
        TemperaturaManual.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TemperaturaManual)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        TemperaturaManual.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TemperaturaManual)
        self.statusbar.setObjectName("statusbar")
        TemperaturaManual.setStatusBar(self.statusbar)
        self.accionSalir = QtWidgets.QAction(TemperaturaManual)
        self.accionSalir.setObjectName("accionSalir")
        self.menuArchivo.addAction(self.accionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(TemperaturaManual)
        QtCore.QMetaObject.connectSlotsByName(TemperaturaManual)

    def retranslateUi(self, TemperaturaManual):
        _translate = QtCore.QCoreApplication.translate
        TemperaturaManual.setWindowTitle(_translate("TemperaturaManual", "Registro de Temperatura"))
        self.pB_medirTemp.setText(_translate("TemperaturaManual", "Medir Temperatura"))
        self.label.setText(_translate("TemperaturaManual", "Temp. Referencia"))
        self.label_2.setText(_translate("TemperaturaManual", "Sensor"))
        self.menuArchivo.setTitle(_translate("TemperaturaManual", "Archivo"))
        self.accionSalir.setText(_translate("TemperaturaManual", "Salir"))


from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TemperaturaManual = QtWidgets.QMainWindow()
    ui = Ui_TemperaturaManual()
    ui.setupUi(TemperaturaManual)
    TemperaturaManual.show()
    sys.exit(app.exec_())
