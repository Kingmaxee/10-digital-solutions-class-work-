from sense_hat import SenseHat
from time import sleep
from random import randint 
sense = SenseHat()

def pick_colour_colour():
    random_red = randint(0,255)
    random_green = randint(0,255)
    random_blue = randint(0,255)
    return(random_red,random_green,random_blue)

sense.show_letter ("A", pick_random_colour())
sleep(.5)
sense.show_letter ("s", pick_random_colour())
sleep(.5)
sense.show_letter ("d", pick_random_colour())
sleep(.5)
sense.show_letter ("f", pick_random_colour())
sleep(.5)
sense.show_letter ("g", pick_random_colour())
sleep(.5)
sense.show_letter ("h", pick_random_colour())
sleep(.5)
sense.show_letter ("j", pick_random_colour())
sleep(.5)
sense.show_letter ("k", pick_random_colour())