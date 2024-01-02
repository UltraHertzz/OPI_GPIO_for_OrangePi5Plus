#include <wiringPi.h>
#include <stdio.h>

class OrangePi {
    public:
        const int LED = 5;

        void loop(){
            pinMode(this->LED, OUTPUT);
            while (TRUE){
                digitalWrite(this->LED, HIGH);
                delay(1000);
                digitalWrite(this->LED, LOW);
                delay(1000);
            }
        }
    
};

int main(){

    wiringPiSetup();
    OrangePi LED;
    LED.loop();

}

