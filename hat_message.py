#!/user/bin/env python

from sense_hat import SenseHat
sense = SenseHat()

x=3

for i in range(x+1):
        sense.show_message("Hello World")
