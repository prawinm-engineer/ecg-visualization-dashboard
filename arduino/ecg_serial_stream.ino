/*
  ECG Serial Streaming using AD8232
  Board: Arduino Uno

  This code acquires raw ECG data from the AD8232 sensor
  and streams it via serial communication to a PC
  for visualization and HRV analysis in Python.
*/

const int ECG_PIN = A0;
const int LO_PLUS = 10;
const int LO_MINUS = 11;

void setup() {
  Serial.begin(9600);

  pinMode(LO_PLUS, INPUT);
  pinMode(LO_MINUS, INPUT);

  Serial.println("ECG Serial Stream Started");
}

void loop() {

  // Check lead-off condition
  if (digitalRead(LO_PLUS) == 1 || digitalRead(LO_MINUS) == 1) {
    Serial.println("Leads Off");
  } 
  else {
    int ecgValue = analogRead(ECG_PIN);
    Serial.println(ecgValue);
  }

  delay(5); // ~200 Hz sampling
}
