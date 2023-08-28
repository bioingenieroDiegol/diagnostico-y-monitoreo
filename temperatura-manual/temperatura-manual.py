# Registro de la Temperatura mediante Arduino.
# Agosto 2019.
# Instrumental Biomédico para Diagnóstico y Monitoreo
# Facultad de Ingeniería.
# UNER

# Los datos se registran desde la entrada Analog In 0 del Arduino (completar
# descripción). Lo que está desprolijo y hay que revisar es el tamaño de los
# vectores que guardan los datos. Está por defecto en un número fijo (500) pero
# estaría bueno ver cómo se hace un vector dinámico, que cambie su tamaño de
# acuerdo al contenido que se le va agregando.

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from pantallaTemperaturaManual import Ui_TemperaturaManual

import numpy as np
import pint
from pint import UnitRegistry

import serial

class Registro():
    def __init__(self, tam=500):
        self.tam = tam
        self.index = 0
        self.temp_ref = np.zeros([tam])
        self.temp_sensor = np.zeros([tam])

    def modificarTam(self, nuevoTam):
        self.tam = nuevoTam
        self.index = 0
        self.temp_ref = np.zeros([tam])
        self.temp_sensor = np.zeros([nuevoTam])

    def agregarDato(self, temp_ref, temp_sensor):
        self.temp_ref[self.index] = temp_ref
        self.temp_sensor[self.index] = temp_sensor
        self.index = self.index+1
        if (self.index >= self.tam):
            self.index = 0

    def grabarVector(self):
        np.savetxt("temp-referencia.txt", self.temp_ref[:self.index])
        np.savetxt("temp-sensor.txt", self.temp_sensor[:self.index])



class Window(QMainWindow):
    def __init__(self, reg):
        QMainWindow.__init__(self)
        self.ui = Ui_TemperaturaManual()
        self.ui.setupUi(self)
        self.datosAdquiridos = 0

        self.p = self.ui.ventanaPlot
        self.curva = self.p.plot()
        self.curva.setPen((255,0,0))

        self.reg = Registro()

        # self.ser = serial.Serial('COM3', 115200)
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.ser.flushInput()

        # fija la cantidad de datos inicial que serán registrados y graficados (50 es razonable?)
        # self.ui.sB_cantDatos.setValue(reg.tam)

        # fija los extremos del gráfico temporal
        self.x1 = 0   # el mínimo después lo tengo que cambiar a 50 grados
        self.x2 = 100 # supuestamente la temperatura máxima es 100 grados
        self.y1 = 0
        self.y2 = 1024
        self.setearLimitesPlot(self.x1,self.x2,self.y1,self.y2)

        # fija período (en ms)
        self.periodo = 10

        # conexiones para dar servicio a los botones
        self.ui.pB_medirTemp.clicked.connect(self.registrarDato)
        # self.ui.pB_finalizar.clicked.connect(self.detenerTimer)
        # self.ui.sB_cantDatos.valueChanged.connect(self.cambiarCantDatos)
        # self.ui.pB_grabar.clicked.connect(self.grabar)
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

    def registrarDato(self):
        # self.datosAdquiridos = 0
        self.ser.flushInput()
        self.borrarCurva()
        self.ser.write(b'1')     # manda un dato cualquiera para avisarle al arduino que lea el analog in.
        self.update()

        # periodo = window.ui.sB_periodo.value()
        # print("periodo de adquisición: ", periodo)
        # self.timer.start(self.periodo)
        # self.timer.timeout.connect(self.update)

    def detenerTimer(self):
        print("detener timer!!!")
        print(reg.tem)
        print("size: ", reg.temp_sensor.size)
        # self.graficar(reg.vector)
        self.timer.stop()
        self.datosAdquiridos = 0

    def actualizarPlot(self):
        self.curva.setData(reg.temp_ref[:reg.index], reg.temp_sensor[:reg.index])

    def update(self):
        # self.datosAdquiridos += 1
        nuevo_numero = 0
        try:
            ser_bytes = self.ser.readline()
            t_sensor = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            # print("nuevo númerito: {}".format(nuevo_numero))
            # vector.append(nuevo_numero)
            t_ref = window.ui.sB_tref.value()
            print(" ")
            print("---------------------------------")
            print("tref, tsensor: ", t_ref, t_sensor)
            reg.agregarDato(t_ref,t_sensor)
            print(reg.temp_ref[:reg.index])
            print(reg.temp_sensor[:reg.index])
            window.ui.lcd_sensor.display(t_sensor)
            reg.grabarVector()
            # print("nuevo numero: ", t_sensor)
            self.actualizarPlot()
        except:
            print("Keyboard Interrupt")

        # print("-------------> vector", reg.vector)
        # window.graficar(vector)
        # self.graficar(reg.vector)
        # if self.datosAdquiridos >= window.ui.sB_cantDatos.value():
            # self.detenerTimer()


    # def grabar(self):
    #     reg.grabarVector()


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
