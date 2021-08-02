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
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

N, K = 7, 6
S = [4, 3, 1, 1, 2, 10, 2]

# 左を伸ばしていく
# その部分列に含まれる全ての要素の値の積は「K以下」である。
# lはrをオーバーすることもある

if 0 in S:
    print(N)
    exit()
else:
    l, ans, total = 0, 0, 1
    for r in range(N):
        total *= S[r]
        while total > K and l <= r:
            total //= S[l]
            l += 1
        ans = max(ans, r - l + 1)
print(ans)

# (条件) 連続部分列に含まれる全ての要素の値の和は、「K以上」である。
N, K = 4, 10
A = [6, 1, 2, 7]

left = 0
total = 0
ans = 0

for right in range(0, N):
    total += A[right]
    while total >= K:
        ans += N - right
        total -= A[left]
        left += 1
print(ans)

N = 10
S = 15
A = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
right = 0
total = 0
ans = 0
# S以上を求める場合にはこの形で
for left in range(N):
    while right < N and total < S:
        total += A[right]
        right += 1
    if total < S:
        break
    if left == right:
        right += 1
    total -= A[left]

# 要素の種類についての問題
# 全ての要素を含む区間の最短は？
# [0, 2), [0, 3), [3, 5)
P = 5
A = [1, 8, 8, 8, 1]
dict = {}
for i in A:
    dict[i] = 0
# 要素の種類数
V = len(dict.items())

# 事象の数をカウント
cnt = 0
right = 0
# １つ目から全ての事象をカバーするまでrightを進める
while right < P:
    if dict[A[right]] == 0:
        cnt += 1
    dict[A[right]] += 1

    if cnt == len(dict.items()):
        break

    right += 1
    print(l, r)

l = 0
# 右を一つ進めて左をできる限り進める
for r in range(right + 1, P):
    # 新しく一つ加える
    dict[A[r]] += 1
    while True:
        # もし要素が一つしか無かったら削れない
        if dict[A[l]] == 1:
            break
        dict[A[l]] -= 1
        l += 1
    print(l, r)

# 各要素にダブりがない区間の最長
# [0, 2), [2, 5)...
N = 6
A = [1, 2, 2, 3, 4, 4]

dict = defaultdict(int)
l = 0
for r in range(N):
    while dict[A[r]] == 1:
        dict[A[l]] -= 1
        l += 1
    print(l, r)
    dict[A[r]] += 1

# K種類以内の要素のみを含んだ区間の最長は？
N, K = 10, 2
A = [1, 2, 3, 4, 4, 3, 2, 1, 2, 3]
d = {}

ans = 0
l = 0
for r in range(N):
    # rの要素を足す
    if A[r] in d:
        d[A[r]] += 1
    else:
        d[A[r]] = 1

    while len(d) > K:
        # 末尾をどんどん除いていく
        d[A[l]] -= 1
        if not d[A[l]]:
            del d[A[l]]
        l += 1

    ans = max(ans, r - l + 1)

print(ans)

# 要素をlim種類含む連続部分列を求める
N = 7
S = 'xxoooxx'

# 種類数の登録　すべての要素を含む連続部分列の最小について、に拡張
d = {}
for i in range(N):
    d[S[i]] = 0
lim = len(d) # すべての要素数 dの中にこの数だけ入っていればいい
#####################################################

lim = 2 # 要素数がlim個の連続部分列が欲しい
d = {}

l = 0
ans = 0
# rを1つずつ刻んでいく
for r in range(N):
    if S[r] in d:
        d[S[r]] += 1
    else:
        d[S[r]] = 1

    # lim種類未満であれば何もしない
    if len(d) < lim:
        continue

    # 現在lim種類以上あれば削る
    while len(d) > lim or d[S[l]] > 1:
        d[S[l]] -= 1
        if not d[S[l]]:
            del d[S[l]]
        l += 1

    ans += l + 1

print(ans)

N = 4
A = [2, 5, 4, 6]

l, ans, xo, total = 0, 0, 0, 0

for r in range(N):
    xo ^= A[r]
    total += A[r]

    # xo == totalになるまでA[l]で引き続ける
    while xo < total:
        xo ^= A[l]
        total -= A[l]
        l += 1

    ans += r - l + 1

print(ans)


N, K = 10, 4
A = [100, 300, 600, 700, 800, 400, 500, 800, 900, 900]

right, ans = 0, 0
for left in range(N):
    # 単調増加するとこまでもしくは長さKになるまで
    while right < N - 1 and A[right] < A[right + 1] and right - left < K - 1:
        right += 1
    # もし長さKまで伸ばせたらans += 1
    if right - left == K - 1:
        ans += 1
    # 前に進めないならright += 1
    if left == right and right < N:
        right += 1
print(ans)

# codeforces 736
# D. Integers Have Friends
# セグ木 + 尺取り

T = getN()
for _ in range(T):
    N = getN()
    psu = getList()
    A = [abs(psu[i] - psu[i + 1]) for i in range(N - 1)]
    seg = SegTree(A, segfunc, ide_ele)
    if N == 1:
        print(1)
        continue

    l, ans = 0, 0
    for r in range(N - 1):
        while seg.query(l, r + 1) == 1:
            l += 1
        ans = max(ans, r - l + 2)
    print(ans)
