from gpiozero import Buzzer
from time import sleep

a_bz = Buzzer(pin=17,active_high=True)
a_bz.off()

def beep():
    while True:
        a_bz.on()
        sleep(.5)
        a_bz.off()
        sleep(.5)
def end():
    a_bz.close()
    
if __name__ == "__main__":
    try:
        beep()
    except KeyboardInterrupt:
        end()