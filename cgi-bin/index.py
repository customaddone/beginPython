from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

n = 7
r = 4

# n個の数字をr個に分割する方法
# nCr通り出ます
def comb_pow(i, array, n, r):
    global cnt
    if i == r:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = -1
    if len(array) > 0:
        last = array[-1]

    for j in range(last, n):
        new_array = array + [j]
        comb_pow(i + 1, new_array, n, r)

comb_pow(0, [], n, r)
