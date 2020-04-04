import time
from decimal import Decimal
list = [i for i in range(20000)]
lista = [0]
maxnum = 0

t1 = time.time()
for i in range(400, 1000):
    num = sum(list[i:i + 4000])
    maxnum = max(maxnum, num)
print(maxnum)
t2 = time.time()
print(Decimal(t2 - t1))

t3 = time.time()
# これに時間かかるけど
for i in range(20000):
    lista.append(lista[i] + list[i])
# これがむちゃくちゃ速い
for i in range(400, 1000):
    num = lista[i + 4000] - lista[i]
    maxnum = max(maxnum, num)
print(maxnum)
t4 = time.time()
print(Decimal(t4 - t3))
