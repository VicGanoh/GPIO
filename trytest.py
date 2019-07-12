import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
from gpiozero import Button
from gpiozero import LED
from signal import pause

GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=(23) 
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
while True:
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
    sleep(0.5)
led = LED(17)

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(1)
    
led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()

button = Button(2)

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing

    
