from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

cl = [220,220,220,220,220,220,220,248]
cm = [220,262,294,330,350,393,441,495]
ch = [220,525,589,661,7000,786,800,880]

pitch = [cm[3],cm[5],cm[6],cm[3],cm[2],cm[3],cm[5],cm[6],ch[1],cm[6],cm[5],cm[1],cm[3],cm[2],cm[2],cm[3],
          cm[5],cm[2],cm[3],cm[3],cl[6],cl[6],cl[6],cm[1],cm[2],cm[3],cm[2],cl[7],cl[6],cm[1],cl[5]]

beat = [1,1,3,1,1,3,1,1,1,1,1,1,1,1,3,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,3]

p_bz = TonalBuzzer(17)
p_bz.stop()

def loop():
    while True:
        for i in range(0,len(pitch)):
            p_bz.play(Tone(pitch[i]))
            sleep(beat[i]*.5)
        sleep(1)
    
def end():
    p_bz.stop()
    
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        end()