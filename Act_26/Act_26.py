#Rotary Encoder
from gpiozero import RotaryEncoder, Button
from time import sleep

encod = RotaryEncoder(a = 17, b=18)
button = Button(27)

Counter = 0
tmp = 0

def rotaryDeal():
    global Counter
    global tmp
    Counter += encod.steps
    encod.steps=0
    if tmp != Counter:
        print("Counter = %d" % Counter)
        tmp = Counter

def btnISR():
    global Counter
    Counter = 0
    print("Counter reset")

button.when_pressed = btnISR

if __name__ == "__main__":
    try:
        while True:
            rotaryDeal()
            sleep(0.1)
    except KeyboardInterrupt:
        encod.close()
        button.close()