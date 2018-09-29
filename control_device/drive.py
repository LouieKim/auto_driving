import sys
import time
import pygame
import RPi.GPIO as gpio

class Drive_commend():
    
    L_forward = 12
    L_reverse = 16
    R_forward = 20
    R_reverse = 21
    timeDelay = 1
    gpio.cleanup()
    
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.cleanup()
        gpio.setup(self.L_forward, gpio.OUT)
        gpio.setup(self.L_reverse, gpio.OUT)
        gpio.setup(self.R_forward, gpio.OUT)
        gpio.setup(self.R_reverse, gpio.OUT)
    
    def stop(self):
        gpio.output(self.L_forward, False)
        gpio.output(self.L_reverse, False)
        gpio.output(self.R_forward, False)
        gpio.output(self.R_reverse, False)
        print("car is stop")
        
    def forward(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_forward, True)
        gpio.output(self.R_forward, True)
        print("car is driving")
        
    def reverse(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_reverse, True)
        gpio.output(self.R_reverse, True)
        print("car is reversing")
        
    def forward_left(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.R_forward, True)
        print("car is turning forward_left")
        
    def forward_right(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_forward, True)    
        print("car is turning forward_right")
        
    def reverse_left(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.R_reverse, True)
        print("car is turning reverse_left")
        
    def reverse_right(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_reverse, True)
        print("car is turning reverse_right")
    
    def turn_right(self, tf = 0):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_forward, True)
        gpio.output(self.R_reverse, True)
        print("car is turning right")
        time.sleep(tf)
        self.stop()
        
    def turn_left(self, tf = 0):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_reverse, True)
        gpio.output(self.R_forward, True)
        print("car is turning left")
        time.sleep(tf)
        self.stop()
        
    def control_wheel(self):
        
        run = True
        
        try:
            while run:
                key_press = input()
                #forward left
                if key_press == 'q':
                    self.forward_left()
                
                #forward
                elif key_press == 'w':
                    print("press key w")
                    self.forward()
                
                #forward right
                elif key_press == 'e':
                    self.forward_right()
                
                #turning left
                elif key_press == 'a':
                    self.turn_left()
                
                #stop
                elif key_press == 's':
                    self.stop()
                    
                #turning right
                elif key_press == 'd':
                    self.turn_right()
                    
                #reverse left
                elif key_press == 'z':
                    self.reverse_left()
                    
                #reverse
                elif key_press == 'x':
                    self.reverse()
                    
                #reverse right
                elif key_press == 'c':
                    self.reverse_right()

                    
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            exit()			
        
        finally:
            exit()
                
    def main(self):
        self.control_wheel()


class Drive_panel():
    
    L_forward = 12
    L_reverse = 16
    R_forward = 20
    R_reverse = 21
    timeDelay = 1
    gpio.cleanup()
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.cleanup()
        gpio.setup(self.L_forward, gpio.OUT)
        gpio.setup(self.L_reverse, gpio.OUT)
        gpio.setup(self.R_forward, gpio.OUT)
        gpio.setup(self.R_reverse, gpio.OUT)
    
    def stop(self):
        gpio.output(self.L_forward, False)
        gpio.output(self.L_reverse, False)
        gpio.output(self.R_forward, False)
        gpio.output(self.R_reverse, False)
        print("car is stop")
        
    def forward(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_forward, True)
        gpio.output(self.R_forward, True)
        print("car is driving")
        
    def reverse(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_reverse, True)
        gpio.output(self.R_reverse, True)
        print("car is reversing")
        
    def forward_left(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.R_forward, True)
        print("car is turning forward_left")
        
    def forward_right(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_forward, True)    
        print("car is turning forward_right")
        
    def reverse_left(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.R_reverse, True)
        print("car is turning reverse_left")
        
    def reverse_right(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_reverse, True)
        print("car is turning reverse_right")
    
    def turn_right(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_forward, True)
        gpio.output(self.R_reverse, True)
        print("car is turning right")
        
    def turn_left(self):
        self.stop()
        time.sleep(self.timeDelay)
        gpio.output(self.L_reverse, True)
        gpio.output(self.R_forward, True)
        print("car is turning left")
        
    def control_wheel(self):
        pygame.init()
        screen = pygame.display.set_mode((300, 100))
        pygame.display.set_caption("control_car")
        
        clock = pygame.time.Clock()
        run = True
        
        screen.fill(pygame.color.Color(255, 255, 255))
        pygame.display.flip()    
        clock.tick(60)
        
        try:
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                keys = pygame.key.get_pressed()
                
                #forward left
                if keys[pygame.K_q]:
                    self.forward_left()
                
                #forward
                elif keys[pygame.K_w]:
                    print("press key w")
                    self.forward()
                
                #forward right
                elif keys[pygame.K_e]:
                    self.forward_right()
                
                #turning left
                elif keys[pygame.K_a]:
                    self.turn_left()
                
                #stop
                elif keys[pygame.K_s]:
                    self.stop()
                    
                #turning right
                elif keys[pygame.K_d]:
                    self.turn_right()
                    
                #reverse left
                elif keys[pygame.K_z]:
                    self.reverse_left()
                    
                #reverse
                elif keys[pygame.K_x]:
                    self.reverse()
                    
                #reverse right
                elif keys[pygame.K_c]:
                    self.reverse_right()

                    
        except Exception as e:
            print(e)
        
        finally:
            pygame.quit()
                
    def main(self):
        self.control_wheel()        
        
if __name__ == "__main__":
    pass

