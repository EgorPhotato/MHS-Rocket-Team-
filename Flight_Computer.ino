#include <Wire.h>    //Include wire library 
#include <MPU6050_light.h>  //Include library for MPU communication

MPU6050 mpu(Wire);   //Create object mpu
  
unsigned long timer = 0;    

void setup() {

  Serial.begin(9600);    //Start serial communication
  Wire.begin();     
  mpu.begin();      
  delay(1000);
  mpu.calcGyroOffsets();     //Calibrate gyroscope
  

}
void loop() {
  mpu.update();    //Get values from MPU
  if ((millis() - timer) > 100) { // print data every 100ms
    timer = millis();
    Serial.println(mpu.getAngleZ());     //Print Z angle value on LCD 
    delay(10);
  }
}
