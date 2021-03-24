
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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# indeedなう　D - 高橋くんと数列
"""
その数を一つでも含む連続部分列を返す
各iにつきO(1)で
含まないものを引こう
"""

N, C = getNM()
A = getList()

# 数字A[i]の最後の場所
p = [-1] * (C + 1)
ans = [0] * (C + 1)

for i in range(N):
    # 片方で前回以降の分だけ、片方で最後まで
    # lを固定してrをl+1 ~ Nにすればダブらない
    # さらに前回の場所 + 1 ~ をlにもできる
    ans[A[i]] += (i - p[A[i]]) * (N - i)
    p[A[i]] = i

for i in ans[1:]:
    print(i)

# D - AtCoder Express 2
# bitの別解

"""
クエリソートしてみる

qを置いてみてその間の個数を調べてみる
右から探索する pの降順に
bitで求まる

pがある
lがp以上になるものについてそのrをbitに置く
bit.cum(p, q + 1)
"""

N, M, Q = getNM()
R = [getList() for i in range(M)]
que = []
for i in range(Q):
    p, q = getNM()
    que.append([p, q, i])
R.sort()
que.sort()
ans = [0] * Q

bit = BIT(N)

for p in range(N, 0, -1):
    while R and p <= R[-1][0]:
        l, r = R.pop()
        bit.add(r, 1)
    while que and p <= que[-1][0]:
        ql, qr, index = que.pop()
        ans[index] = bit.cum(ql, qr + 1)

for a in ans:
    print(a)

# ARC026 C - 蛍光灯

N, M = getNM()
seg = SegTree([float('inf')] * (M + 1), segfunc, ide_ele)
L = [getList() for i in range(N)]
L.sort()
seg.update(0, 0)

# [0, 1, 2, 3, 4, 5]
# seg.query(0, 2): [0, 1]の最小値
# seg.query(2, 2 + 1): [2]の最小値
# seg.update(2, min(vs, opt + c)): 2をmin(vs, opt + c)に更新
for l, r, c in L:
    opt = seg.query(l, r)
    vs = seg.query(r, r + 1)
    seg.update(r, min(vs, opt + c))
print(seg.query(M, M + 1))
