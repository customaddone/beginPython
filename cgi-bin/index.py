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

num = [i for i in range(0, 10, 2)]
A = [2, 4, 5]
B = [2, 3]

for i in A:
    index = bisect_right(num, i)
    print(num[index - 1])

# numの中でのi未満の数字の最大値を求める
for i in A:
    index = bisect_left(num, i)
    print(num[index - 1])

# numの中でのiより大きい数字の最小値を求める
for i in B:
    index = bisect_right(num, i)
    print(num[index])

# numの中でのi以上の数字の最小値を求める
for i in B:
    index = bisect_left(num, i)
    print(num[index])

A = [1, 2, 4, 8, 16, 32]

def or_less(array, x):
    # arrayの中のx以下のものの個数
    # arrayの中のx以下のもののうちの最大値
    index = bisect_right(array, x)
    if index == 0:
        or_less_int = -float('inf')
    else:
        or_less_int = array[index - 1]
    return [index, or_less_int]

def less_than(array, x):
    # arrayの中のx未満のものの個数
    # arrayの中のx未満のもののうちの最大値
    index = bisect_left(array, x)
    if index == 0:
        less_than_int = -float('inf')
    else:
        less_than_int = array[index - 1]
    return [index, less_than_int]

print(or_less(A, 8))
print(less_than(A, 1))

def or_more(array, x):
    # arrayの中のx以上のものの個数
    # arrayの中のx以上のもののうちの最小値
    n = len(array)
    index = bisect_left(array, x)
    if index == n:
        or_more_int = float('inf')
    else:
        or_more_int = array[index]
    return [n - index, or_more_int]

def more_than(array, x):
    # arrayの中のxより大きいものの個数
    # arrayの中のxより大きいのもののうちの最小値
    n = len(array)
    index = bisect_right(array, x)
    if index == n:
        more_than_int = float('inf')
    else:
        more_than_int = array[index]
    return [n - index, more_than_int]

print(or_more(A, 32))
print(more_than(A, 1))

# ABC122 D - We Like AGC
X, Y, Z, K = getNM()
A = sorted([-i for i in getList()])
B = sorted([-i for i in getList()])
C = sorted([-i for i in getList()])

pos = []
heapify(pos)
dict = defaultdict(int)
u = (A[0] + B[0] + C[0], 0, 0, 0)
heappush(pos, u)
dict[u] = 1

for i in range(K):
    p, i, j, l = heappop(pos)
    print(-p)
    # 取り出すごとにA, B, Cについての次の値をpush
    if i + 1 < X:
        opt_a = (A[i + 1] + B[j] + C[l], i + 1, j, l)
        if dict[opt_a] == 0:
            heappush(pos, opt_a)
            dict[opt_a] = 1
    if j + 1 < Y:
        opt_b = (A[i] + B[j + 1] + C[l], i, j + 1, l)
        if dict[opt_b] == 0:
            heappush(pos, opt_b)
            dict[opt_b] = 1
    if l + 1 < Z:
        opt_c = (A[i] + B[j] + C[l + 1], i, j, l + 1)
        if dict[opt_c] == 0:
            heappush(pos, opt_c)
            dict[opt_c] = 1

# ABC149 E - Handshake
N, K = 9, 14
A = [1, 3, 5, 110, 24, 21, 34, 5, 3]

A.sort(reverse = True)

# 各ペアを大きい順に並べるのはムリ
# ただし、合計がx以上/以下になるペアが何個あるかは求められる
# x以上になるペアが何個あるか
def cnt(x):
    r = 0
    ans = 0
    list_num = [0] * N
    for i in range(N - 1, -1, -1):
        while r < N and A[r] + A[i] >= x:
            r += 1
        list_num[i] = r
        ans += r

    return [ans, list_num]

ng = 0
ok = 2 * (10 ** 6)

while ok - ng > 1:
    mid = (ok + ng) // 2
    if cnt(mid)[0] <= K:
        ok = mid
    else:
        ng = mid

# 境界がわかったら
imos = [0] + copy.deepcopy(A)
for i in range(N):
    imos[i + 1] += imos[i]

ans = 0
plus = cnt(ok)[1]

# cntから得た情報を元に上から順番に足していく
for i in range(N):
    ans += (A[i] * plus[i]) + imos[plus[i]]
