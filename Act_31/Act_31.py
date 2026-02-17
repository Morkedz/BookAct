#MPU6050 6 axis altimeter sensor, 3 axis gyroscope (orientation) and 3 axis accelerometer.
#i2c bus device, need to install mpu6050-raspberrypi
#run with implementation required
from mpu6050 import mpu6050
from time import sleep

sens = mpu6050(0x68)

def loop():
    while True:
        accel = sens.get_accel_data()
        gyro = sens.get_gyro_data()
        temp = sens.get_temp()

        print("Accelerometer data")
        print("x: " + str(accel["x"]))
        print("y: " + str(accel["y"]))
        print("z: " + str(accel["z"]))
            
        print("Gyroscope data")
        print("x: " + str(gyro["x"]))
        print("y: " + str(gyro["y"]))
        print("z: " + str(gyro["z"]))

        print("Temperature: " + str(temp) + "C")
        sleep(1)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        print("Exit")
    