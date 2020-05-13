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

sx, sy, tx, ty = getNM()

path = ""
path_s = ""
for _ in range(tx - sx):
    path_s += "R"
for _ in range(ty - sy):
    path_s += "U"
path_e = ""
for _ in range(tx - sx):
    path_e += "L"
for _ in range(ty - sy):
    path_e += "D"

path = path_s + path_e + "DR" + path_s + "UL" + "UL" + path_e + "DR"
print(path)
