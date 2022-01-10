import machine
import esp32
import time
import random
import RTC
import network

p4 = machine.Pin(4, machine.Pin.OUT)
p14 = machine.Pin(14, machine.Pin.OUT)
p4.value(1)
p14.value(1)




def pin_4():
    global p4
    p4.value(0)
    time.sleep(0.05)
    p4.value(1)
    # time.sleep(0.3)


def pin_14():
    global p14
    p14.value(0)
    time.sleep(0.05)
    p14.value(1)
    # time.sleep(0.3)


def sec():
    return '!'


def imp_4():
    return '*'


def imp_14():
    return '$'


def counter_sec():
    return random.randrange(30)


def counter_imp():
    return random.randrange(4)


def count_odd():
    return random.randrange(20)


def emulator():
#    print(p)
#    p.irq(handler=None)
    start = time.time()
    count = 0
    num_sec = 0
    total_imp = 0
    times = 0
    period = 60 * 10
    imp_ten_min_4 = 0
    imp_ten_min_14 = 0
    data_imp_4 = []
    data_imp_14 = []
    while times < period:
        if count % 2 == 0:
            a = counter_sec()
            b = counter_sec()
            if a > period - times:
                a = period - times
            if b > period - times:
                b = period - times
        else:
            a = counter_imp()
        for i in range(a):
            times += 1
            if count % 2 == 0:
                print(sec(), end='')
                num_sec += 1
                slptime = 0.1
            else:
                if count_odd() % 2 == 0:
                    print(imp_4(), end='')
                    pin_4()
                    total_imp += 1
                    imp_ten_min_4 += 1
                else:
                    print(imp_14(), end='')
                    pin_14()
                    total_imp += 1
                    imp_ten_min_14 += 1
                slptime = 0.05
            if (total_imp + num_sec) % 100 == 0:
                data_imp_4.append(imp_ten_min_4)
                data_imp_14.append(imp_ten_min_14)
                imp_ten_min_4 = 0 
                imp_ten_min_14 = 0
                print()
            time.sleep(slptime)
        count += 1
    end = time.time()
    print("time = " , end-start)
    print('num sec = ', num_sec)
    print('num imp =', total_imp)
    print('IO_4', data_imp_4)
    a = sum([x for x in data_imp_4])
    print('sum imp 4 =', a)
    print('IO_14', data_imp_14)
    b = sum([x for x in data_imp_14])
    print('sum imp 14 =', b)

#emulator()

#io23 = machine.Pin(23,machine.Pin.IN)
#io23.irq(trigger= machine.Pin.IRQ_FALLING,handler = emulator)
