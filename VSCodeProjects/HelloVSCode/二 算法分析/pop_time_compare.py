#from timeit import Timer
import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))

print("popzero %f seconds \n" % popzero.timeit(number=1000))

x = list(range(2000000))

print("popend %f seconds \n" % popend.timeit(number=1000))

'''for i in range(100000,1000001,100000):
    x = list(range(i))
    print("popzero %f seconds" % popzero.timeit(number=1000))
    x = list(range(i))
    print("popend %f seconds" % popend.timeit(number=1000))'''

print("length   pop(0)   pop()")
for i in range(100000,1000001,100000):
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    x = list(range(i))
    pe = popend.timeit(number=1000)
    print("%d %f %f" % (i, pz, pe))
