/*
 
  Este programa convierte en digital el voltaje que viene de un sensor y envía 
  ese valor por puerto serie cada 10 ms (100 Hz). 
   
*/


int sensorPin = A0;    // selecciona el pin de entrada (del A/D)
int sensorValue = 0;  // variable para almacenar el voltaje del sensor


void setup() {
  // inicializa la comunicación serie
  Serial.begin(115200);

  // initializa el pin digital LED_BUILTIN como salida
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    sensorValue = analogRead(sensorPin);
    Serial.println(sensorValue);
    delay(10);
    digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  
}
