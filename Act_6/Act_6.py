from gpiozero import Button
from gpiozero import LED
from signal import pause

green = LED(21)
red = LED(18)
button = Button(17)

red.on()
green.off()

def on():
    green.on()
    red.off()

def off():
    red.on()
    green.off()
    
button.when_released = off
button.when_pressed = on
    
def loop():
    pause()
    
def end():
    red.close()
    green.close()
    button.close()
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()