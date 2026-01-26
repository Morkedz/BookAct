from gpiozero import Button, MCP3008
from time import sleep

flame_act = Button(18)
flame_pin = MCP3008(channel = 0)

def loop():
    condition = False
    while True:
        flame_val = round(flame_pin.value * 255)
        print(flame_val)
        current = flame_act.is_pressed
        if current != condition and current == True:
            print("flame detected")
            condition = True
        elif current != condition and current == False:
            print("flame lost")
            condition = False
        sleep(.5)
        
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        pass