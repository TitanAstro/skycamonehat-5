#!/usr/bin/env python

# Titan Astro SkyCamOne Focus Tool v.1.1
# * Experimental *

from time import sleep
import sys
from gpiozero import OutputDevice

IN1 = OutputDevice(20)
IN2 = OutputDevice(21)
IN3 = OutputDevice(26)
IN4 = OutputDevice(19)

step_sequence = [ 
	[1, 0, 0, 0],
	[1, 1, 0, 0],
	[0, 1, 0, 0],
	[0, 1, 1, 0],
	[0, 0, 1, 0],
	[0, 0, 1, 1],
	[0, 0, 0, 1],
	[1, 0, 0, 1]
]

def set_step (w1, w2, w3, w4):
	IN1.value = w1
	IN2.value = w2
	IN3.value = w3
	IN4.value = w4

def step_motor(steps, direction=1, delay=0.001):
	print ("Moving %d steps with direction %d."%(steps,direction))
	for _ in range(steps):
		for step in (step_sequence if direction > 0 else reversed(step_sequence)):
			set_step(*step)
			sleep(delay)

print("Titan Astro Manual focus tool")
print()
print("This script helps you manually focus with the STEPPER1 header of your SkyCamOne HAT")
print("Stop this program by pressing Ctrl-C or Command-C")
print()

# Read command line options. If none, print help message and exit.
if len(sys.argv) <= 1:
    print("ERROR: Please provide number of steps, either positive or negative. 100 is a good start.\n\n")
    sys.exit()
else:
    try:
        steps = int(sys.argv[1])
    except ValueError:
        try:
            steps = float(sys.argv[1])
            print("ERROR: You requested an invalid amount of steps. Whole numbers only, please. Either positive or negative, e.g.: 100 or -100\n\n")
            sys.exit()
        except ValueError:
            print("ERROR: You requested an invalid amount of steps. Please only use whole numbers.\n\n")
            sys.exit()


try:
	if steps < 0:
 		direction = -1
	else:
		direction = 1;
	steps = abs(steps);
	step_motor(steps, direction)
except KeyboardInterrupt:
	print(" Program stopped" )
