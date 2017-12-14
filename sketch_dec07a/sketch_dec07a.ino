#include <Servo.h>
//while(Serial.available()==0){};
Servo servo;
Servo servo2;
int pos = 90;
int pos2 = 90;
int led = 8;
void pos2rw();
void setup() {
 Serial.begin(9600);
 servo.attach(12);
 servo2.attach(9);
 servo2.write(pos);
 servo.write(pos2);
 pinMode(led, OUTPUT);
 digitalWrite(led, HIGH);

 
}

void loop() {
  while(Serial.available()==0){};
  pos = Serial.read();
  if (4<pos<174){
    servo2.write(pos);
    pos2rw();  
  }
  else{
   loop();
  }
  
  
}

void pos2rw(){
  while(Serial.available()==0){};
  pos2 = Serial.read();
  if (4<pos2<174){
    servo.write(pos2);
    loop();
  }
  else{
    pos2rw();
  }
  
}






