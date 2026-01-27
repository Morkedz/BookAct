from gpiozero import MCP3008
from time import sleep

hall = MCP3008(channel = 0)

def loop():
    while True:
        act = hall.value * 255
        print(act)
        if act >=138:
            print("North")
        elif act <=128:
            print("South")
        else:
            print("no magnet")
        sleep(.5)
        
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        hall.close()