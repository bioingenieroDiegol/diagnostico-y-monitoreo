# Registro de la Temperatura mediante Arduino.
# Abril 2019. Agosto 2019.
# Instrumental Biomédico para Diagnóstico y Monitoreo
# Facultad de Ingeniería.
# UNER

# Los datos se registran desde la entrada Analog In 0 del Arduino (ver software
# Arduino). La placa los envía por puerto serie y se grafican. La adquisición
# se realiza a 100 Hz (T=10ms).

from PyQt5 import QtCore, QtGui

from PyQt5.QtWidgets import QMainWindow, QApplication

from pantallaRegistroTemperatura import Ui_Temperatura
import numpy as np
import serial

class Registro():
    def __init__(self, tam=500):
        self.tam = tam
        self.index = 0
        self.vector = np.zeros([tam])

    def modificarTam(self, nuevoTam):
        self.tam = nuevoTam
        self.index = 0
        self.vector = np.zeros([nuevoTam])

    def agregarDato(self, dato):
        self.vector[self.index] = dato
        self.index = self.index+1
        if (self.index >= self.tam):
            self.index = 0

    def grabarVector(self):
        np.savetxt("registro-de-temperatura.txt", self.vector)



class Window(QMainWindow):
    def __init__(self, reg):
        QMainWindow.__init__(self)
        self.ui = Ui_Temperatura()
        self.ui.setupUi(self)
        self.datosAdquiridos = 0

        self.p = self.ui.ventanaPlot
        self.curva = self.p.plot()
        self.curva.setPen((255,0,0))

        self.reg = Registro()

        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        # self.ser = serial.Serial('COM3', 115200)
        self.ser.flushInput()

        # fija la cantidad de datos inicial que serán registrados y graficados (50 es razonable?)
        self.ui.sB_cantDatos.setValue(reg.tam)

        # fija los extremos del gráfico temporal
        self.x1 = 0
        self.x2 = self.ui.sB_cantDatos.value()
        self.y1 = 0
        self.y2 = 1024
        self.setearLimitesPlot(self.x1,self.x2,self.y1,self.y2)

        # fija período (en ms)
        self.periodo = 10

        # conexiones para dar servicio a los botones
        self.ui.pB_iniciar.clicked.connect(self.iniciarTimer)
        self.ui.pB_finalizar.clicked.connect(self.detenerTimer)
        self.ui.sB_cantDatos.valueChanged.connect(self.cambiarCantDatos)
        self.ui.pB_grabar.clicked.connect(self.grabar)
        self.ui.accionSalir.triggered.connect(self.salir)
        # self.ui.pB_grabar.clicked.connect(grabarDatos)

        self.timer = QtCore.QTimer()

    def cambiarCantDatos(self):
        nuevoMax = window.ui.sB_cantDatos.value()
        self.x2 = nuevoMax
        reg.modificarTam(nuevoMax)
        # print("-------------------------> max X: ", self.x2)
        self.setearLimitesPlot(self.x1, self.x2, self.y1, self.y2)

    def setearLimitesPlot(self, x1, x2, y1, y2):
        self.p.setRange(xRange=[x1, x2+10], yRange=[y1, y2])

    def graficar(self, data):
        self.p.plot(data)

    def borrarPlot(self):
        self.p.clear()

    def borrarCurva(self):
        self.curva.clear()

    def iniciarTimer(self):
        self.datosAdquiridos = 0
        # print("iniciar timer!!!")
        self.ser.flushInput()
        self.borrarCurva()
        # periodo = window.ui.sB_periodo.value()
        # print("periodo de adquisición: ", periodo)
        self.timer.start(self.periodo)
        self.timer.timeout.connect(self.update)

    def detenerTimer(self):
        # print("detener timer!!!")
        # print(reg.vector)
        # print("size: ", reg.vector.size)
        # self.graficar(reg.vector)
        self.timer.stop()
        self.datosAdquiridos = 0

    def actualizarPlot(self):
        self.curva.setData(reg.vector)

    def update(self):
        self.datosAdquiridos += 1
        nuevo_numero = 0
        try:
            ser_bytes = self.ser.readline()
            nuevo_numero = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        except:
            print("Keyboard Interrupt")

        # print("nuevo númerito: {}".format(nuevo_numero))
        # vector.append(nuevo_numero)
        reg.agregarDato(nuevo_numero)

        # print("-------------> vector", reg.vector)
        # window.graficar(vector)
        # self.graficar(reg.vector)
        self.actualizarPlot()
        if self.datosAdquiridos >= window.ui.sB_cantDatos.value():
            self.detenerTimer()


    def grabar(self):
        reg.grabarVector()


    def salir(self):
        sys.exit()




if __name__ == '__main__':

    import sys

    ## initializing Qt (only once per application)
    app = QApplication(sys.argv)
    reg = Registro()
    # print(reg.vector)

    # print("vector vacío: ", vector)

    # inicializa un objeto (window) que contendra todos los widgets, y lo muestra
    window = Window(reg)
    window.show()
    # window.ui.lbl_etiqueta.setText("hola")
    # window.escribirEtiqueta("Chau")

    # inicializacion()

    ## Start the Qt event loop: app.exec()
    sys.exit(app.exec_())
