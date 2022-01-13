
import time
import machine
import esp32



p14 = machine.Pin(14, machine.Pin.OUT)
p14.value(1)

#Увеличава  плавно честотата на импулсите в зададени граници на скоростта
# min speed = 2.4 km/h = 1 imp/s - value(0) = 1/3 sec = 333ms, value (1) = 2/3sec = 666ms
# max speed = 240km/h
# coefficient = 2.4 / speed

def impulse_generator(speed):
    coeff = 2.4/speed
    while true:
        one_imp(coeff)
        time.sleep(coeff / 60)

def one_imp(coefficient) #speed
    global p14
    p14.value(0)
    time.sleep(coefficient / 30)
    p14.value(1)
    #time.sleep(0.0666 * coefficient)




time_int = 240
speed = 1 # km/h
count = 0

step = 5
coefficient = 2.4 / speed
while speed <= 300:
    impulse_generator(speed)
    time.sleep(5)
    speed += step


