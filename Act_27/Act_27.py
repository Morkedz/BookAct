#DHT11, module that composes of humidity sensor and thermistor; T
import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11

def loop():
    while True:
        try: 
            c = dht.temperature
            f = c*(9/5)+32
            humidity = dht.humidity
            print(f"Temp: {f:.2f} F, {c:2f} C. Humidity: {humidity}%")
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2)
            continue
        except Exception as error:
            dht.exit()
            raise error
        time.sleep(2)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        pass