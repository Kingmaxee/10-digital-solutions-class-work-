from sense_hat import SenseHat
import random
import time
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


sense.show_message("click to start")
sense.set_pixels(clear)
#Set random numbers (random.randit(1,4))
# Making it loop infinately
while True:
    run = 0
    while run == 0:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                run = 1



    while run == 1:
    #Setup ends here
        anum = 1 
        ana = 0
        clock = 0
        trys = 0
        average = 0 
        #for num in range(1,11):
        while trys != 9:
            if clock == 0:
                trys = trys - 1 
            anum =(random.randint(1,4))
            pause =(random.randint(10,40)/15)
            if anum == 1:
                arrow = up_arrow
            elif anum == 2:
                arrow = right_arrow
            elif anum == 3:
                arrow = down_arrow
            elif anum == 4:
                arrow = left_arrow
            sense.set_pixels(arrow)
            start_time = time.time()
            
            
            #Checking for movment in the joystick
            while ana != anum:
                for event in sense.stick.get_events():
               # Check if joystick is pressed
                    if event.action == 'pressed':
                    
                    # Check which direcion has been pressed
                        if event.direction == 'up':
                            ana = 1
                        elif event.direction == 'right':
                            ana = 2
                        elif event.direction == 'down':
                            ana = 3
                        elif event.direction == 'left':
                            ana = 4
                            
                            
                            
            
            
          #Make function of calling the arrow, then just
          # Calling time 
          
            sense.clear()
            
            clock = (round(time.time()-start_time,2))
            time.sleep(pause)
            trys = trys + 1
            print(clock)
            
            average = (average + clock)
            

        # adding the orientation feature 

            
            

        #Check to see if the code works correctly up until this point 
        sense.show_letter("M")


                
        a = sense.get_accelerometer_raw()
        x = a["x"]
        y = a["y"]
        z = a["z"]
                #Rounding orientation variables in sense.show_message
                #Printing final message 
        sense.show_message("Your:" f" AVG:{(average)/10} X:{round(x, 2)} Y:{round(y, 2)} Z:{round(z, 2)}")
        #Checking that the code runs
        print('finished')
        #Ending the loop
        run = 0        
