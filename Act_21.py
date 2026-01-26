from gpiozero import Button, Buzzer, MCP3008
from time import sleep

gas_ana = MCP3008(channel = 0)
gas_cond = Button(18)
buz = Buzzer(17)

def loop():
    condition = 0
    while True:
        gas_lvl = round(gas_ana.value * 255)
        print(gas_lvl)
        current = gas_cond.is_pressed
        if current != condition and current == False:
            print("safe")
            condition = current
            buz.on()
        elif current != condition and current == True:
            print("danger")
            condition = current
            buz.off()
        sleep(.5)
        
if __name__=="__main__":
    try:
        loop()
    except KeyboardInterrupt:
        buz.close()