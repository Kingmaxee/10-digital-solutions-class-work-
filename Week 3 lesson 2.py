from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

red = (255,0,0)
green = (0,255,0)
while True:
    # take reading from all 3 sensors
    temp = sense.get_temperature()
    press = sense.get_pressure()
    hum = sense.get_humidity()
    
    # round the values to one decimal
    temp = round(temp,1)
    press = round(temp,1)
    hum = round(temp,1)
    #create temp message
    message = "Temp: " +str(temp) 
    
    if temp > 18 and temp < 27:
        bg = green
    else:
        bg = red
        

    # Display temp message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)

 #create pressure message
    message = "Temp: " +str(temp) + "Pressure: " + str(press) + "Humidity: " + str(hum)
    
    if temp > 18 and temp < 27:
        bg = green
    else:
        bg = red
        

    # Display pressure message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)

 #create pressure message
    message = "Pressure: " + str(press) 
    
    if press > 979 and press < 1027:
        bg = green
    else:
        bg = red
        
 #create hum message
    message = "Humidity: " + str(hum)
    
    if hum > 55 and hum < 65:
        bg = green
    else:
        bg = red
        

    # Display hum message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)

    # Display message
    sense.show_message(message, scroll_speed = 0.075, back_colour = bg)
