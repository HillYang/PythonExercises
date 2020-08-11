import time

def sumOfN(n):
    startTime = time.time()
    theSum = 0
    for i in range(1, n+1 ):
        theSum = theSum + i
    endTime = time.time()
    return theSum, endTime - startTime

print(time.time())
print(sumOfN(10))

for i in range(5):
    print("sum is %d required %10.5f seconds" % sumOfN(10000))

for i in range(5):
    print("sum is %d required %10.3f seconds" % sumOfN(1000000))