import board
import time
from adafruit_bme280 import basic as adafruit_bme280
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

print("Test: BME280 TempHumPres sensor")
print()
print("This script tries to read the values from your BME280 sensor attached to one of the I2C ports on your SkyCamOne HAT.")
print("Stop this test by pressing Ctrl-C or Command-C")
print()

try:
   while True:
      print("\nTemperature: %0.1f C" % bme280.temperature)
      print("Humidity: %0.1f %%" % bme280.humidity)
      print("Pressure: %0.1f hPa" % bme280.pressure)
      time.sleep(1)

except KeyboardInterrupt:
   print("Script stopped.")
