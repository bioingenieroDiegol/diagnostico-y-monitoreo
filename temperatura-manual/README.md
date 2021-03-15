# Diagnóstico y Monitoreo #
## Facultad de Ingeniería - UNER ##
## 2019 ##

Sistema de adquisición con Arduino para el registro de temperatura en el TPL1.

Antes de ejecutar el programa por primera vez es necesario instalar dos
librerías: 

- pyqtgraph
- pyserial

Las instrucciones son un poco diferentes en Windows y Linux. 


Windows
---------

La suite Anaconda instala muchos programas y librerías pero siempre hay algunas
cosas que quedan fuera. Por eso la explicación es más bien genérica, en caso de
que necesiten instalar otras librerías. 

Hay dos modos: con la utilidad CONDA y con la utilidad PIP. Nuestra
recomendación es aprovechpar la integración de Anaconda y optar por la primera
herramienta, que forma parte del paquete. 

Instalación de una librería "equis":

1. Buscar en google estas palabras clave: anaconda install equis. Por ejemplo:
   anaconda install pyqtgraph
2. Abrir el resultado cuyo dominio sea anaconda.org (usualmente es el primer
   resultado, y el título es Pyqtgraph :: Anaconda Cloud).
3. Copiar la orden que figura en la página. En el caso de pyqtgraph es: "conda
   install -c anaconda pyqtgraph".
4. Desde el inicio de Windows buscar "Anaconda Prompt" o Anaconda solamente y
   buscar el que diga Prompt. Hay dos Prompts, uno es el "Anaconda Powershell
   Prompt", pero mejor si utilizan el "Anaconda Prompt" a secas.
5. Se abre un terminal y ahí ejecutan la orden que copiaron antes. Tener
   paciencia, el sistema parece no responder en algunos casos, la pantalla puede
   quedarse sin mostrar el cursos, con el fondo negro, pero no se dejen vencer
   por el desánimo, tampoco por el final de Game of Thrones ni por el deseo de
   comprar cosas inútiles para llenar algún vacío existencial y esperen un
   mensaje que pide la confirmación de la instalación. Obviamente confirmar
   pulsando "Y" y "ENTER".
6. No olvidar de repetir el procedimiento para cada librería (pyqtgraph,
   pyserial).
   

Ejecución del Programa
---------------------------

Hay dos programas. 

1. Temperatura Continuo: registra continuamente con una frecuencia de muestreo
   de 100 Hz. Es para realizar el ensayo a partir del cual calcular la constante
   de tiempo (TAU) del instrumento.
2. Temperatura Manual: registra un dato cada vez que se pulsa un botón en la
   pantalla del programa. 
   
Dentro de cada carpeta de uno y otro programa está el código Arduino que hay que
cargar en la Arduino UNO o Arduino Mega que use cada grupo. Pedir instrucciones
en clase.

Antes de ejecutar el programa es necesario editar la linea que indica el puerto
al que está conectado la placa Arduino. Buscar:

   self.ser = serial.Serial('/dev/ttyACM0', 115200)

Y reemplazarla por (colocar el número de COM adecuado):

   self.ser = serial.Serial('COM1', 115200)

Finalmente, los programas se ejecutan desde el Anaconda Prompt, navegando hasta
el directorio local donde estén alojados. Para que corran escribir:

   python registro-temperatura.py

ó 

   python temperatura-manual.python
   
   
PELIGRO - DANGER - GEFAHR - ОПАСНО - PERIGO - VAARA
--------------------------------------------------------------

Estos programas están en desarrollo, en versión beta, y pueden fallar tanto como
las pruebas de Tu-Sam.

La grabación de datos se realiza en formato .txt pero con cada ejecución del
programa se sobreescribe el archivo, así que para salvaguardar los datos es
necesario renombrar y/o mover los archivos de texto.



