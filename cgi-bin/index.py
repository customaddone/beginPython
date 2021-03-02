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

# 二分探索木
# binary search tree
class BST:
    # arrayでどんな値が来るか読み込ませる
    # arrayはソートした配列をいれてね
    def __init__(self, N, array):
        self.N = N
        self.bit = [0] * (N + 1)
        self.comp = {} # value → index
        self.rev = {} # index → value
        for i, a in enumerate(array):
            self.comp[a] = i + 1
            self.rev[i + 1] = a
        self.b = 1 << N.bit_length() - 1

    # 追加 1-indexで収納される
    def add(self, a):
        x = self.comp[a]
        while(x <= self.N):
            self.bit[x] += 1
            x += x & -x

    # 削除
    def erase(self, a):
        x = self.comp[a]
        while(x <= self.N):
            self.bit[x] += -1
            x += x & -x

    def lowerbound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

    # x番目の値を返す
    def query(self, x):
        ind = self.lowerbound(x)
        return self.rev[ind]

# 使い方
Q = getN()
# ①まずクエリ先読みで使用する値をBSTに読み込ませる
read = []
que = []
for i in range(Q):
    t, x = getNM()
    if t == 1:
        read.append(x)
    que.append([t, x])
bit = BST(len(read), sorted(read))

for t, x in que:
    if t == 1:
        # ②addで値を1つ追加、eraseで消去
        bit.add(x)
    else:
        # ③queryで小さい方からx番目の値を返す
        res = bit.query(x)
        print(res)
        bit.erase(res)
