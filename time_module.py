import time

initial = time.time()
i = 0
while i < 1000000:
    i += 1
print(f"While loop ran in {time.time()-initial} seconds")
initial_2 = time.time()
for i in range(0, 1000000, 1):
    continue
print(f"For loop ran in {time.time()-initial_2} seconds")
local_time = time.asctime(time.localtime(time.time()))
print(local_time)
print(time.time())
time.sleep(2)
print(time.time())
