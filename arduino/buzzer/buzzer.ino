#define BUZZER_PIN 11

void setup() {
  Serial.begin(9600);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char nota = Serial.read();
    int freq = 0;

    switch (nota) {
      case 'A': freq = 262; break; // dó
      case 'B': freq = 294; break; // ré
      case 'C': freq = 330; break; // mi
      case 'D': freq = 349; break; // fá
      case 'E': freq = 392; break; // sol
    }

    if (freq > 0) {
      tone(BUZZER_PIN, freq, 300);
      delay(300);
      noTone(BUZZER_PIN);
    }
  }
}