# 合計がngになるペアを足りない分K - sum(plus)個足す
ans += ng * (K - sum(plus))
print(ans)

# ABC155 D - Pairs
N, K = 10, 40
A = [5, 4, 3, 2, -1, 0, 0, 0, 0, 0]
minus = [-x for x in A if x < 0]
plus = [x for x in A if x >= 0]

minus.sort()
plus.sort()

def cnt(x):
    ans = 0
    if x < 0:
        x = -x
        r = 0
        # - * +
        for num in minus[::-1]:
            while r < len(plus) and plus[r] * num < x:
                r += 1
            ans += len(plus) - r
        return ans

    r = 0
    for num in minus[::-1]:
        if num * num <= x:
            ans -= 1
        while r < len(minus) and minus[r] * num <= x:
            r += 1
        ans += r
    r = 0
    for num in plus[::-1]:
        if num * num <= x:
            ans -= 1
        while r < len(plus) and plus[r] * num <= x:
            r += 1
        ans += r
    ans //= 2
    # -になるものはまとめて計算
    ans += len(minus) * len(plus)
    return ans

bottom = 0
top = 2 * (10 ** 18) + 2


while top - bottom > 1:
    mid = (top + bottom) // 2
    if cnt(mid - 10 ** 18 - 1) < K:
        bottom = mid
    else:
        top = mid

print(int(top - 10 ** 18 - 1))

# ARC037 C - 億マス計算
N, K = getNM()
A = sorted(getList())
B = sorted(getList())

# かけ合わせるとx以下になるものが何個あるか
def cnt(x):
    r = 0
    ans = 0
    list_num = [0] * N
    # BiについてAの各要素とペアになれるのがいくつあるか
    for i in range(N - 1, -1, -1):
        while r < N and A[r] * B[i] <= x:
            r += 1
        list_num[i] = r
        ans += r

    return [ans, list_num]

ng = 0
ok = 2 * (10 ** 18)

while ok - ng > 1:
    mid = (ok + ng) // 2
    if cnt(mid)[0] >= K:
        ok = mid
    else:
        ng = mid

print(ok)

# ABC107 D - Median of Medians

"""
ソートしても問題はない
連続部分列はN(N + 1)//2個ある
ヒープキューによるN^2解は思いつく
端っこがlのものについてO(logN)ぐらいで求められないか
BITを立てていこうか A[i]が中央値になるか
左右にどれだけ広がればいいか
左右に広げた時にちょうど濃度が1/2になればいい
結局累積が必要になる？

中央値の列挙は必要ない　二分探索？
前から数えてN(N + 1)//4 + 1個目は何だろう

全部列挙するとN(N + 1) // 2個ある
列挙できたとしてもその中の中央値は求められない
二分探索で求める？
結局のところ濃度を考える
平均値がx以下である連続区間の個数は
"""

N = getN()
A = getList()

# 一回あたり計算量はO(NlogN)
def f(x):
    imos = [0] * (N + 1) # 1-index
    for i in range(N):
        if A[i] <= x:
            imos[i + 1] = 1
        imos[i + 1] += imos[i]

    # 前から濃度を計算する
    # x以下の値の個数 - xより大きい値の個数
    # 0でeven
    for i in range(N + 1):
        under, upper = imos[i], i - imos[i]
        imos[i] = [under - upper, i + 1] # 2-indexに

    # imos[j] - imos[i] > 0になるi, jを選ぶ
    # 小さい順に置いていって左のものの個数を数えればいい
    imos.sort(reverse = True)
    bit = BIT(N + 2) # 2-index

    res = 0
    while imos:
        now = imos[-1][0]
        opt = []
        while imos and imos[-1][0] <= now:
            _, index = imos.pop()
            opt.append(index)
            # 左にあるものの個数を数える
            res += bit.get(index)
        while opt:
            bit.add(opt.pop(), 1)

    return res

# N(N + 1) // 2個あるけど、その半分 (N(N + 1) // 2) // 2以下の個数になるように
lim = (N * (N + 1) // 2) // 2
alt = [0] + sorted(A)

# NlogmaxAlogNだと間に合わない
# NloglogNでやる
index = 0
for i in range(32, -1, -1):
    opt = index + 2 ** i
    if opt < N + 1 and f(alt[opt]) <= lim:
        index += 2 ** i

print(alt[index + 1])
