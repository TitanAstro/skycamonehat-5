from gpiozero import OutputDevice
from time import sleep

DEW = OutputDevice(17)

print("Test: Dew heater")
print()
print("This script cycles the dew heater output between ON and OFF every 3 seconds")
print("Stop this test by pressing Ctrl-C or Command-C")
print()
try:
	while True:
		print("Heater on")
		DEW.value = 1
		sleep(3)
		print("Heater off")
		DEW.value = 0
		sleep(3)
except KeyboardInterrupt:
	print("Script stopped." )
