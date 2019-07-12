from gpiozero import LED
from time import sleep
from signal import pause

red = LED(17)
yellow = LED(11)
green = LED(26)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
    yellow.on()
    sleep(1)
    yellow.off()
    sleep(1)
    green.on()
    sleep(1)
    green.off()
    sleep(1)
    


    