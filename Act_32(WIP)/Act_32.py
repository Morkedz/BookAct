#DS1307 Component, Real Time Clock (RTC), communicates with I2C protocol (SDA SCL), binary-coded decimal clock calander.
#T
import sys
import time
import datetime
import SDL_DS1307

print("Program Started at " + time.strftime("%Y-%m-%d %H:%M:%S"))
#Coordinate to EST time