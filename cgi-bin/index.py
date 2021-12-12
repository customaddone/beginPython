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
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# F - Knapsack for All Segments
"""
11111 P = 20 の場合
11111 - 11 = 11100
実際には111は20で割れないけど、
[0, 1, 11, 11, 11, 11]
11111を20で割った余りが11
11を20で割った余りが11
11100 = 111 * 100
111は20で割れないけど、100が20で割れるので11100の余りが0になる
100と20の効果を打ち消したい
1[0000] * pw[4]
1[000] * pw[3]
1[00] * pw[2]
1[0] * pw[1]
1 * pw[0]
1 * pw[4 - 2]
1 * pw[3 - 2]
1 * pw[2 - 2] の計算
Pは素数 2とか5の場合もある
それだけ場合分け
4 2
1111 の時　答えは0
右端が偶数かどうか
4 5
1111 の時　答えは0
右端が0か5か
"""

N, P = getNM()
C = input()[::-1]

if P == 2:
    ans = 0
    for i in range(N):
        if int(C[i]) % 2 == 0:
            ans += N - i
    print(ans)

elif P == 5:
    ans = 0
    for i in range(N):
        if int(C[i]) == 0 or int(C[i]) == 5:
            ans += N - i
    print(ans)

else:
    mod = [0]
    pw = 1 # 10 ** iをPで割った時の余り
    for c in C:
        mod.append((int(c) * pw + mod[-1]) % P)
        pw = pw * 10 % P # 10 ** iをPで割った時の余りから10 ** (i + 1)をPで割った時の余りを求める

    print(sum(v * (v - 1) // 2 for v in Counter(mod).values()))

# codeforces div716 Product 1 Modulo N

"""
1, 2, 3, 4 delete some integers to meet the condition
product modulo 1?
can I delete few elements?
find large and small relationship?
n - 1, n - 2...
remove the divizor numbers
pro = mn + 1 this and n is coprime
"""

N = getN()
# 1 ~ N - 1の中のNと互いに素になる要素の全ての積の mod N は N - 1になる
l = [1] + [i for i in range(2, N) if math.gcd(i, N) == 1]
p = 1
for o in l:
    p *= o
    p %= N

if p == 1:
    print(len(l))
    print(*l)
else:
    ans = [i for i in l if p != i]
    print(len(ans))
    print(*ans)

# ABC228 E Integer Sequence Fair

"""
数え上げ
全ての通りはK^N通りあるが
M^(K^N) を求める？

K^Nはmodしてはいけない
だけど圧縮したい
Mを?回かけるとまた1に戻るような数は？
M^(mod - 1) = 1 (mod p)
つまりMをmod - 1回かけると1になる
つまりmod - 1を新しいmodにしてKを累乗する
"""

N, K, M = getNM()
if M % MOD == 0:
    print(0)
    exit()
t = pow(K, N, MOD - 1)
print(pow(M, t, MOD))
