from time import sleep
from typing import Any
import RPi.GPIO as GPIO

def run():
    gpio_pin = 17
    GPIO.setmode(GPIO.BOARD)
    # NB: setup pins as output
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    # NB: set pin 1 to 3.3V and pin 2 to 0V
    print("On")
    GPIO.output(gpio_pin, GPIO.HIGH)
    sleep(3)
    # NB: set both pins to 0V
    print("Off")
    GPIO.output(gpio_pin, GPIO.LOW)
    sleep(3)
    print("On")
    GPIO.output(gpio_pin, GPIO.HIGH)
    sleep(3)
    # NB: set both pins to 0V
    print("Off")
    GPIO.output(gpio_pin, GPIO.LOW)
    sleep(3)

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    print("Program starting...")
    try:
        run()
    except KeyboardInterrupt:
        cleanup()
    finally:
        cleanup()
