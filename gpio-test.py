import RPi.GPIO as GPIO
print("importing RPi.GPIO !!!!");
import time
print("importing time !!!");

channels = [40]
GPIO.setmode(GPIO.BOARD);

GPIO.setup(40, GPIO.OUT)

print("GPIO BD pin 40 setup finished, start toggle !!!")
for a in range(1000):
   print a
   print("GPIO high please measure")
   GPIO.output(40, GPIO.HIGH)
   time.sleep(0.05)
   print("GPIO low please measure")
   GPIO.output(40, GPIO.LOW)
   time.sleep(0.05)

GPIO.cleanup()
