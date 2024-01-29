import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray, Float64
from car_driver.gpio_init import CarController_SideTurn
import time

class CarDriver(Node):
    """
    Publication: None
    Subscription: /mux (Float32MultiArray [x,y] which is the control value in direction of [])
    Description: subscribe to control value that published by mux node and drive the car
    """
    def __init__(self):

        super().__init__('driver')

        self.sub = self.create_subscription(Float64MultiArray, 
                                            '/controller/mux',self.call_back, 10)
        self.car = CarController_SideTurn()

    def call_back(self, msg):

        x, y, t = msg.data

        if y > 0:
            self.car.drive_forward(x,y,100)
            self.car.recover()
        elif y < 0:
            self.car.drive_back(x,y,100)
            self.car.recover()
        else:
            self.car.stop()
        delta_t = (time.time() - t)
        self.get_logger().info('Execution Time: "%s"' % delta_t)

def main(args=None):

    rclpy.init(args=args)
    driver = CarDriver()
    rclpy.spin(driver)

    driver.car.exit() # clean up all gpios
    driver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()