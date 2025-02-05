import time
import board
import adafruit_sht31d

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_sht31d.SHT31D(i2c)

loopcount = 0

print("Test: SHT31D TempHum sensor")
print()
print("This script tries to read the values from your SHT31D sensor attached to one of the I2C ports on your SkyCamOne HAT. ")
print("Stop this test by pressing Ctrl-C or Command-C")
print()


try: 
   while True:
      print("\nTemperature: %0.1f C" % sensor.temperature)
      print("Humidity: %0.1f %%" % sensor.relative_humidity)
      loopcount += 1
      time.sleep(1)
      # every 5 passes turn on the heater for 1 second
      if loopcount == 5:
        loopcount = 0
        sensor.heater = True
        print("Sensor Heater status =", sensor.heater)
        time.sleep(1)
        sensor.heater = False
        print("Sensor Heater status =", sensor.heater)

except KeyboardInterrupt:
	print("Script stopped.")

