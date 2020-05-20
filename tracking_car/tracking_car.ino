/*
  Software serial multple serial test

 Receives from the hardware serial, sends to software serial.
 Receives from software serial, sends to hardware serial.

 The circuit:
 * RX is digital pin 10 (connect to TX of other device)
 * TX is digital pin 11 (connect to RX of other device)

 Note:
 Not all pins on the Mega and Mega 2560 support change interrupts,
 so only the following can be used for RX:
 10, 11, 12, 13, 50, 51, 52, 53, 62, 63, 64, 65, 66, 67, 68, 69

 Not all pins on the Leonardo support change interrupts,
 so only the following can be used for RX:
 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI).

 created back in the mists of time
 modified 25 May 2012
 by Tom Igoe
 based on Mikal Hart's example

 This example code is in the public domain.

 */
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
int m1Dir = 4;//左方向
int m1pwm = 5;//左速度
int m2pwm = 6;//右速度
int m2Dir = 7;//右方向 
int speed=40;//速度

void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  mySerial.begin(9600);

  pinMode(m1Dir , OUTPUT);
  pinMode(m1pwm , OUTPUT);
  pinMode(m2Dir , OUTPUT);
  pinMode(m2pwm , OUTPUT); 
}

void forward(){
  digitalWrite(m1Dir, HIGH);
  analogWrite(m1pwm,speed);
  digitalWrite(m2Dir, HIGH);
  analogWrite(m2pwm,speed);
}

void slow() { 
  speed = speed - 10;
}

void quick() {
  speed = speed+10;
}

void left(){
  digitalWrite(m1Dir, HIGH);
  analogWrite(m1pwm,0);
  digitalWrite(m2Dir, HIGH);
  analogWrite(m2pwm,40);
  delay(200);
}

void right(){
  digitalWrite(m1Dir, HIGH);
  analogWrite(m1pwm,40);
  digitalWrite(m2Dir, HIGH);
  analogWrite(m2pwm,0);
  delay(200);
}

void loop() // run over and over
{
  String str;
  if (mySerial.available()){
    str=mySerial.readStringUntil(0);
    Serial.println(str);
    mySerial.flush();
    if(str=="quick"){
      quick();
    }
    else if(str=="slow"){
      slow();
    } 
    else if(str=="left"){
      left();
    } 
    else if(str=="right"){
      right();
    }
    else if(str=="lost"){
      speed=0;
    }
  }
  forward();
}


