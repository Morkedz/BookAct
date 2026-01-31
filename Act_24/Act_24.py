from gpiozero import DistanceSensor
from gpiozero import LED
from time import sleep

sensor = DistanceSensor(echo=17, trigger=18)

try:
    green.on()
    red.off()
    while True:
        dis=sensor.distance*100
        print("Distance: {:.2f} cm".format(dis))
        sleep(1)
        
except KeyboardInterrupt:
    pass
    sensor.close()
    red.close()
    green.close()