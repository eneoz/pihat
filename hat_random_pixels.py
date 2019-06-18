#!/user/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time
import random


for i in range(50+1):
        r = random.randint(0,7)
        a = random.randint(0,7)
        sense.set_pixel(r,a, (255,0,255))
        sense.set_pixel(a,r, (255,0,255))
        time.sleep(1)
        sense.set_pixel(r,a, (0,0,0))
        sense.set_pixel(a,r, (0,0,0))
        time.sleep(1)

        sense.clear()
