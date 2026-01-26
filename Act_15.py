from gpiozero import PWMLED,MCP3008
from gpiozero.tools import random_values
from time import sleep

pot = MCP3008(channel = 0)
led = PWMLED(17)

def loop():
    while True:
        potv = round(pot.value *1023)
        print(potv)
        led.source = pot
        sleep(0.5)
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        led.close()