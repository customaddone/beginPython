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
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

# 参考
# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

# https://atcoder.jp/contests/abc157/tasks/abc157_d
N, M, K = getNM()

# グループ分けをして解いていく
U = UnionFind(N)

friendlist = [getList() for i in range(M)]
blockedlist = [getList() for i in range(K)]
# friendlist内のa, bを繋いでいく
for a, b in friendlist:
    U.union(a - 1, b - 1)

friends = [0] * (N + 1)
blocks = [0] * (N + 1)

# 「同じグループ内に」友達、ブロックが何人いるか
for a, b in friendlist:
    if U.same(a - 1, b - 1):
        friends[a - 1] += 1
        friends[b - 1] += 1
for a, b in blockedlist:
    if U.same(a - 1, b - 1):
        blocks[a - 1] += 1
        blocks[b - 1] += 1

ans = []
for i in range(N):
    # U.size: グループの大きさ
    cnt = U.size(i) - friends[i] - blocks[i] - 1
    ans.append(cnt)
print(*ans)
