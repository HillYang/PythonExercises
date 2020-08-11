import time

def sumOfN3(n):
    startTime = time.time()
    theSum = n * (n+1) / 2
    endTime = time.time()
    return theSum, endTime - startTime

print("the sum is %d reuqired %10.10f seconds" % sumOfN3(10000))

print("the sum is %d reuqired %10.10f seconds" % sumOfN3(1000000))

print("the sum is %d reuqired %10.10f seconds" % sumOfN3(100000000))