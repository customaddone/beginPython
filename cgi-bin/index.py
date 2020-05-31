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
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

prime = [2]
max = 10 ** 5
limit = int(math.sqrt(max))
data = [i + 1 for i in range(2, max, 2)]

# エラストテネスの篩
while limit > data[0]:
    prime.append(data[0])
    data = [j for j in data if j % data[0] != 0]
prime = prime + data

print(prime)
