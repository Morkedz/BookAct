from gpiozero import LED
from time import sleep

laser = LED(17)

def loop():
    while True:
        laser.on()
        sleep(0.5)
        laser.off()
        sleep(0.5)
        
def end():
    laser.close()
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()