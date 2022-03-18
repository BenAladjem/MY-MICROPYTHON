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
        
    p1.irq(handler=None)
    p2.irq(handler=None)
    p3.irq(handler=None)
    time.sleep(2)
    print("new")
    print(num)
    print("P1 ",p1.value())
    print("P2 ",p2.value())
    print("P3 ",p3.value())
    
    if p1.value() == 0 and p2.value == 1 and p3.value == 1:
        print('p1')
        p4.value(1)
        time.sleep(1)
        p4.value(0)
    elif p1.value() == 0 and p2.value == 1 and p3.value == 0:
        p5.value(1)
        time.sleep(1)
        p5.value(0)
    elif p1.value() == 1 and p2.value == 0 and p3.value == 0:
        p6.value(1)
        time.sleep(1)
        p6.value(0)
    elif p1.value() == 0 and p2.value == 0 and p3.value == 0:
        p7.value(1)
        time.sleep(1)
        p7.value(0)
    
    p1.irq(handler=command_relay, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
    p2.irq(handler=command_relay, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)
    p3.irq(handler=command_relay, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING)


#print(dir(Pin))
p1.irq(handler=command_relay, trigger= Pin.IRQ_FALLING | Pin.IRQ_RISING)
p2.irq(handler=command_relay, trigger= Pin.IRQ_FALLING | Pin.IRQ_RISING)
p3.irq(handler=command_relay, trigger= Pin.IRQ_FALLING | Pin.IRQ_RISING)