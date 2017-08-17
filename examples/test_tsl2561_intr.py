#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tsl2561 import TSL2561
import RPi.GPIO as GPIO
import sys
import os
import time
count=0x0
tsl2561_int = 23  # the Raspberry Pi port where the interrupt is connected to.

tsl = TSL2561(debug=False, autogain=False, gain=0, integration_time=0)
tsl.enable()
tsl.disableInterrupt()
tsl.setInterruptThresholdLow(0x0,0x0)
tsl.setInterruptThresholdHigh(0xE0,0x0)
tsl.enableLevelInterrupt(2)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(tsl2561_int, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

def rising_edge_callback(channel):
    print "edge detected"
    global count 
    ir  = tsl.readWord(0x8E)
    if ir is not 0:
        count += 1
    os.system("clear")
    print "Interrupt count: %i"  % count

GPIO.add_event_detect(tsl2561_int, GPIO.FALLING)    
GPIO.add_event_callback(tsl2561_int, rising_edge_callback)
while True:
    try:
        time.sleep(1)
        if GPIO.input(tsl2561_int) == 0:
            ir  = tsl.readWord(0x8E)
            if ir is not 0:
                tsl.clearInterrupt()
                print "interrupt cleared"

    except KeyboardInterrupt:
        sys.exit(0)
    except:
        sys.exit(1)
