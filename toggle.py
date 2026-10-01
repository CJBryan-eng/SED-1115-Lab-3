# Use the Pin method from the machine software library
from machine import Pin
#Import utime to sleep after switch
import utime


# Define the inputs and outputs and assign them to software objects
led1 = Pin(16, Pin.OUT)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

#led starts off
led1.off()

#Code keeps running
while True:

    #All switches affect 1 led
    if sw5.value() == 1 or sw4.value() == 1 or sw3.value() == 1 or sw2.value() == 1 or sw1.value() == 1: 
        
        #led turns oposite of current state
        led1.toggle() 
        
        #switches sleep after first press
        utime.sleep_ms(200)
