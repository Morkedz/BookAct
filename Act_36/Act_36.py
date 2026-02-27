#Stepmotor
import RPi.GPIO as GPIO
from RpiMotorLib.RpiMotorLib import BYJMotor

steps = 512
pins = [17,18,19,20]
motor = BYJMotor("stepper", "28BYJ48")

def loop():
    while True:
        motor.motor_run([17,18,19,20],.001,steps,False, False, "half", .005)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.output(pins, GPIO.LOW)
        GPIO.cleanup()