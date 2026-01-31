#use setup from Act_9_2.py

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

speed = .4

pitch = ["F4","B4","C5","Bb4","Ab4","Bb4","Ab4","F4","Ab4","F4","Eb4","F4","Eb4"]

beat = [1,.1,3,.66,.33,1,.66,.33,1,.66,.33,1.66,1]

bz = TonalBuzzer(17)

def loop():
    while True:
        for i in range(0,len(pitch)):
            bz.play(pitch[i])
            sleep(beat[i]*speed)
        bz.stop()
        sleep(4.33*speed)
        
def end():
    bz.stop()
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()