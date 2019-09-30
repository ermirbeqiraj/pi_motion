from gpiozero import LED
from time import sleep

class LedIndication:
    
    def __init__(self, interval = 0.1, times = 15, motion_gpio_pin = 25, armed_gpio_pin=7):
        self.interval = interval
        self.times = times
        self.led = LED(motion_gpio_pin)
        self.green_led = LED(armed_gpio_pin)

    def run(self):
        self.armed(False)

        runfor = 0
        while runfor < self.times:
            self.led.on()
            sleep(self.interval)
            self.led.off()
            sleep(self.interval)
            runfor += 1
        
        self.armed()
    
    def armed(self, on=True):
        if on:
            self.green_led.on()
        else:
            self.green_led.off()
