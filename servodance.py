#!/usr/bin/env python

################################################
# Module:   servodance.py
# Created:  2 April 2008
# Author:   Brian D. Wendt
#   http://principialabs.com/
# Version:  0.2
# License:  GPLv3
#   http://www.fsf.org/licensing/
'''
Fun test of the servo.py module.
'''
################################################

import servo
import time

#number of servos to dance
n = 4

#center all servos
s = 0
while s <= n:
    servo.move(s, 90)
    s += 1
time.sleep(0.5)

# perform 9 iterations, 10deg increments
i = 9
while i >= 1:

    units = i + 1    # units to pulse servo
    deg   = i * 10    # degrees moved L/R of center
    wait  = i * 0.025 # wait time - large deflections need more

    # move left
    servoPosition = 90 - deg
    # command Arduino
    s=0
    while s <= n:
      servo.move(s, servoPosition)
      time.sleep(wait)
      s += 1
    time.sleep(wait)

    # center
    servoPosition = 90
    # command Arduino
    s=0
    while s <= n:
      servo.move(s, servoPosition)
      time.sleep(wait)
      s += 1
    time.sleep(wait)

    # move right
    servoPosition = 90 + deg
    # command Arduino
    s=0
    while s <= n:
      servo.move(s, servoPosition)
      time.sleep(wait)
      s += 1
    time.sleep(wait)

    # center
    servoPosition = 90
    # command Arduino
    s=0
    while s <= n:
      servo.move(s, servoPosition)
      time.sleep(wait)
      s += 1
    time.sleep(wait)

    i -= 1