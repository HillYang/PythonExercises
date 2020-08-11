from timeit import Timer

def test_concat():
    l = []
    for i in range(1000):
        l = l + [i]


def test_append():
    l = []
    for i in range(1000):
        l.append(i)

def test_compre():
    l = [i for i in range(1000)]

def test_range():
    l = list(range(1000))

t1 = Timer("test_concat()", "from __main__ import test_concat")
print("concat %f seconds \n" % t1.timeit(number= 1000))

t2 = Timer("test_append()", "from __main__ import test_append")
print("append %f seconds \n" % t2.timeit(number= 1000))

t3 = Timer("test_compre()", "from __main__ import test_compre")
print("comprehension %f seconds \n" % t3.timeit(number= 1000))

t4 = Timer("test_range()", "from __main__ import test_range")
print("range %f seconds \n" % t4.timeit(number= 1000))
