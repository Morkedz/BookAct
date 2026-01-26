from gpiozero import LED, Button
from time import sleep
from signal import pause

touch=Button(17)
red = LED(18)
green=LED(19)

red.on()
green.off()

def pressed():
    red.on()
    green.off()
    
def released():
    red.off()
    green.on()
    
touch.when_pressed=pressed
touch.when_released=released
    
if __name__ == "__main__":
    try:
        pause()
    except KeyboardInterrupt:
        green.close()
        red.close()