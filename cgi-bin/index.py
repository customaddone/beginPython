def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

from itertools import permutations
from math import factorial, hypot

odd = [i for i in range(0, 16, 3)]
limit = 33

lista = set()
for i in odd:
    for j in odd:
        lista.add(i + j)
lista = list(lista)

# ４つの数字を足し合わせた時に33以下になる数字
for i in lista:
    index = bisect_right(lista, limit - i)
    print(i, lista[index - 1])

# ４つの数字を足し合わせた時に33未満になる数字
for i in lista:
    index = bisect_left(lista, limit - i)
    print(i, lista[index - 1])
