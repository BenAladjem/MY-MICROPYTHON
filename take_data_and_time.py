import time

seconds = time.time()
print(seconds)
local_time = time.ctime(time.time())
print(local_time)
time.sleep(5)
print(time.ctime(time.time()))

