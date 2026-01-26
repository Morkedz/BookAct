from gpiozero import Button
from gpiozero import LED
from signal import pause

red = LED(18)
tilt = Button(17)
green = LED(21)

red.on()
green.off()

def on():
    green.on()
    red.off()

def off():
    red.on()
    green.off()
    
tilt.when_released = off
tilt.when_pressed = on
    
def loop():
    pause()
    
def end():
    red.close()
    green.close()
    tilt.close()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()