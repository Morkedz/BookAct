from gpiozero import Button, MCP3008
from gpiozero.tools import absoluted, scaled
from signal import pause
from time import sleep

r_module = Button(17)
pot = MCP3008(channel = 0)

def pressed():
    print("rain")
    
def released():
    print("no rain")
    
r_module.when_pressed = pressed
r_module.when_released = released

def MAP(x, in_min, in_max, out_min, out_max):
    return (x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

def loop():
    while True:
        pot_vlue = pot.value
        pot_vlue = MAP(pot_vlue,0,1,0,100)
        print(pot_vlue)
        print("{:.2f}".format(pot_vlue))
        sleep(.5)
        
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        r_module.close()