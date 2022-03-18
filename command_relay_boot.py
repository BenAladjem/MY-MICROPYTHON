from machine import Pin
import time

p4 = Pin(4,Pin.OUT)
p5 = Pin(5,Pin.OUT)
p6 = Pin(6,Pin.OUT)
p7 = Pin(7,Pin.OUT)

p1 = Pin(1,Pin.IN)
p2 = Pin(2,Pin.IN)
p3 = Pin(3,Pin.IN)

p4.value(0)
p5.value(0)
p6.value(0)
p7.value(0)

def command_relay(num):
    num.value(1)
    time.sleep(1)
    num.value(0)

p1.value(1)
p2.value(1)
p3.value(1)


s = 0
while s < 20:
    time.sleep(1)
    s += 1
    if p1.value() == 0 and p2.value() == 1 and p3.value() == 1:
        #R1, p4
        command_relay(p4)
       
    elif p1.value() == 1 and p2.value() == 0 and p3.value() == 1:
        #R2, p5
        command_relay(p5)
    elif p1.value() == 1 and p2.value() == 1 and p3.value() == 0:
        #R3, p6
        command_relay(p6)
    elif p1.value() == 0 and p2.value() == 0 and p3.value() == 1:
        #R4, p7
        command_relay(p7)
    
        