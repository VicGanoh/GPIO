from subprocess import call
from gpiozero import Button

button = Button(2)

def print_thing():
    print ("button pressed")

button.when_pressed = print_thing