import OPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup([3,5], GPIO.OUT)
pwm0 = GPIO.PWM(chip=0,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)
pwm1 = GPIO.PWM(chip=1,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)
#pwm2 = GPIO.PWM(chip=2,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True) No such device
#pwm3 = GPIO.PWM(chip=3,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)
pwm4 = GPIO.PWM(chip=4,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)
pwm5 = GPIO.PWM(chip=5,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)
pwm6 = GPIO.PWM(chip=6,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)
pwm7 = GPIO.PWM(chip=7,pin=0,frequency=50,duty_cycle_percent=100,invert_polarity=True)

pwm0.start_pwm()
pwm1.start_pwm()
#pwm2.start_pwm()
#pwm3.start_pwm()
pwm4.start_pwm()
pwm5.start_pwm()
pwm6.start_pwm()
pwm7.start_pwm()

try:
    while True:
        for i in range(1,100,5):
            pwm0.duty_cycle(i)
            pwm1.duty_cycle(i)
            #pwm2.duty_cycle(i)
            #pwm3.duty_cycle(i)
            pwm4.duty_cycle(i)
            pwm5.duty_cycle(i)
            pwm6.duty_cycle(i)
            pwm7.duty_cycle(i)
            time.sleep(0.02)
        for i in range(100,1,-5):
            pwm0.duty_cycle(i)
            pwm1.duty_cycle(i)
            #pwm2.duty_cycle(i)
            #pwm3.duty_cycle(i)
            pwm4.duty_cycle(i)
            pwm5.duty_cycle(i)
            pwm6.duty_cycle(i)
            pwm7.duty_cycle(i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pwm0.stop_pwm()
    pwm1.stop_pwm()
    #pwm2.stop_pwm()
    #pwm3.stop_pwm()
    pwm4.stop_pwm()
    pwm5.stop_pwm()
    pwm6.stop_pwm()
    pwm7.stop_pwm()

    pwm0.pwm_close()
    pwm1.pwm_close()
    #pwm2.pwm_close()
    #pwm3.pwm_close()
    pwm4.pwm_close()
    pwm5.pwm_close()
    pwm6.pwm_close()
    pwm7.pwm_close()
    GPIO.setup(33, GPIO.OUT)
    GPIO.cleanup()

