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

# ABC195 F. Coprime Present

"""
A以上B以下　幅は72以下
A, Bがでかい
連続する数　ここポイント
連続する数は互いに素

Q:どの数とどの数をペアにしてはいけないか
偶数は一緒にしてはいけない　偶数のどれか1つ or 全くない
奇数はどんな感じ
3の倍数の場合は6つ前、6つ後ろと一緒になってはいけない
5の倍数は10こ前、10こ後ろと一緒になってはいけない...
2の倍数が入る通り、3の倍数が入る通り...をdp
bit dpすれば
2 4
0b1 2は3の倍数
0b10 3は3の倍数
0b1 4は2の倍数
"""

A, B = getNM()
# 72までに素数が20個あります
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
N = [i for i in range(A, B + 1)]
L = len(N)

# 各数字をbit棒に変換する
for i in range(L):
    # なんの約数かをbit形式で記録
    opt = 0
    for j in range(20):
        if N[i] % prime[j] == 0:
            opt += (1 << j)
    N[i] = opt

prev = [0] * (1 << 20)
prev[0] = 1 # 空集合が1
for i in range(L):
    next = [0] * (1 << 20)
    # 配るdpで
    for bit in range(1 << 20):
        next[bit] += prev[bit] # 何も足さない場合
        if not bit & N[i]: # 共通の約数がなければ
            next[bit | N[i]] += prev[bit]
    prev = next

print(sum(prev))

# 典型90 042 - Multiple of 9（★4）
# 配るのは0から、累積するのは2から

K = getN()
if K % 9 != 0:
    print(0)
    exit()

dp = [0] * (K + 2)
dp[0] = 1
dp[1] = 1
for i in range(K + 1):
    if i > 1:
        dp[i] += dp[i - 1]
    dp[i] %= mod
    dp[i + 1] += dp[i]
    dp[min(i + 10, K + 1)] -= dp[i]

print(dp[-2])

# codeforces round667
# F. Subsequences of Length Two

# 耳dpの要領　tが文字数2なので
# t1, t2にそれぞれ何個振り分けるか
# 今までi個変換してこれより前にあるt1の個数がj個

N, K = getNM()
S = list(input())
T = input()
t1, t2 = T[0], T[1]
if t1 == t2:
    for i in range(N - 1, -1, -1):
        if K and S[i] != t1:
            S[i] = t1
            K -= 1
    ans = 0
    cnt = 0
    for i in range(N):
        if S[i] == t1:
            ans += cnt
            cnt += 1
    print(ans)
    exit()

# 今までi個変換してこれより前にあるt1の個数がj個の時の連続部分列の個数
prev = [[-float('inf')] * (N + 1) for i in range(K + 1)]
prev[0][0] = 0
for n in range(N):
    next = [[-float('inf')] * (N + 1) for i in range(K + 1)]
    # 現在までに変換している個数
    for i in range(K + 1):
        # ここより前にあるt1の個数
        for j in range(N):
            # 変換しない
            next[i][j] = max(next[i][j], prev[i][j])
            # その文字がt1だった
            if S[n] == t1:
                next[i][j + 1] = max(next[i][j + 1], prev[i][j])
            # その文字がt2だった
            if S[n] == t2:
                # これより前のt1の個数だけカウント数が増える
                next[i][j] = max(next[i][j], prev[i][j] + j)

            # 変換する
            if i < K:
                # t1に変換
                next[i + 1][j + 1] = max(next[i + 1][j + 1], prev[i][j])
                # t2に変換
                next[i + 1][j] = max(next[i + 1][j], prev[i][j] + j)

    prev = next

print(max(prev[-1]))

# edufo #1 E. Chocolate Bar

"""
O(NM)ぐらいで考えよう 50回やる
面積Kのチョコが欲しい　切り方

端っこを使うと？　N, Mのうち短い方を切るといい
kが小さい　最高50
縦 + 横、　縦 + 縦 + 横
cutして減らすのもある
"""

dp = [[[0 for k in range (51)] for j in range (31)] for i in range (31)]

def calc (n, m, k) :
    #print(n,m,k)
    if (dp[n][m][k] != 0) or (n*m == k) or (k == 0) :
        return dp[n][m][k]

    ans = 10**9

    for i in range (1,n//2 + 1) :
        for j in range (k+1) :
            #print(i,j,'a')
            if (i*m >= (k-j)) and ((n-i)*m >= j) :
                ans = min(ans, m*m + calc(i,m,k-j) + calc(n-i,m,j))

    for i in range (1,m//2 + 1) :
        for j in range (k+1) :
            #print(i,j,'b')
            if (i*n >= (k-j)) and ((m-i)*n >= j) :
                ans = min(ans, n*n + calc(n,i,k-j) + calc(n,m-i,j))

    dp[n][m][k] = ans

    return ans

for _ in range (getN()):
    N, M, K = getNM()

    print(calc(N, M, K))

# edufo73 D. Make The Fence Great Again
# 状態を減らす系dp
# 前と後ろしか関係ないのだから状態は3つずつでいい

"""
コスト1回で1伸ばせる　隣接するやつとの差をつけろ
O(N^2)のdpなら...
隣のやつが過度に伸ばされててもあんまり...
1伸ばすか、伸ばさないか
伸ばしても精々2伸ばすだけ
"""

T = getN()
for _ in range(T):
    N = getN()
    F = [getList() for i in range(N)]
    last = -1
    # 伸ばさない時と伸ばした時と
    prev = [0, inf, inf]

    for i in range(N):
        next = [inf, inf, inf]
        for j in range(3):
            for k in range(3):
                if last + j != F[i][0] + k:
                    next[k] = min(next[k], prev[j] + F[i][1] * k)

        prev = next
        last = F[i][0]

    print(min(prev))
