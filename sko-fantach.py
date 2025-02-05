#!/usr/bin/python
from gpiozero import Button
import time

PULSE = 2       # Noctua fans puts out two pluses per revolution
WAIT_TIME = 1   # [s] Time to wait between each refresh

tach = Button("GPIO8", pull_up=True)

# Setup variables
t = time.time()
rpm = 0

# Caculate pulse frequency and RPM
def fell():
    global t
    global rpm

    dt = time.time() - t
    if dt < 0.005:
        return  # Reject spuriously short pulses

    freq = 1 / dt
    rpm = (freq / PULSE) * 60
    t = time.time()

# Add event to detect
tach.when_released = fell 

print("Test: Fan Tachometer")
print()
print("This script tries to read the tachometer from your PC fan attached to the FAN header of your SkyCamOne HAT.")
print("It returns the RPM value each second.")
print("Stop this test by pressing Ctrl-C or Command-C")
print()

try:
    while True:
        print("%.f RPM" % rpm)
        rpm = 0
        time.sleep(1)   # Detect every second

except KeyboardInterrupt:   # trap a CTRL+C keyboard interrupt
    print("Script stopped.")
