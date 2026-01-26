from gpiozero import Button
from gpiozero import LED
import matplotlib.pyplot as plt
import time
import threading

conclude = False
condition = False
x_data = []
y_data = []

mag = Button(17)
green = LED(20)
red = LED(18)

red.on()
green.off()

def mag_pres():
    global condition
    green.on()
    red.off()
    condition = True
    
def mag_abs():
    global condition
    green.off()
    red.on()
    condition = False

def evaluate():
    global conclude
    count = 0
    while not conclude:
        y_data.append(1 if condition else 0)
        x_data.append(count)
        
        count += 1
        time.sleep(1)

mag.when_pressed = mag_pres
mag.when_released = mag_abs

if __name__ == "__main__":
    data_thread = threading.Thread(target=evaluate)
    data_thread.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        conclude = True
        data_thread.join()
        plt.step(x_data, y_data)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Button State')
        plt.show()
        
        # Cleanup
        green.close()
        red.close()
        mag.close()