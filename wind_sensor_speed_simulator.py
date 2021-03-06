
import time
import machine
import esp32



p14 = machine.Pin(14, machine.Pin.OUT)
p14.value(1)

#Увеличава  плавно честотата на импулсите в зададени граници на скоростта
# min speed = 2.4 km/h = 1 imp/s - value(0) = 1/4 sec = 250ms, value (1) = 3/4sec = 750ms
# max speed = 240km/h
# coefficient = 2.4 / speed

def impulse_generator(speed):
    coeff = speed / 2.4
    dur = 1000 / coeff 
    i = 10000 / dur
    while i >= 0:
        one_imp(dur)
        time.sleep_ms(dur * 0.75)
        i -= 1

def one_imp(coefficient):
    print('*')
    global p14
    p14.value(0)
    time.sleep_ms(coefficient * 0.25)
    p14.value(1)
    #time.sleep(0.0750 * coefficient)




time_int = 240
speed = 5 # km/h
count = 0

step = 5
coefficient = 2.4 / speed
while speed <= 300:
    impulse_generator(speed)
    #time.sleep(5)
    speed += step


