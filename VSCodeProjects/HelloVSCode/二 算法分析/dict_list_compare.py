import timeit
import random

print("Number list_time dict_time")

for i in range (10000,100001,10000):
    time = timeit.Timer("random.randrange(%d) in x" %i, "from __main__ import random, x")
    x = list(range(i))
    list_time = time.timeit(number=1000)
    x = {j:None for j in range(i)}
    dict_time = time.timeit(number=1000)
    print("%d %f %f" % (i, list_time, dict_time))