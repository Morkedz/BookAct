from gpiozero import Button
from gpiozero import LED
from signal import pause

green = LED(21)
red = LED(18)
vibrate = Button(17)

red.on()
green.off()

def on():
    green.off()
    red.on()

def off():
    red.off()
    green.on()
    
vibrate.when_released = off
vibrate.when_pressed = on
    
def loop():
    pause()
    
def end():
    vibrate.close()
    red.close()
    green.close()
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()