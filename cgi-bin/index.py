from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
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

# AGC019 B - Reverse and Compare

"""
何通りあるか　comboかdp
nC2を選んで i == jは意味ない
1 2 aatt
1 3 taat
1 4 ttaa
2 3 atat
2 4 atta
3 4 aatt
無駄な動きはない？
全通り選んでダブったのを引くか、前からdpか、comboか

ataaの場合
2 3 aata
1 4 aata 同じ
a, s1, s2...sn, aの場合
a ~ aとs1 ~ s2は同じ
ペアが１つあれば１つダブりが生まれる
文字が同じ場所を探す
abracadabraの場合
2 10 と 1 11は同じだし、
2 3 と 1 4も同じ
"""

A = input()
N = len(A)
l = [0] * 26

for i in range(N):
    l[ord(A[i]) - ord('a')] += 1

ans = (N * (N - 1) // 2) + 1
for i in range(26):
    ans -= l[i] * (l[i] - 1) // 2
print(ans)


# 第5回PAST J
"""
a:a
b:ab
2:ababab
c:abababc
1:abababcabababc
文字列はまとめる
指数関数的に増える
ハンバーガーと同じか？
2, 6, 7, 14 全体の長さがわかる

a
aaaaaaaaaa
aaaaaaaaaa + aaaaaaaaaaを9回
10 ** 15超えた時点でストップ
[ab] * 1
[ab] * 3
ab * 3, c * 1
ab * 3, c * 1, ab * 3, c * 1
14 // 2 = 7

7で引けるだけ引く
X = 6なら
X = 8なら

[1, 2, 6, 7, 14]
0になったら最初に出てくる文字

６文字目まで出力した
"""

S = input()
N = len(S)
X = getN() - 1

C = [0] * (N + 1)
p = 0

for i in range(N):
    if S[i] <= '9':
        C[i + 1] = C[i] * (int(S[i]) + 1)
    else:
        C[i + 1] = C[i] + 1
    if C[i + 1] > X:
        p = i
        break

for i in range(p, -1, -1):
    if S[i] <= '9':
        X %= C[i]
    else:
        if X == C[i]:
            print(S[i])
            break

# ARC081E Don't Be a Subsequence

"""
まず最短で何文字か
部分文字列（連続しなくていい）
後ろから順番にdpしていっては

全種類入ってればアウト
i番目以降の種類数を数える
atcoderregularcontest
最初の地点から飛ぶ
[[1, 13], [], [3, 15], [5], [6, 9, 19]...]
aについて見ると1に飛べる
bについて見ると飛ぶとこはない　答えはb
末尾sのものでdp取れるが
最小で何文字かはわかる
次に辞書順最小を求める
aから飛んでみる　カウントが減ってればOK

まず最短文字数を求める　そのあと辞書順最小のものを探す
"""

S = [-1] + ord_chr(list(input()), 0)
N = len(S)
l = [[] for i in range(26)]

for i in range(1, N):
    l[S[i]].append(i)

# スタート地点から最小で何文字飛ぶのか
dp = [0] * N
for i in range(N - 1, -1, -1):
    cnt = float('inf')
    for j in range(26):
        # 一番小さい回数で飛べるとこを探す
        index = bisect_right(l[j], i)
        if index == len(l[j]):
            cnt = 0
        else:
            cnt = min(cnt, dp[l[j][index]])
    dp[i] = cnt + 1

ans = ''
now = 0
cnt = dp[0]

# cnt文字復元
# 一番早い飛べるとこ（カウントが減るとこ）に飛ぶ
while cnt:
    for j in range(26):
        index = bisect_right(l[j], now)
        if index == len(l[j]): # ゴール
            ans += chr(j + ord('a'))
            cnt -= 1
            break
        if dp[l[j][index]] == cnt - 1:
            now = l[j][index]
            ans += chr(j + ord('a'))
            cnt -= 1
            break

print(ans)
