from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# AGC055

"""
順列の通りの求め方は集合の取り方 * factorial

高橋くんがとるみかんの集合を固定するとすると
青木くんがとるみかんはどこに挟まれるか

青木くんがとるみかんが高橋くんのとるみかんをoverallしてると次高橋くんがとる
1つ目は高橋くんが、2つ目は青木くんがとることになるのだが、高橋くんがとるもの、青木くんがとるものが固定
されていたら後の順番が全て固定される

x1,x2,x3...とy1,y2,y2...が決定され、x1,y1が固定されていたら
残りのxとyが挟み込まれる場所は一意に決まる
"""
