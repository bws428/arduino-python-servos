#!/usr/bin/env python

################################################
# Module:   servomarch.py
# Created:  23 December 2009
# Author:   Brian D. Wendt
#   http://principialabs.com/
# Version:  0.2
# License:  GPLv3
#   http://www.fsf.org/licensing/
'''
Another fun test of the servo.py module.
'''
################################################

import servo
import time

# set number of servos to march
servos = 4

# marching orders
t = 0.3 # give servos time to move
deflection = 12 #degrees from center

# fall in
s = 1
while s <= servos:
	servo.move(s, 90)
	s += 1
	time.sleep(0.01)

# march servos, joining one at a time
march=1
while march < servos+1:
	i = 8
	while i >0:
		s = 1
		while s <= march:
			servo.move(s, 90-deflection)
			s += 1
		time.sleep(t)
		s = 1
		while s <= march:
			servo.move(s, 90+deflection)
			s += 1
		time.sleep(t)
		i -= 1
	march += 1

# final salute
s = 1
while s <= servos:
    servo.move(s, 75)
    s += 1
    time.sleep(t)
time.sleep(t)
s = 1
while s <= servos:
    servo.move(s, 100)
    s += 1
time.sleep(0.1)
s = 1
while s <= servos:
    servo.move(s, 80)
    s += 1
time.sleep(0.1)
s = 1
while s <= servos:
    servo.move(s, 110)
    s += 1
time.sleep(0.1)
s = 1
while s <= servos:
    servo.move(s, 90)
    s += 1
time.sleep(1)