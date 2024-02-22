#include <Adafruit_GFX.h>
#include <RGBmatrixPanel.h>

#define CLK  11
#define OE   9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, false);

int player1Score = 0;
int player2Score = 0;

void setup() {
  matrix.begin();
  matrix.setTextSize(1);
  matrix.setTextWrap(false);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "P1_SCORE_UP") {
      player1Score++;
    } else if (command == "P2_SCORE_UP") {
      player2Score++;
    }
    updateDisplay();
  }
}

void updateDisplay() {
  matrix.fillScreen(0);
  matrix.setCursor(1, 1);
  matrix.print(player1Score);
  matrix.setCursor(17, 1);
  matrix.print(player2Score);
  matrix.writeDisplay();
}
