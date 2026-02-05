from gpiozero import Button, LED
from time import sleep
from signal import pause
Obstacle = Button(17,pull_up=True)

def loop():
    while True:
        if Obstacle.is_pressed:
            print("Barrier Detected")
            sleep(1)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        Obstacle.close()