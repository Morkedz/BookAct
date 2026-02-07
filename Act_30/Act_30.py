#requires installing adafruit-circuitpython-bmp280 library

from time import sleep
import board
import adafruit_bmp280

i2c = board.I2C()
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,address=0x76)

bmp280.sea_level_pressure = 1013.25

def loop():
    try:
        while True:
            print("\nTemperature: %0.1f C"%bmp280.temperature)
            print("Pressure:%0.1f hPa" % bmp280.pressure)
            print("Altitude = %0.2f meters" % bmp280.altitude)
            sleep(2)
    except KeyboardInterrupt:
        print("exit")

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        bmp280.close()