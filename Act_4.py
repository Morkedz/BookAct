from gpiozero import LED
from time import sleep

relay_pin = LED(17)

def setup():
    relay_pin.off()
    
def loop():
    while True:
        relay_pin.on()
        sleep(1)
        relay_pin.off()
        sleep(1)
        
def end():
    relay_pin.close()
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()