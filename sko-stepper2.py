from gpiozero import OutputDevice
from time import sleep

IN1 = OutputDevice(13)
IN2 = OutputDevice(12)
IN3 = OutputDevice(6)
IN4 = OutputDevice(5)

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
	for _ in range(steps):
		for step in (step_sequence if direction > 0 else reversed(step_sequence)):
			set_step(*step)
			sleep(delay)

print("Test: Stepper 2")
print()
print("This script tests the functioning of the stepper attached to the STEPPER2 header of your SkyCamOne HAT")
print("Stop this test by pressing Ctrl-C or Command-C")
print()

try:
	while True:
		steps = int(input(" Enter number of steps: "))
		direction = int(input(" Enter direction (1 for forward, -1 for backward): " ))
		step_motor(steps, direction)
except KeyboardInterrupt:
	print(" Program stopped" )
