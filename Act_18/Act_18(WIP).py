from gpiozero import Button, MCP3008
from time import sleep

voice_pin = MCP3008(channel = 0)

def MAP(s, in_min, in_max, out_min, out_max):
    return (s-in_min)*(out_max-out_min)/(in_max-in_min)+out_min

def loop():
    count=0
    while True:
        voice_v = voice_pin.value
        voice_v = round(MAP(voice_v,0,1,0,255))
        if voice_v:
            print(voice_v)
            if voice_v < 100:
                count+=1
                sleep(1)
            
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        pass