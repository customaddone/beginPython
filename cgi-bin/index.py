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
import copy
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

N, M = getNM()
A = getList()
A.sort()

lista = []
for i in range(M):
    b, c = getNM()
    lista.append([b, c])
lista.sort(reverse = True,key = lambda i:i[1])

listalta = [0]
for i in range(M):
    listalta.append(listalta[i] + lista[i][0])
listalta.pop(0)

for i in range(N):
    index = bisect_left(listalta, i + 1)
    # index >= M(indexが枠外に飛んでないか)
    if index != M and A[i] < lista[index][1]:
        A[i] = lista[index][1]
print(sum(A))
