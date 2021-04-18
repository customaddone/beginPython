from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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
連続部分列はN(N + 1)//2個ある
ヒープキューによるN^2解は思いつく
端っこがlのものについてO(logN)ぐらいで求められないか
BITを立てていこうか A[i]が中央値になるか
左右にどれだけ広がればいいか
左右に広げた時にちょうど濃度が1/2になればいい
結局累積が必要になる？

中央値の列挙は必要ない　と言うか無理　二分探索？
前から数えてN(N + 1)//4 + 1個目は何だろう

全部列挙するとN(N + 1) // 2個ある
列挙できたとしてもその中の中央値は求められない
二分探索で求める？
結局のところ濃度を考える
平均値がx以下である連続区間の個数は
"""

N = getN()
A = getList()

# 中央値がx以下になる連続部分列がいくつあるか
# x以下の要素を1, それ以外を0とすると
# [10, 30, 20], x = 20の場合[1, 0, 1]と表現できる
# 連続部分列[l, r]について1の濃度が過半数である場合、中央値がx以下になる
# [10]なら濃度は1, [10, 30, 20]なら濃度は2/3　これが> 1/2であればいい
# 0を-1に変えるとx以下のもの - xより大きいものの数が分かる
# 前から累積和で[10], [10, 30], [10, 30, 20]の濃度を求める
# [30, 20]の濃度 = [10, 30, 20]の濃度 - [10]の濃度
def f(x):
    # 累積　x以下のもの - xより大きいもの 長さN + 1
    I = [0] + [1 if A[i] <= x else -1 for i in range(N)]
    for i in range(1, N + 1):
        I[i] += I[i - 1]
    I = [[I[i], i + 1] for i in range(N + 1)]
    I.sort(key = lambda i:i[0], reverse = True) # lambdaでi[0]を指定する

    # I(x以下のもの - xより大きいもの)の値が小さいものから
    # 同じであればindexが右のものから探索する
    res = 0
    bit = BIT(N + 1)
    while I:
        _, ind = I.pop()
        res += bit.get(ind)
        bit.add(ind, 1)

    return res

code = [0] + sorted(A) + [float('inf')] # 長さN + 2
ok = -1
ng = N + 2
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(code[mid]) <= (N * (N + 1) // 2) // 2:
        ok = mid
    else:
        ng = mid

print(code[ok + 1])

# AOJ LthKthNumber

"""
N = 4, K = 3, L = 2
[4, 3, 1, 2]
K = 3を満たすのは
[4, 3, 1], [4, 3, 1, 2], [3, 1, 2]
それぞれについて小さい方からK番目の数字を取り出す
それのL番目の数字
連続部分列はN^2//2あるので全部書き出すのは無理
K番目に小さな文字がx以下であるもの　
[4, 3, 1]については4以下の数字を並べるとk番目に小さい数字は4になる
K番目の数字を取り出せるか
3以下の数字のみをupすると
[ , 3, 1]は取り出せない
[ , 3, 1, 2]は取り出せる
[3, 1, 2]は取り出せる
これの合計がLを超えるか
連続部分列について右端がrのもので何個取り出せるかをlogNでできるか
[]できない
[2]できない
[ , 1, 2]できない
[ , 3, 1, 2]できる　現れる数字の累積がK個以上な点を抑える
尺取りでいけそうな気が
累積がKより大きくなるまでlを右に進める
"""

N, K, L = getNM()
A = getList()

def f(x):
    I = [0] + [1 if A[i] <= x else 0 for i in range(N)]
    for i in range(1, N + 1):
        I[i] += I[i - 1]
    res = 0
    # 尺取り
    l = 0
    for r in range(1, N + 1):
        while l < N + 1 and I[r] - I[l] >= K:
            l += 1
        if r - l + 1 >= K:
            res += l

    # x以下のK番目の数字をres個取れる
    return res

code = [0] + sorted(A) + [float('inf')] # 長さN + 2
ok = -1
ng = N + 2
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(code[mid]) < L:
        ok = mid
    else:
        ng = mid

print(code[ok + 1])
