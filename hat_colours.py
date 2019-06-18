#!/usr/bin/env pyhton

from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 0, 255)
blue = (0, 255, 255)

speed = 0.05

message = "XDXDXDXDXD"

x = 20
for i in range(x+1):
	sense.show_message(message, speed, text_colour=yellow,back_colour=blue)

sense.clear()
