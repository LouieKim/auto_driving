from control_device.drive import Drive_commend
from control_device.ultra_sensor import  ultra_sensor
import random

class Automate():
    def __init__(self):
        self.drive = Drive_commend()
        self.sensor = ultra_sensor()
        self.danger_distance = 16

    def check_front(self):
        curDis = self.sensor.distance("cm")
        print("font distance: ", curDis)
        return curDis

    def auto_drive(self):
        while True:
            check_object = self.check_front()

            if check_object < self.danger_distance:
                self.drive.stop()

                x = random.randrange(0, 2)

                if x == 0:
                    self.drive.turn_left(1)
                elif x == 1:
                    self.drive.turn_right(1)
            else :
                self.drive.forward()