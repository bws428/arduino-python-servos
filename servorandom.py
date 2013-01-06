#!/usr/bin/env python

################################################
# Module:   servorandom.py
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
import random

t = 0.23 # sleep time

# center all servos
s = 1
while s <= 4:
    servo.move(s, 90)
    s += 1
time.sleep(1)

# move random servos to random angles
i = 0
while i < 80:
  serv = random.randrange(1, 5)
  ang =  random.randrange(0, 181, 30)
  servo.move(serv, ang)
  print "     servo.move(%d, %d)" % (serv, ang)
  time.sleep(t)
  i += 1

# wave goodbye
s = 1
while s <= 4:
    servo.move(s, 50)
    s += 1
    time.sleep(t)
time.sleep(t)
s = 1
while s <= 4:
    servo.move(s, 130)
    s += 1
    time.sleep(0.01)
time.sleep(t)
s = 1
while s <= 4:
    servo.move(s, 50)
    s += 1
    time.sleep(0.01)
time.sleep(t)
s = 1
while s <= 4:
    servo.move(s, 130)
    s += 1
    time.sleep(0.01)
time.sleep(1)

# re-center all servos
s = 1
while s <= 4:
    servo.move(s, 90)
    s += 1
    time.sleep(0.01)