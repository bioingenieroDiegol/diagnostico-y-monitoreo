# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantallaRegistroTemperatura.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Temperatura(object):
    def setupUi(self, Temperatura):
        Temperatura.setObjectName("Temperatura")
        Temperatura.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Temperatura)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pB_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.pB_iniciar.setObjectName("pB_iniciar")
        self.verticalLayout.addWidget(self.pB_iniciar)
        self.pB_finalizar = QtWidgets.QPushButton(self.centralwidget)
        self.pB_finalizar.setObjectName("pB_finalizar")
        self.verticalLayout.addWidget(self.pB_finalizar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pB_grabar = QtWidgets.QPushButton(self.centralwidget)
        self.pB_grabar.setObjectName("pB_grabar")
        self.horizontalLayout_2.addWidget(self.pB_grabar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lbl_cantDatos = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cantDatos.setObjectName("lbl_cantDatos")
        self.horizontalLayout_2.addWidget(self.lbl_cantDatos)
        self.sB_cantDatos = QtWidgets.QSpinBox(self.centralwidget)
        self.sB_cantDatos.setMaximum(1000000)
        self.sB_cantDatos.setProperty("value", 100)
        self.sB_cantDatos.setObjectName("sB_cantDatos")
        self.horizontalLayout_2.addWidget(self.sB_cantDatos)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.ventanaPlot = PlotWidget(self.centralwidget)
        self.ventanaPlot.setObjectName("ventanaPlot")
        self.verticalLayout_2.addWidget(self.ventanaPlot)
        Temperatura.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Temperatura)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        Temperatura.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Temperatura)
        self.statusbar.setObjectName("statusbar")
        Temperatura.setStatusBar(self.statusbar)
        self.accionSalir = QtWidgets.QAction(Temperatura)
        self.accionSalir.setObjectName("accionSalir")
        self.menuArchivo.addAction(self.accionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(Temperatura)
        QtCore.QMetaObject.connectSlotsByName(Temperatura)

    def retranslateUi(self, Temperatura):
        _translate = QtCore.QCoreApplication.translate
        Temperatura.setWindowTitle(_translate("Temperatura", "Registro de Temperatura"))
        self.pB_iniciar.setText(_translate("Temperatura", "Iniciar"))
        self.pB_finalizar.setText(_translate("Temperatura", "Finalizar"))
        self.pB_grabar.setText(_translate("Temperatura", "Grabar"))
        self.lbl_cantDatos.setText(_translate("Temperatura", "Cant Datos"))
        self.menuArchivo.setTitle(_translate("Temperatura", "Archivo"))
        self.accionSalir.setText(_translate("Temperatura", "Salir"))


from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Temperatura = QtWidgets.QMainWindow()
    ui = Ui_Temperatura()
    ui.setupUi(Temperatura)
    Temperatura.show()
    sys.exit(app.exec_())
