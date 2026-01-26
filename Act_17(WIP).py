from gpiozero import Button, MCP3008
import math
from time import sleep

temp_pin = MCP3008(channel = 0)
temp_but = Button(17)

def print_cond(cond):
    if cond == 1:
        print("appropriate")
    else:
        print("hot")

def loop():
    status = 1
    tmp = 1
    while True:
        ana = temp_pin.value
        vr = float(ana)*3.3
        rt = 10000*vr/(3.3-vr)
        new_temp = 1/(((math.log(rt/10000))/3950) + (1/273.15+25))
        c = new_temp
        f = c *(9/5)+32
        print("temp c={:.2f}\ttemp f={:.2f}".format(c,f))
        tmp = not temp_but.is_pressed
        if tmp != status:
            print_cond(tmp)
            status = tmp
        sleep(.5)
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        pass