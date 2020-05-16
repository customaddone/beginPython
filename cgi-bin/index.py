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

# N個の県、M個の市
N, M = getNM()
city = []
# i県の中でn番目に→誕生が早い順に全ての都市を並べる
# →i県の市が来た時だけpref[i] += 1する　
# i県の中での順位が効率よく求められる
pref = [1] * (N + 1)
for i in range(M):
    # 市iについて
    # p県に属し、y年生まれ
    p, y = getNM()
    # 入力した順番についてのインデックス(i)を通っておく
    city.append([i + 1, p, y])
# 誕生が早い順に全ての都市を並べる
city = sorted(city, key=lambda i: i[2])

ans = []
for i, p, y in city:
    np = len(str(p))
    uppercode = '0' * (6 - np) + str(p)

    # p県のうちで何番目か
    order = pref[p]
    yp = len(str(order))
    undercode = '0' * (6 - yp) + str(order)
    # 次に来るp県の都市はpref[i] + 1番目に早く生まれた
    pref[p] += 1
    ans.append([i, uppercode + undercode])

ans = sorted(ans, key=lambda i: i[0])
for i in ans:
    print(i[1])
