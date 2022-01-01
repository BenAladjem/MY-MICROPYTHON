import random
import time

#pin = machine.Pin(4, machine.Pin.OUT)
#pin.value(1)
def impulse_generator():
    global pin
    pin.value(0)
    time.sleep(0.01)
    pin.value(1)

def random_generator():
    return random.randrange(10,400)
def sec():
    return '!'

def imp():
    return '*'

period = 6000 #60sec * 10ms = 1 min
i = 1
imp_per_two_sec = 0

one_milisec = 0.00085 # 0.01 -> 0.0085 error rate
two_sec = 200 # times *
min_time = 9999999
max_time = 0
data = []
start = time.time()
avg_imp_count = 0
while period:
    if imp_per_two_sec % two_sec == 0:
        num = random_generator()
        data.append(num * 10)
        print()
    if min_time > num:
        min_time = num
    if max_time < num:
        max_time = num

    if i % num == 0:
        print(imp(), end='')
        i = 0

    else:
        pass
        #print(sec(), end='')
    time.sleep(one_milisec * 10)

    period -= 1
    i += 1
    imp_per_two_sec += 1
avg_imp_count = sum(data)/ len(data)
print()
end = time.time()
print(f'min interval {min_time * 10}ms')
print(f'max interval {max_time * 10}ms')
print(data)
print(f'average imp count = {avg_imp_count}')
print(f'{(end - start):.2f}sec')

