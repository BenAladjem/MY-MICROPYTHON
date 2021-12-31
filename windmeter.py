import random
import time

#Увеличава и намалява плавно честотата на импулсите в зададени граници

def impulse_generator():
    pass

def sec():
    return '!'

def imp():
    return '*'

period = 6000
i = 1
time_int = 200
interval = time_int
count = 0
flag = True
step = 10
while period:
    if interval >= time_int:
        flag = True

    if interval <= 1:
        interval = step
        flag = False
    if i % interval == 0:
        print(imp(), end='')
        print(count)
        count = 0
        i = 0
        if flag:
            interval -= step
        else:
            interval += step
    else:
        #print(' ', end='')
        #print(sec(), end='')
        count += 1
    time.sleep(0.01)
    period -= 1
    i += 1

