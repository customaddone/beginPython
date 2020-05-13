def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
S = input()

while len(S) >= 5:
    # Sを４つの単語で順に調べて刈っていく
    if len(S) >= 7 and S[-7:] == "dreamer":
        S = S[:-7]
        continue

    if len(S) >= 6 and S[-6:] == "eraser":
        S = S[:-6]
        continue

    elif S[-5:] == "dream" or S[-5:] == "erase":
        S = S[:-5]
        continue

    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")
