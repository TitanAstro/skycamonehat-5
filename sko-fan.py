from gpiozero import PWMOutputDevice
import time
import signal
import sys
import os

FAN_PIN = 7
WAIT_TIME = 2
PWM_FREQ = 25

FAN_LOW = 11
FAN_HIGH = 99
FAN_OFF = 10
FAN_MAX = 100

MIN_TEMP = 37
MAX_TEMP = 68

#Get CPU temp
def getCPUTemperature():
	with open('/sys/class/thermal/thermal_zone0/temp') as f:
		return float(f.read()) / 1000

def setFanSpeed(speed):
	pwm_fan.value = 1 - (speed / 100)
	return()

def HandleFanSpeed():
	temp = float(getCPUTemperature())
	if temp < MIN_TEMP:
		setFanSpeed(FAN_OFF)
		print("Fan OFF")
	elif temp > MAX_TEMP:
		setFanSpeed(FAN_MAX)
		print("Fan MAX")
	else:
		step = (FAN_HIGH - FAN_LOW)/(MAX_TEMP - MIN_TEMP)
		setFanSpeed(FAN_LOW + (round((temp - MIN_TEMP) * step )))
	print ("Temp: %.2f\xb0C, PWM: %.0f%%" % (temp, (1-pwm_fan.value)*100))
	return()

print("Test: PC Fan")
print()
print("This script reads the temperature of your Raspberry Pi processor and regulates the speed of your PC fan attached to the FAN header of your SkyCamOne HAT.")
print("Stop this test by pressing Ctrl-C or Command-C")
print()

try:
   pwm_fan = PWMOutputDevice(FAN_PIN, initial_value = 0, frequency = PWM_FREQ)
   setFanSpeed(FAN_OFF)
   while True:
      HandleFanSpeed()
      time.sleep(WAIT_TIME)

except KeyboardInterrupt:
   print("Script stopped.")
   setFanSpeed(FAN_LOW)

finally: 
   pwm_fan.close()
