//getting 
#include <Servo.h>             //Servo library

int incomingByte = 0; // for incoming serial data
Servo servo_test;    		//initialize a servo object for the connected servo  
int angle = 0; 

void setup() 
{ 
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  servo_test.attach(9); 		 // attach the signal pin of servo to pin9 of arduino
} 
  
void loop() 
{ 
    
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    distance = Serial.read();                //gettin distance from left from serial
    angle = arccos(distance);                //calculating angle on camera rotation from distance from left
    servo_test.write(angle);              	 //command to rotate the servo to the specified angle
    delay(15);                       
  }
  delay(1000);
}