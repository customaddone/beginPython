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

n = int(input())
s = input()
cnt = 0

for i in range(1000):
    flag = 0

    for st in s:
        # 条件を書き込む
        if flag == 0 and st == str(i // 100):
            flag = 1
        elif flag == 1 and st == str((i % 100) // 10):
            flag = 2
        elif flag == 2 and st == str(i % 10):
            flag = 3
            break
    if flag == 3:
        cnt += 1
print(cnt)
