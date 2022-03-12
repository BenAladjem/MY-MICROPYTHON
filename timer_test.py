

import time
#Засича се интервала от време между две натискания на ENTER

def time_convert(t):
    x = int(100 * round(t,2))
    tim = x // 100
    h = tim // 3600
    min = (tim % 3600) // 60
    sec = tim % 60
    milisec = x % 100
    print(h,':',min,':',sec,':',milisec)
input()
start = time.time()
input()
stop = time.time()
delta = stop - start
print(delta)
print(round(delta,2))
time_convert(delta)









