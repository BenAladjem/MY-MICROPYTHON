import esp32
import time
import machine

print('k')
p4 = machine.Pin(4, machine.Pin.IN)
p14 = machine.Pin(14, machine.Pin.OUT)
print (p4.value())
p4.value(1)
print(p4.value())
p14.value(0)
sec = 0
s = 0
while s < 10:
    time.sleep(1)
    s += 1
    if p4.value() == 1:
        while sec < 60:
            time.sleep(1)
            print(sec)
            sec += 1
            if p4.value() == 0:
                print('END')
                