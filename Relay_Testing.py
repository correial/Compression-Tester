from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def off():
    ("Status: OFF")
    RELAIS_1_GPIO = 22
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    sleep(.1)


def on():
    print ("Status: ON, IDLE")
    RELAIS_1_GPIO = 22
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    sleep(1)

def out():
    print ("Status: ON, OUT")
    RELAIS_1_GPIO = 17
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    sleep(5)

def intake():
    print ("Status: ON, IN")
    RELAIS_1_GPIO = 17
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    sleep(5)

def load_cell():
    X = 0
    RELAIS_1_GPIO = 25
    GPIO.setup(RELAIS_1_GPIO, GPIO.IN)
    X = GPIO.input(25)
    print(X)


on()
intake()
off()