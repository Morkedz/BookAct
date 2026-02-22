#Stepmotor
from time import sleep
from gpiostepper import Stepper

speed = 300 #in rpm
steps = 32
motor = Stepper(motor_pins=[17,18,19,20], number_of_steps = steps)

motor.set_speed(speed)
gear_reduct = 64
spr = steps * gear_reduct

def rotary(clb_direction):
    if clb_direction == "a":
        motor.step(spr)
        sleep(1)
    elif clb_direction == "c":
        motor.step(-spr)
        sleep(1)

def loop():
    while True:
        clb_direction = input("Type 'a' for anticlockwise rotation, 'c' for clockwise")
        if clb_direction == "a":
            print("Running anticlockwise")
            break
        elif clb_direction == "c":
            print("Running clockwise")
            break
        else:
            print("Enter a valid input")
    while True:
        rotary(clb_direction)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        motor.close()