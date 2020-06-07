#include <SoftwareSerial.h>
#include <Sprite.h>
#include <Matrix.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C mylcd(0x27,16,2);
SoftwareSerial mySerial(10, 11); // RX, TX

//libraries http://duinoedu.com/dl/lib/dupont/sprite/
//libraries http://duinoedu.com/dl/lib/dupont/matrix/
Matrix mesLeds367 = Matrix(3,6,7,1);
int X[] = {
  0,7,6,5,4,3,2,1};
int Y[] = {
  7,6,5,4,3,2,1,0};

int botton=8; 
int mine, yours;

void setup()
{
  Serial.begin(9600);
  mySerial.begin(9600);
  mesLeds367.clear();
  mylcd.init();
  mylcd.backlight();
  mylcd.clear();
  pinMode(botton, INPUT);
  mine=1;
  yours=1;
}

void stone(){
  mesLeds367.clear();
  for(int i=2; i<=5; i++){
    for(int j=2; j<=5; j++){
        mesLeds367.write(X[i],Y[j],HIGH);
    }
  }
}

void scissor(){
  mesLeds367.clear();
  for(int i=2; i<=7; i++){
    for(int j=0; j<=7;j++){
      if(i==j||i+j==7){
        mesLeds367.write(X[i],Y[j],HIGH);
      }
    }
  }
  for(int i=0; i<=2; i++){
    for(int j=0; j<=2; j++){
      if(i==0||i==2||j==0||j==2){
        mesLeds367.write(X[i],Y[j],HIGH);
      }
    }   
  }
  for(int i=0; i<=2; i++){
    for(int j=5; j<=7; j++){
      if(i==0||i==2||j==5||j==7){
        mesLeds367.write(X[i],Y[j],HIGH);
      }
    }   
  }
}

void pack(){
  mesLeds367.clear();
  for(int i=0; i<=7; i++){
    for(int j=0; j<=7; j++){
      if(i==0||j==0||i==7||j==7){
        mesLeds367.write(X[i],Y[j],HIGH);
      }
    }
  }
}

void showmine(int mine){
  switch(mine){
    case 1: 
      stone();
      break;
    case 2:
      scissor();
      break;
    case 3:
      pack();
      break;
  }
}

void compete(int mine, int yours){
  mylcd.clear();
  mylcd.setCursor(0, 0);
  if(yours - mine == 1||  mine-yours ==2){
    mylcd.print("I win!");
  }
  else if(mine - yours == 1||  yours-mine ==2){
    mylcd.print("You win!");
  }
  else if(mine==yours){
    mylcd.print("Same!");
  }
  else {
    mylcd.print("Pass");
  }
}

void loop()
{
  byte rev;
  if (mySerial.available())
  {
    rev = mySerial.read();
    Serial.println(rev);
    yours = rev-48;
  }

  //Serial.println(digitalRead(8));
  if (digitalRead(8) == HIGH) {
    while (digitalRead(8) == HIGH) {
      delay(10);
    }
    mine = random(1, 4);
    showmine(mine);
    compete( mine, yours);
  }
}


