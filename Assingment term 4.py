from sense_hat import SenseHat
from time import sleep
from random import randint
import random
sense = SenseHat()

#All setup 

#define colours

# Specified colour for the arrows
R = (102,51,0)

# colour to make the LEDS blank
N = (0,0,0)


#Clear starting menu
clear = [
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    ]


# setting up arrows
up_arrow = [
    N,N,N,N,N,N,N,N,
    N,N,N,R,R,N,N,N,
    N,N,R,R,R,R,N,N,
    N,R,R,R,R,R,R,N,
    N,N,N,R,R,N,N,N,
    N,N,N,R,R,N,N,N,
    N,N,N,R,R,N,N,N,
    N,N,N,N,N,N,N,N,
    ]
down_arrow = [
    N,N,N,N,N,N,N,N,
    N,N,N,R,R,N,N,N,
    N,N,N,R,R,N,N,N,
    N,N,N,R,R,N,N,N,
    N,N,N,R,R,N,N,N,
    N,R,R,R,R,R,R,N,
    N,N,R,R,R,R,N,N,
    N,N,N,R,R,N,N,N,
    ]

left_arrow = [
    N,N,N,N,N,N,N,N,
    N,N,R,N,N,N,N,N,
    N,R,R,N,N,N,N,N,
    R,R,R,R,R,R,R,N,
    R,R,R,R,R,R,R,N,
    N,R,R,N,N,N,N,N,
    N,N,R,N,N,N,N,N,
    N,N,N,N,N,N,N,N,
    ]

right_arrow = [
    N,N,N,N,N,N,N,N,
    N,N,N,N,N,R,N,N,
    N,N,N,N,N,R,R,N,
    N,R,R,R,R,R,R,R,
    N,R,R,R,R,R,R,R,
    N,N,N,N,N,R,R,N,
    N,N,N,N,N,R,N,N,
    N,N,N,N,N,N,N,N,
    ]
arrow = clear



sense.set_pixels(clear)
#Set random numbers (random.randit(1,4))

#Setup ends here
anum = 1 

for num in range(1,10):
    anum =(random.randint(1,4))
    if anum == 1:
        arrow = up_arrow
    elif anum == 2:
        arrow = down_arrow
    elif anum == 3:
        arrow = left_arrow
    else:
        anum == right_arrow
    sense.set_pixels(arrow)
    print(anum)
#while True:
 #   sleep(1)
  #  sense.flip_h()