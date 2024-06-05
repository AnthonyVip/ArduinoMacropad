#include <Keypad.h>

const byte ROWS = 5;
const byte COLS = 4;

const char hexaKeys[ROWS][COLS] = {
  {'+', '%', '$', '@'},
  {'P', '9', '8', '7'},
  {'C', '6', '5', '4'},
  {'M', '3', '2', '1'},
  {'E', 'F', 'S', '0'}
};

// Digital pins for Rows and Cols
byte rowPins[ROWS] = {6, 5, 4, 3, 2};
byte colPins[COLS] = {10, 9, 8, 7};

// Creates keypad object
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS);

unsigned long debounceDelay = 50;
unsigned long lastDebounceTime = 0;

char lastKeyPressed = NO_KEY;
const unsigned long keyHoldThreshold = 1000;



void setup() {
  Serial.begin(9600);
}

void loop() {
  char customKey = customKeypad.getKey();
  unsigned long currentTime = millis();
  if (customKey != NO_KEY){
     if (customKey != lastKeyPressed || (currentTime - lastDebounceTime > debounceDelay)){
        lastDebounceTime = currentTime;
        lastKeyPressed = customKey;
        Serial.println(customKey);
    }
  }
  else{
    lastKeyPressed = NO_KEY;
    }
  
}
