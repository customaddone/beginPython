def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

N = getN()
nums = getList()
nums.sort()
checker = nums[0]
count = 1
for i in range(1,N):
    if(checker != nums[i]):
        count += 1
        checker = nums[i]
# 効率的にやっていけばダブった数字だけを-2ずつしていける
if (N - count) % 2 == 0:
    print(count)
# もしダブった数字の個数が奇数なら
else:
    print(count - 1)
