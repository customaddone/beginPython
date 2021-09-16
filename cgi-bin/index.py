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
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# パ研合宿2020　第1日「SpeedRun」
# 同じgcdを持つ区間は結合しても同じまま

"""
K個に切り分ける
それぞれの部分の総和のgcdが大きいほどいい
最大公約数はいくつになるか
二分探索したいが dpもしたい

300C150とかは無理

K = 1から考える
答えはAの総和

A が最大300しかない
エッジを貼る
k回辺を移動して0 ~ Nにいけるか

調和級数
"""

N = getN()
A = [0] + getList()
su = sum(A)
for i in range(1, N + 1):
    A[i] += A[i - 1]

ans = [0] * (N + 1)
for i in range(su + 1, 0, -1):
    # これを通過すると必ず条件を満たす区間を作れる
    if su % i != 0:
        continue

    cnt = 0
    last = 0
    for j in range(1, N + 1):
        if (A[j] - A[last]) % i == 0:
            last = j
            cnt += 1

    # cnt以下の区間は結合することで簡単に作れる
    for a in range(cnt + 1):
        ans[a] = max(ans[a], i)

for a in ans[1:]:
    print(a)

# Chokudai SpeedRun 002 J - GCD β

"""
N <= 50000 これはなに？
NlogNまでならいける
最大公約数を最大にするには　同じ倍数でまとめればいい
ただしAiは大きい
どちらの数字を使うか
targetを選択するか
全部因数分解して候補を探る Aiがでかいので間に合わない
まずAi, Bi 10 ** 5個が候補としてある
1個下の奴とのgcdで結ぶ　エッジは高々20万本
AiスタートとBiスタートがある
残っているものとgcdする
Aiがでかいので...
A0, B0の約数しか候補にならない
"""

def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

N = getN()
A, B = [], []
for i in range(N):
    a, b = getNM()
    A.append(a)
    B.append(b)

ans = set()
opt_l = make_divisors(A[0]) + make_divisors(B[0])

for opt in opt_l:
    for i in range(N):
        if (A[i] % opt != 0) and (B[i] % opt != 0):
            break
    else:
        ans.add(opt)

ans = sorted(list(ans))
print(ans[-1])

# ABC136 Max GCD

"""
0回以上K回以下行う
Aの全ての要素を割り切る: 操作後をAの全てがansの倍数になる
二分探索したい　単調性はあるのか
K = 無限の時
8 20
0 28
-A 28 + A 結局最初のAの値に拘束される
0 28で28が最大か
K = 無限の場合の最大値はsum(A)
どれだけこれに近づけるか
sum(A)の倍数にしか到達できない　倍数の数は大体logN にぶたんしなくても十分早い
K回操作することでtargetの倍数に揃えられるか
4 5
10 1 2 22　の時
35に揃えられるか
-10, -1, -2, +13 無理
7に揃えられるか
-3, -1, -2, -1 total: -7, abs: 7
前からtotal // 7個を反転させる　反転させた場合現在のabsから7 - 2abs(Ai)増える
それぞれの要素についてプラスするかマイナスするか
プラスするものとマイナスするものはイーブンでないといけない
"""

N, K = getNM()
A = getList()
su = sum(A)

for p in make_divisors(su)[::-1]:
    ar = sorted([a % p for a in A], reverse = True)
    total = sum(ar) # total値は反転させるごとに7ずつ減っていく
    ab = total # abは反転させるごとにa * 2 - pずつ減る ならaの大きい順に反転させた方がお得

    for i in range(N):
        if total == 0:
            break
        total -= p
        ab -= ar[i] * 2 - p
    if ab <= K * 2:
        print(p)
        exit()

# codeforces round691
# C - Row GCD

# commmon divisor
# Ai + nのgcdについて　1 ~ Mまで
# 最悪セグ木でなんとか

# 求めるdがあったとすると　現在の時点でもmodが全て同じでないといけない
# 候補は各数字同士の差分のgcdの約数　因数ごとにやれば
# A[0] + B[i]とgのgcdを取ればいい

# A[0] + B[i]とgが共通してもつ因数をmとすると
# g = nmと表せる
# A[0] + B[i]よりknm大きいA[1] + B[i]も当然mを約数にもつ

N, M = getNM()
A = getList()
B = getList()

target = A[0]
if N > 1:
    A = [abs(A[i] - A[i - 1]) for i in range(N - 1)]
    g = A[0]
    for i in range(2, N - 1):
        g = math.gcd(g, A[i])
else:
    g = 0

print(*[math.gcd(target + B[i], g) for i in range(M)])

# edufo 89 D - Two Divisors
# 約数同士の足し算について

"""
2以上の数を2つ
約数の中から探そう
aiはギリギリエラストテネスはできる　全てについて約数列挙はできない
√N = 3000ぐらい
列挙する個数を減らすかそもそも約数列挙しないか
素数はやらなくていい 存在しない証明が難しいか
d1とd2は共通因数を持っていたらだめ　互いに素でないといけない
因数についてどちらかにだけ置く　
最大因数を足すか？

a1が偶数の場合は？ 偶数 + 奇数にしないと
2^k + 他の全ての因数の積 = 奇数になる　これは合成数か？
これは合成数になりうるが、奇数の因数はない！！
つまり逆にない条件を考える　素数
2^kがない or 他の全ての因数の積がない
他の全ての因数の積がない場合はどうあがいても偶数 + 偶数になるのでダメ
例えば105(3 * 5 * 7)について　3 + 5 = 2 * (3 + 5 の平均　これは偶数　これをさらに２で割ると3は下回る)
奇数の因数が２つあればいい
3200以下の素数の個数は452個　これを回せば

ない条件　2の累乗 or 奇数の因数が1種類しかない
他は2^k + 奇数の因数の積でok
結局のところ最小の因数 + それ以外の積　をすればいい
因数が２つあればいい
"""

# osa_k法
max = 10 ** 7 + 7
ar = [i for i in range(max)]
# 最大の約数を拾う
for i in range(2, max):
    if ar[i] == i:
        for j in range(i * i, max, i):
            ar[j] = i

N = getN()
A = getList()
ans1, ans2 = [], []

for a in A:
    z = ar[a]
    # zの累乗ではないか
    while a % z == 0:
        a //= z
    # 累乗だった
    if a == 1:
        ans1.append(-1)
        ans2.append(-1)
    # 因数が2種類以上あった
    else:
        ans1.append(z)
        ans2.append(a)

print(*ans1)
print(*ans2)
