import time
b = 786
tim = b // 100
h = tim // 3600
min = (tim % 3600)//60
sec = tim % 60
milisec = b % 100
#print (tim)
#print('h=',h)
#print('min=',min)
#print('sec=',sec)
#print('ms=',milisec)
print(h,':',min,':',sec,':',milisec)

start = time.time()
while b >0:
    time.sleep(0.00845)
    b -= 1
stop = time.time()
result = stop - start
print('res',result)
