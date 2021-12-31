import network
#import esp
from machine import RTC

rtc = RTC()

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

num_sec = 0
total_imp = 0
imp_ten_min_4 = 0
imp_ten_min_14 = 0
data_imp_4 = []
data_imp_14 = []

def emulator():
    program_working_time_in_min = 10 # задава се времето за цялата програма в минути
    collect_imp_period = 1  # задава се времето на колко минути да нулира временния брояч
    count = 0
    times = 0
    period = 600 * program_working_time_in_min # program_working_time_in_min = 10 = 10 min
    global num_sec
    global total_imp
    global imp_ten_min_4
    global imp_ten_min_14
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
                #print(sec(), end='')
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
            if (total_imp + num_sec) % (collect_imp_period * 600) == 0: # collect_imp_period = 1 = 1min
                data_imp_4.append(imp_ten_min_4)
                data_imp_14.append(imp_ten_min_14)
                imp_ten_min_4 = 0 
                imp_ten_min_14 = 0
                print()
            time.sleep(slptime)
        count += 1

#print(wlan.scan())
#print (rtc.datetime())
print(rtc.datetime()[6])

t = 60 - rtc.datetime()[6]
time.sleep(t)
emulator()


print('num sec = ', num_sec)
print('num imp =', total_imp)
print('IO_4', data_imp_4)
a = sum([x for x in data_imp_4])
print('sum imp 4 =', a)
print('IO_14', data_imp_14)
b = sum([x for x in data_imp_14])
print('sum imp 14 =', b)
    
    