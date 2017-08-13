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

time_loop_init = 1.2
time_step = 0.2
time_max = 2
time_min = 0.2

time_init = 1.2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_toggle, GPIO.OUT)
GPIO.setup(switch_mid, GPIO.OUT)
GPIO.setup(switch_add, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_min, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(35, GPIO.HIGH)

def func_timer_add():
    global time_loop_init
    if GPIO.HIGH == GPIO.input(switch_add):
        print(' --- add long press --- ')
        time_loop_init = time_max
	

def func_timer_min():
    global time_loop_init
    if GPIO.HIGH == GPIO.input(switch_min):
        print(' --- min long press --- ')
        time_loop_init = time_min

def switch_add_cb(switch_add):
    global time_loop_init
    if time_loop_init < time_max:
        print (' --- add short press --- ')
        time_loop_init += time_step
        timer = threading.Timer(1, func_timer_add)
        timer.start()
    else:
        print ('reached max key press count')
  
def switch_min_cb(switch_min):
    global time_loop_init
    if time_loop_init > time_min:
        print (' --- min short press --- ')
        time_loop_init -= time_step
        timer = threading.Timer(1, func_timer_min)
        timer.start()
    else:
        print ('reached min  key press count')

GPIO.add_event_detect(switch_add, GPIO.RISING, callback = switch_add_cb, bouncetime = 300)
GPIO.add_event_detect(switch_min, GPIO.RISING, callback = switch_min_cb, bouncetime = 300)

print('Board and callbacks init finished!')

while True:
    GPIO.output(pin_toggle, GPIO.HIGH)
    time.sleep(time_loop_init)
    GPIO.output(pin_toggle, GPIO.LOW)
    time.sleep(time_loop_init)

print ('while loop started !')

#No need cleanup just keep it here for mindset
GPIO.clearnup()
