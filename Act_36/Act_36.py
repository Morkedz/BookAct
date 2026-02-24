#Stepmotor
from time import sleep
from RpiMotorimport RpiMotorLib

speed = 300 #in rpm
steps = 32
motor = RpiMotorLib.BYJm_28BYJ48("stepper", "28BYJ48")

def loop():
    while True:
        motor.motor_run([17,18,19,20],.001,512,False, False, "half", .005)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        motor.close()