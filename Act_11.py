from gpiozero import Button
from gpiozero import LED
from signal import pause

inf = Button(20)
green = LED(17)
red = LED(18)

red.on()
green.off()

def pres():
    green.off()
    red.on()
    
def abse():
    green.on()
    red.off()

def wait():
    pause()
    
def end():
    green.close()
    red.close()
    inf.close()
    
inf.when_pressed = pres
inf.when_released = abse
    
if __name__ == "__main__":
    try:
        wait()
    except KeyboardInterrupt:
        end()