# Registro de la presión arterial mediante el método oscilométrico
#
#
# Agosto 2023.
# Instrumental Biomédico para Diagnóstico y Monitoreo
# Facultad de Ingeniería.
# UNER
#
#
# Se utiliza un sensor MPX50 o MPX100 conectado al Arduino a través
# de un conversor ADS1115. Probado con la librería ADS111X de
# Adafruit con el ejemplo: Differential.
#
#
# Los datos se digitalizan con un ADS1115 que envía los datos de 16
# bits mediante comunicación I2C al Arduino, y desde allí se utiliza
# comunicación serie para enviar los datos a la PC.
#
#
# La adquisición se realiza a 100 Hz (T=10ms).
#
#
# La interfaz gráfica está construida con PyQt5. Para convertir el
# archivo .ui generado en código de Python se utiliza:
# pyuic5 -x pantallaRegistro.ui -o pantallaRegistro.py
#
#

from PyQt5 import QtCore

from PyQt5.QtWidgets import QMainWindow, QApplication

from pantallaRegistroPresion import Ui_Presion
import numpy as np
import serial

from datetime import datetime



class Registro():
    def __init__(self, tiempo=5, frecuencia=100):
        self.tiempo     = tiempo       # en segundos
        self.frecuencia = frecuencia   # en Hertz
        self.periodo    = 0.100        # en segundos
        self.tam = int(self.tiempo / self.periodo)
        # print("tamaño vector: ", self.tam)
        self.index = 0
        self.vector = np.zeros([self.tam])

    def modificarTiempo(self, tiempo):
        self.tiempo = tiempo
        self.tam = int(self.tiempo / self.periodo)
        # print("nuevo tamaño vector: ", self.tam)        
        self.index = 0
        self.vector = np.zeros([self.tam])

    def agregarDato(self, dato):
        self.vector[self.index] = dato
        self.index = self.index+1
        if (self.index >= self.tam):
            self.index = 0
        # print("index: ", self.index)

    def grabarVector(self):
        now = datetime.now()
        fechayhora = now.strftime("%Y%m%d-%H%M%S.txt")
        np.savetxt(fechayhora, self.vector)
        print("Archivo grabado: ", fechayhora)


class Window(QMainWindow):
    def __init__(self, reg):
        QMainWindow.__init__(self)
        self.ui = Ui_Presion()
        self.ui.setupUi(self)
        self.datosAdquiridos = 0

        self.p = self.ui.ventanaPlot
        self.curva = self.p.plot()
        self.curva.setPen((255,0,0))

        # inicialización del registro
        tiempo = 5             # en segundos
        frecuencia = 100       # en Hertz
        self.reg = Registro(tiempo, frecuencia)

        # fija la cantidad de datos inicial que serán registrados y graficados
        self.ui.sB_Tiempo.setValue(reg.tiempo)
 
        # fija los extremos del gráfico temporal
        self.x1 = 0
        self.x2 = reg.tam
        self.y1 = 0
        self.y2 = 65536   # 65536 son 16 bits, 1024 son 10 bits 
        self.setearLimitesPlot(self.x1,self.x2,self.y1,self.y2)

        # conexiones para dar servicio a los botones
        self.ui.pB_iniciar.clicked.connect(self.iniciarTimer)
        self.ui.pB_finalizar.clicked.connect(self.detenerTimer)
        self.ui.sB_Tiempo.valueChanged.connect(self.cambiarTiempo)
        self.ui.pB_grabar.clicked.connect(self.grabar)
        self.ui.accionSalir.triggered.connect(self.salir)

        # inicialización de la comunicación serie
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        # self.ser = serial.Serial('COM3', 115200)
        self.ser.flushInput()

        # inicialización del timer (para la lectura de datos)
        self.timer = QtCore.QTimer()

    def cambiarTiempo(self):

        nuevoTiempo = window.ui.sB_Tiempo.value()

        # actualizamos los parámetros del registro
        reg.modificarTiempo(nuevoTiempo)

        # actualizamos los límites del gráfico
        
        self.x2 = reg.tam
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

        
        periodo = int(reg.periodo * 1000)  # cambio a milisegundos
        # print("periodo de adquisición: ", periodo)
        self.timer.start(periodo)
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
            # print("nuevo número: ", nuevo_numero)
        except:
            print("Keyboard Interrupt")

        # print("nuevo númerito: {}".format(nuevo_numero))
        # vector.append(nuevo_numero)
        reg.agregarDato(nuevo_numero)

        # print("-------------> vector", reg.vector)
        # window.graficar(vector)
        # self.graficar(reg.vector)
        self.actualizarPlot()
        # if self.datosAdquiridos >= window.ui.sB_Tiempo.value():        
        if self.datosAdquiridos >= reg.tam:
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
