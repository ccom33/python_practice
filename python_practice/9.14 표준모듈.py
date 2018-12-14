import math

print(math.sqrt(3))

from math import*

print(math.sqrt(10))

print(math.sinh(234))

print(math.gcd(1234325,2132155))

import math
import turtle as t
t.shape("turtle")
t.penup()
t.goto(-1080,0)
t.pendown()
for x in range(-1080,1080):
    t.goto(x,math.sin(math.radians(x))*100)
t.done()

