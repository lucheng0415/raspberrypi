#!/usr/bin/python  
# -*- coding: UTF-8 -*-  
# copy right Cheng Lu for non commercial use

import RPi.GPIO as GPIO  
import threading  
import time
# GPIO40 pulse control pin
# GPIO33 35 37 switch control pin
#
#

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(32, GPIO.HIGH)
GPIO.output(40, GPIO.HIGH)

timer_int = 1
step = 0.1
timer_max = 2
timer_min = 0.1

print('Board init finished!')

def fun_timer():
    if GPIO.HIGH == GPIO.input(40):
        GPIO.output(40, GPIO.HIGH)
    else:
        GPIO.output(40, GPIO.LOW)
    print('timer: timer_int', timer_int)
    global timer
    timer = threading.Timer(timer_int, fun_timer)
    timer.start()

timer = threading.Timer(timer_int, fun_timer)
timer.start()

while True:
    if  GPIO.HIGH == GPIO.input(36) and timer_int < timer_max:
	time.sleep(0.1)
    	if  GPIO.HIGH == GPIO.input(36) and timer_int < timer_max:
        	print ('add key detected: timer +step')
        	timer_int += step 
 
    if  GPIO.HIGH == GPIO.input(38) and timer_int > timer_min:
	time.sleep(0.1)
    	if  GPIO.HIGH == GPIO.input(38) and timer_int > timer_min:
        	print ('min key detected: timer -step')
        	timer_int -= step 

#No need cleanup just keep it here for mindset
GPIO.clearnup()
