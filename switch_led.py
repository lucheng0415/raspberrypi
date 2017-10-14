#!/usr/bin/python  
# -*- coding: UTF-8 -*-  
# copy right Cheng Lu for non commercial use

import RPi.GPIO as GPIO  
import threading  
import time


pin_toggle = 40
switch_mid = 35
switch_add = 33
switch_min = 37

time_loop_init = 0.1
time_step = 0.01/2
time_max = 1
time_min = 0.05

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_toggle, GPIO.OUT)
GPIO.setup(switch_mid, GPIO.OUT)
GPIO.setup(switch_add, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_min, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(35, GPIO.HIGH)

def switch_add_cb(switch_add):
    global time_loop_init
    if time_loop_init < time_max:
        print ('add pressed')
        time_loop_init += time_step
    else:
        print ('reached add key limitation')
  
def switch_reduce_cb(switch_min):
    global time_loop_init
    if time_loop_init > time_min:
        print ('reduce pressed')
        time_loop_init -= time_step
    else:
        print ('reached reduce key limitation')

GPIO.add_event_detect(switch_add, GPIO.RISING, callback = switch_add_cb, bouncetime = 1000)
GPIO.add_event_detect(switch_min, GPIO.RISING, callback = switch_reduce_cb, bouncetime = 1000)

print('Board and callbacks init finished!')

while True:
    GPIO.output(pin_toggle, GPIO.HIGH)
    ftime.sleep(time_loop_init)
    GPIO.output(pin_toggle, GPIO.LOW)
    ftime.sleep(time_loop_init)
print ('while loop started !')
#No need cleanup just keep it here for mindset
GPIO.clearnup()
