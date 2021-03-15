
// Envia datos por el puerto serie, pero solamente
// si desde la PC recibe algun dato/comando a traves
// de ese mismo puerto. Permite asi obtener conversione
// "a demanda"


int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor

void limpiarBufferSerie(){
  
  // luego de detectar que hay algo en el puerto Serie
  // no estoy seguro de que eso que llegó no vaya a disparar
  // eternamente el Serial.available() así que esta funcion
  // lee, y por ende, limpia el buffer
   
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}   


void setup() {
  Serial.begin(115200); // opens serial port, sets data rate to 115200 bps
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // envía datos solamente cuando recibe algo
  // testea cada 10ms
  delay(10); 
  if (Serial.available() > 0) {
    
    // lee el buffer y lo envia por puerto serie, luego limpia el buffer
    sensorValue = analogRead(sensorPin);
    Serial.println(sensorValue);
    limpiarBufferSerie();
    
    // Serial.print("I received: ");
    // Serial.println(incomingByte, DEC);
    // Serial.println(10);
  }
}
