#include <Servo.h>
#include <stdlib.h>
Servo myservo;
int motor_pin1 = 11;
int motor_pin2 = 6;
int dir1 = 5;
int dir2 = 3;
int servo_pin = 9;
int motor = 20; //速度值
int angle = 90;  //角度值
int num = 0;//临时字符变量，又或者说是缓存用的吧
int sp1 = 0;
int sp2 = 0;
int lev;
int data;
String comdata;
char tmp;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  myservo.attach(servo_pin); 
  myservo.write(90);
  pinMode(motor_pin1, OUTPUT);
  pinMode(motor_pin2, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(dir2, OUTPUT);  
}

void loop() {
  while (Serial.available() > 0)  
{   
  tmp = char(Serial.read());
    if (tmp >= '0' && tmp <= '9') {
      comdata += tmp;
    }
    
    delay(2);
    }
  
  if (comdata.length() > 0) {
//    data = atoi(comdata.c_str());
    
    lev = comdata[0] - '0';
    angle = (comdata[1] - '0') * 10 + (comdata[2] - '0');
    Serial.println(lev);
    Serial.println(angle);
    comdata = "";
    }
    


  if (lev == 0){
    sp1 = 255;
    sp2 = 0;
    motor = 15;
  }
  else if (lev == 3){
    sp1 = 0;
    sp2 = 0;
    motor = 0;
    angle = 90;
  }
  else if (lev == 1){
    sp1 = 0;
    sp2 = 255;
    motor = 15;
  }
  else if (lev == 2){
    sp1 = 0;
    sp2 = 255;
    motor = 22;
  }

  myservo.write(angle);  //控制舵机转动相应的角度。
  analogWrite(dir1, sp1);
  analogWrite(dir2, sp2);
  analogWrite(motor_pin1, motor);
  analogWrite(motor_pin2, motor);
  delay(100);//延时100毫秒
}
