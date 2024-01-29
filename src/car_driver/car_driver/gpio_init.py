from car_driver.OPi import GPIO as GPIO


class CarController_Base():

    def __init__(self) -> None:
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        # correct Right Rear Wheel
            # 18 -> pwm pin (yellow)
            # 19 -> gpio pin  (orange)
            # 22 -> enable (red)
        GPIO.setup([18, 19, 22], GPIO.OUT) 

        # correct Right Front Wheel
            # 31 -> gpio pin (orange)
            # 33 -> pwm pin (yellow)
            # 35 -> enable (green)
        GPIO.setup([31, 33, 35], GPIO.OUT) 

        # correct Left Rear Wheel
            # 13 -> gpio pin (black)
            # 15 -> enbale (light brown)
            # 16 -> pwm pin (red)
        GPIO.setup([13, 15, 16], GPIO.OUT)

        # correct Left Front Wheel
            # 10 -> enable (brown)
            # 11 -> gpio pin
            # 12 -> pwm pin
        GPIO.setup([10, 11, 12], GPIO.OUT)
        # set PWM pin
        self.pwm_rr = GPIO.PWM(7,0,50,100) # pwmchip7 -> GPIO pin 33(febf0020) right rear
        self.pwm_rf = GPIO.PWM(6,0,50,100) # pwmchip6 -> GPIO pin 18(fd8b0010) right front
        self.pwm_lr = GPIO.PWM(5,0,50,100) # pwmchip5 -> GPIO pin 16(febf0000) left rear
        self.pwm_lf = GPIO.PWM(4,0,50,100) # pwmchip4 -> GPIO pin 12(febe0030) left front 
        # Enable all wheels
        self.enable_pin_list = [35, 22, 15, 10]
        GPIO.output(self.enable_pin_list, True)

        self.pwm_rr.start_pwm()
        self.pwm_rf.start_pwm()
        self.pwm_lr.start_pwm()
        self.pwm_lf.start_pwm()

        self.stop_flag = False


    def stop(self):
        GPIO.output(self.enable_pin_list, False)

    def recover(self):
        GPIO.output(self.enable_pin_list, True)

    def exit(self):
        self.pwm_rr.stop_pwm()
        self.pwm_rf.stop_pwm()
        self.pwm_lr.stop_pwm()
        self.pwm_lf.stop_pwm()

        self.pwm_rr.pwm_close()
        self.pwm_rf.pwm_close()
        self.pwm_lr.pwm_close()
        self.pwm_lf.pwm_close()

        GPIO.cleanup()



class CarController_SideTurn(CarController_Base):

    """
    In this class, the car will turn base on speed difference between two sides of the wheel.
    """

    def __init__(self) -> None:
        
        super().__init__()

    def drive_forward(self,joy_left_x, joy_left_y, init_speed):
    
        GPIO.output([31,19,13,11],False)

        if joy_left_x < -0.05:      # turn left
            x_r = 1
            x_l = 1 + joy_left_x
        elif joy_left_x > 0.05:     # turn right
            x_r = 1 - joy_left_x
            x_l = 1 
        else:                       # tolerance for +/- 5%
            x_r = 1
            x_l = 1

        value_l = 100 - init_speed*joy_left_y*x_l
        value_r = 100 - init_speed*joy_left_y*x_r

        self.pwm_rr.duty_cycle(value_r)			
        self.pwm_rf.duty_cycle(value_r)
        self.pwm_lr.duty_cycle(value_l)
        self.pwm_lf.duty_cycle(value_l)

        # time.sleep(0.02) 
        print("Forward")

    def drive_back(self, joy_left_x, joy_left_y,init_speed):

        GPIO.output([31,33, 
                     18,19, 
                     13,16,
                     11,12], True)
        
        if joy_left_x < -0.05:      # turn left
            x_r = 1
            x_l = 1 + joy_left_x
        elif joy_left_x > 0.05:     # turn right
            x_r = 1 - joy_left_x
            x_l = 1 
        else:                       # tolerance for +/- 5%
            x_r = 1
            x_l = 1

        value_l = -1*init_speed*joy_left_y*x_l
        value_r = -1*init_speed*joy_left_y*x_r

        self.pwm_rr.duty_cycle(value_r)		
        self.pwm_rf.duty_cycle(value_r)
        self.pwm_lr.duty_cycle(value_l)
        self.pwm_lf.duty_cycle(value_l)

        #time.sleep(0.02) 
        print("Backward")



class CarController_CenterTurn(CarController_Base):

    """
    In this class, the car will turn around along its center axis.
    """

    def __init__(self) -> None:

        super().__init__()

    def drive_forward(self, joy_left_y, init_speed):
    
        GPIO.output([31,19,13,11],False)

        value_l = 100 - init_speed*joy_left_y
        value_r = 100 - init_speed*joy_left_y

        self.pwm_rr.duty_cycle(value_r)			
        self.pwm_rf.duty_cycle(value_r)
        self.pwm_lr.duty_cycle(value_l)
        self.pwm_lf.duty_cycle(value_l)

        # time.sleep(0.02) 
        print("Forward")

    def drive_back(self, joy_left_y, init_speed):

        GPIO.output([31,33, 
                     18,19, 
                     13,16,
                     11,12], True)
        
        value_l = -1*init_speed*joy_left_y
        value_r = -1*init_speed*joy_left_y

        self.pwm_rr.duty_cycle(value_r)		
        self.pwm_rf.duty_cycle(value_r)
        self.pwm_lr.duty_cycle(value_l)
        self.pwm_lf.duty_cycle(value_l)

        #time.sleep(0.02) 
        print("Backward")

    def drive_left(self, joy_left_x, init_speed):
        # x < 0

        GPIO.output([31,19,13,16,11,12],[False, False, True, True, True, True])
        
        value_l = -1*init_speed*joy_left_x
        value_r = 100 + init_speed*joy_left_x

        self.pwm_rr.duty_cycle(value_r)		
        self.pwm_rf.duty_cycle(value_r)
        self.pwm_lr.duty_cycle(value_l)
        self.pwm_lf.duty_cycle(value_l)

    def drive_right(self, joy_left_x, init_speed):
        # x > 0

        GPIO.output([31,33, 
                     18,19,
                     13,
                     11],[True, True, True, True, False, False])
        
        value_l = 100 - init_speed*joy_left_x
        value_r = init_speed*joy_left_x

        self.pwm_rr.duty_cycle(value_r)		
        self.pwm_rf.duty_cycle(value_r)
        self.pwm_lr.duty_cycle(value_l)
        self.pwm_lf.duty_cycle(value_l)





