#include <Servo.h>

#define MIN_Y 90
#define MAX_Y 180

#define MIN_X 0
#define MAX_X 180

Servo tilt;
Servo pan;

int curX = MAX_X/2;
int curY = MIN_Y;

void setup() {
    Serial.begin( 115200 );
    pan.attach( 11 );
    tilt.attach( 12 );
    
    tilt.write( curX );
    pan.write( curY );
}

void loop() {
    while( Serial.available() == 0 );
    int c = Serial.read();
    int x,y;
    Serial.flush();

    x = ( c % 10 ) - 2;
    y = ( c / 10 ) - 2;
    curX += x;
    curY += y;
    if( curX > MAX_X )
        curX = MAX_X;
    if( curY > MAX_Y )
        curY = MAX_Y;
    
    if( curX < MIN_X )
        curX = MIN_X;
    if( curY < MIN_Y )
        curY = MIN_Y;
    tilt.write( curX );
    pan.write( curY );
}