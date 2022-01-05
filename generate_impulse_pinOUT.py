import machine
import esp32
import time

p4 = machine.Pin(4, machine.Pin.OUT)
p14 = machine.Pin(14, machine.Pin.OUT)
p4.value(1)
p14.value(1)


def pin_4():
    global p4
    p4.value(0)
    time.sleep(0.01)
    p4.value(1)
    # time.sleep(0.3)


def pin_14():
    global p14
    p14.value(0)
    time.sleep(0.01)
    p14.value(1)
    # time.sleep(0.3)