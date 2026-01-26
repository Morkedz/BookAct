from gpiozero import MCP3008
from time import sleep

x = MCP3008(channel = 0)
y = MCP3008(channel = 1)
z = MCP3008(channel = 2)

def MAP(s, in_min, in_max, out_min, out_max):
    return (s-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

def find_direction():
    state = ["home","down","up","left","right","pressed"]
    i=0
    xv = round(x.value*1024)
    yv = round(y.value*1024)
    zv = round(z.value*1024)
    xv=round(MAP(xv,0,1023,0,255))
    yv=round(MAP(yv,0,1023,0,255))
    zv=round(MAP(zv,0,1023,0,255))
    print(xv)
    print(yv)
    print(zv)
    
    if xv<= 30:
        i=1
    if xv>=225:
        i=2
    if yv<=30:
        i=3
    if yv>=225:
        i=4
    if zv<=2:
        i=5
    return state[i]

def loop():
    while True:
        print(find_direction())
        sleep(.5)
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        pass