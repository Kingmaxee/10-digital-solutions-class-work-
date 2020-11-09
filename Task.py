from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

blue = (0,0,255)
red = (255,0,0)

x = 4
y = 4
Coord = sense.set_pixel(x,y,blue)


#while True:
 #   for event in sense.stick.get_events():
        
  #      if event.action == 'pressed':
            
   #         if event.direction == 'up':
    #            y = y+1
    


while True:
    for event in sense.stick.get_events():
        # Check if joystick is pressed
        if event.action == 'pressed':
            
            # Check which direcion has been pressed
            if event.direction == 'up':
                y = y+1
            elif event.direction == 'down':
                y = y-1
            elif event.direction == 'left':
                x = x-1
            elif event.direction == 'right':
                x = x+1
            elif event.direction == 'middle':
                 sense.show_letter('M')
        
            
        

