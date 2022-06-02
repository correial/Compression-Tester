from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# turns linear actuator off **must be the final line of code in "main function" **
def off():
    ("Status: OFF")
    RELAIS_1_GPIO = 22
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    sleep(.1)

# turns linear actuator off
def on():
    print ("Status: ON, IDLE")
    RELAIS_1_GPIO = 22
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    sleep(1)

# extends linear actuator arm
def out():
    print ("Status: ON, OUT")
    RELAIS_1_GPIO = 17
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    sleep(5) #time in which actuator arm is moving

# retracts linear actuator arm 
def intake():
    print ("Status: ON, IN")
    RELAIS_1_GPIO = 17
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    sleep(5) #time in which actuator arm is moving

def load_cell():
    X = 0
    RELAIS_1_GPIO = 25
    GPIO.setup(RELAIS_1_GPIO, GPIO.IN)
    X = GPIO.input(25)
    print(X)

'''
Here will be the while statement to stop the load cell at a specific threshold of force. 
The value (val) come from the hx711 exampl.py file

example: 

while val <= 50
    on()
    outake()

off()

'''