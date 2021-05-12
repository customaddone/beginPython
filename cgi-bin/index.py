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
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
大学N個
N人の生徒が1 ~ Nのどれかの大学にいる
チームのサイズを決める
サイズkより人数が少ないチームは参加できない
k人区切りでチームを送れる

合計人数のサイズはそんなに大きくない　各チームソートは可能
チームは送れる分だけ送った方がいい
トータルは単調減少するか？
各チーム上位何人まで送れるかは割り算すれば容易に数えられるが、
1クエリにつきO(N)かかる
なんとか√NかlogNにできないか
つまり各kについてlogNでできないか

天才数え上げか？
結局modがいくつあるか数える問題　つまり数学整数問題
modが0なら全員送れる　残ったmodが送れない人数
1 ~ Kについてmodを求める　調和級数行けるか

チームの人数nについて1~kで割った時の余りを求める
[4, 3, 0, 0, 0, 0, 0]みたいになる　N個全てをkで割っていくのは間に合わない
倍数ごとにkを計測していけば割る回数を減らせるかも　変わらない部分については何もしなくてok
大半のチームは人数が0なのがわかる kをあげて行くときに候補から除外していけば
"""

T = getN()
for _ in range(T):
    N = getN()
    t = [[] for i in range(N)]
    B = getList()
    S = getList()
    for b, s in zip(B, S):
        t[b - 1].append(s)
    for i in range(N):
        t[i].sort(reverse = True)
        for j in range(1, len(t[i])):
            t[i][j] += t[i][j - 1]

    q = deque([i for i in range(N)])
    ans = []
    for k in range(1, N + 1):
        cnt = 0
        for _ in range(len(q)):
            u = q.pop()
            n = len(t[u])
            if n // k > 0:
                cnt += t[u][(n // k) * k - 1]
                q.appendleft(u)
        ans.append(cnt)

    print(*ans)
