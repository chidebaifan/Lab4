import RPi.GPIO as GPIO
from hal import hal_led as led
from hal import hal_input_switch as switch
import time
from time import sleep
def blink_led(delay):
    # Led Blink

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main():
    led.init()
    switch.init()
    while True:
        switchon = switch.read_slide_switch()
        if switchon ==1:
            blink_led(0.2)


        else:
            for i in range(25):
                blink_led(0.1)
            while switchon == 0:
                switchon = switch.read_slide_switch()
                sleep(0.1)


if __name__ == "__main__":
     main()

