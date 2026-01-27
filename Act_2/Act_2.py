from gpiozero import RGBLED
from colorzero import Color
from time import sleep

colors = ["red","green","blue","magenta","cyan","yellow","white","black"]

led_light = RGBLED(13,17,20)

def loop_light():
    while True:
        for col in colors:
            led_light.color = Color(col)
            sleep(1)
        
def end():
    led_light.close

if __name__ == "__main__":
    try:
        loop_light()
    except KeyboardInterrupt:
        end()        