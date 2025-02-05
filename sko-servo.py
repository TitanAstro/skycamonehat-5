import warnings
warnings.filterwarnings('ignore', module='gpiozero')
from gpiozero import Servo
from time import sleep

servo = Servo(18)

print("Test: Servo")
print()
print("This script moves the servo attached to your SkyCamOne HAT hence and forth each second.")
print("If your servo does not actuate, try reversing the connector.")
print("Stop this script by pressing Ctrl-C or Command-C")

try:
   while True:
      print("Minimum")
      servo.min()
      sleep(1)
      print("Middle")
      servo.mid()
      sleep(1)
      print("Maximum")
      servo.max()
      sleep(1)

except KeyboardInterrupt:
   print("Script stopped.")
