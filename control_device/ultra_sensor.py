import RPi.GPIO as gpio
import time

class ultra_sensor():

    eco_send_pin = 12
    eco_receive_pin = 16

    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.eco_send_pin, gpio.OUT)
        gpio.setup(self.eco_receive_pin, gpio.IN)

        gpio.output(self.eco_send_pin, False)

    def distance(self, measure = "cm"):
        while gpio.input(self.eco_receive_pin) == 0:
            nosig = time.time()

        while gpio.intput(self.eco_receive_pin) == 1:
            sig = time.time()

        t1 = sig - nosig

        if measure == "cm":
            distance = t1 / 0.000058
        elif measure == "in":
            distance = t1 / 0.000148
        else:
            print("impreper choice mease")
            distance = None

        return distance