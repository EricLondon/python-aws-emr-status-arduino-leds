// define pins for leds
int ledPinGreen = 12;
int ledPinRed = 13;

int incomingByte = 0;

void setup() {
  // put your setup code here, to run once:

  // set pin modes to output for leds
  pinMode(ledPinGreen, OUTPUT);
  pinMode(ledPinRed, OUTPUT);

  // init serial connection
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() > 0) {
    // read the incoming byte
    incomingByte = Serial.read();

    if (incomingByte == '1') {
      // 1|true: set green led to on, red to off
      digitalWrite(ledPinGreen, HIGH);
      digitalWrite(ledPinRed, LOW);
    } else {
      // 0|false: set green led to off, red to on
      digitalWrite(ledPinGreen, LOW);
      digitalWrite(ledPinRed, HIGH);
    }

  }

  delay(500);
}
