# N**iの数が多くなりすぎる時は、listを思いっきり伸ばして二分探索すればOK
import bisect
import time
from decimal import Decimal

t1 = time.time()
a = [x for x in range(2000000)]

t1 = time.time()
b = a.index(888888)
t2 = time.time()
print(Decimal(t2 - t1))

t3 = time.time()
b = bisect.bisect_left(a, 888888)
t4 = time.time()
print(Decimal(t4 - t3))
