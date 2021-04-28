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
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# PAST6 # M-等しい数

N = getN()
A = getList()
Q = getN()
q = []
c = set(A)
for _ in range(Q):
    l, r, x = getNM()
    c.add(x)
    q.append([l, r, x])

cnt = defaultdict(int)
color = [0] * (N + 2)
bit = BIT(N) # 1 ~ N + 1まで対応

for i in range(N):
    cnt[A[i]] += 1
    if i == 0 or A[i] != A[i - 1]:
        bit.add(i + 1, 1) # 1-index
        color[i + 1] = A[i]

ans = 0
for k, v in cnt.items():
    ans += v * (v - 1) // 2

for l, r, x in q:
    # 色の位置を特定していく
    ball = bit.get(l + 1)
    now = bit.lowerbound(ball)
    # 色の左端を収集する
    opt = [now]
    while now <= r:
        ball += 1
        now = bit.lowerbound(ball)
        opt.append(now)

    # 色を消す
    act = defaultdict(int) # 集計用
    for i in range(len(opt) - 1):
        act[color[opt[i]]] -= min(r + 1, opt[i + 1]) - max(l, opt[i])
        if l <= opt[i] <= r:
            bit.add(opt[i], -1)
    # 新しく色をつける
    act[x] += r - l + 1

    # 集計 前のと今のとを見比べる
    for k, v in act.items():
        prev = cnt[k]
        next = prev + v
        ans += (next * (next - 1) // 2) - (prev * (prev - 1) // 2)
        cnt[k] = next

    # 色をつける r + 1側 → l側
    if opt[-1] != r + 1: # r + 1に色の始点がなければ
        bit.add(r + 1, 1)
        # 元のopt[-2]の色がr + 1の色になる
        color[r + 1] = color[opt[-2]]
    # bit.lowerbound(bit.get(l)): lより左側にある一番近い色の左端
    if color[bit.lowerbound(bit.get(l))] != x:
        bit.add(l, 1)
        color[l] = x

    print(ans)
