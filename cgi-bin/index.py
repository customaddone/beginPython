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
mod = 10 ** 9 + 7

N = getN()
rength = len(str(N))
numlist = [3, 5, 7]
cnt = 0

def sevfivthr(i, strint):
    global cnt
    if i == rength:
        return
    else:
        for num in numlist:
            newstr = strint + str(num)
            if ('3' in newstr) and ('5' in newstr) and ('7' in newstr):
                if int(newstr) <= N:
                    cnt += 1
            sevfivthr(i + 1, newstr)
for i in numlist:
    sevfivthr(1, str(i))
print(cnt)
