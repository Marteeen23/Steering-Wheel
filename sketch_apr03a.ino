char a='X';
void setup() {
  Serial.begin(115200);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {
  if(Serial.available())
  {
    a=Serial.read();
  }
  if(a=='F')
  {
    digitalWrite(5, HIGH);
    digitalWrite(6, LOW);
    digitalWrite(10, HIGH);
    digitalWrite(11, LOW);
  }
  else if(a=='R')
  {
    digitalWrite(5, HIGH);
    digitalWrite(6, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
  }
  else if(a=='L')
  {
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(10, HIGH);
    digitalWrite(11, LOW);
  }
  else if(a=='B')
  {
    digitalWrite(5, LOW);
    digitalWrite(6, HIGH);
    digitalWrite(10, LOW);
    digitalWrite(11, HIGH);
  }
  else
  {
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(10, LOW);
    digitalWrite(11, LOW);
  }
}
