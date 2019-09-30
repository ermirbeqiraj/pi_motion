from gpiozero import MotionSensor
from time import sleep
from physical_indication import LedIndication

pir = MotionSensor(24)
notify = LedIndication(interval=0.1, times=15, motion_gpio_pin=25, armed_gpio_pin=7)

print("Waiting for PIR to settle")
pir.wait_for_no_motion()

notify.armed()

while True:
    try:
        print("PIR is Ready")
        pir.wait_for_motion()
        print("PIR detected motion.")
        notify.run()
    except KeyboardInterrupt:
        exit()