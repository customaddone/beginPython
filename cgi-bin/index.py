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
sys.setrecursionlimit(300000)

#############
# Main Code #
#############

"""
何文字現れるか
dfsするか
数字-文字列の場合　compound
木を作成してみる
2(2u2lt4d)3(rb)pa =
2 * (2u2lt4d) + 3 * (rb) + p + a
括弧の中が子要素
S <= 1000 なので
直接の親要素はどれだろう
"""

S = input()
N = len(S)
l = []
ran = [[-1, N, 1]]
i_st = ''

for i in range(N):
    if S[i] in '0123456789':
        i_st += S[i]
    else:
        if len(i_st):
            val = int(i_st)
        else:
            val = 1
        i_st = ''
        if S[i] == '(':
            l.append([i, val])
        elif S[i] == ')':
            sta, val = l.pop()
            ran.append([sta, i, val])
        else:
            ran.append([i, i, val])

ran.sort()
n = len(ran)
parent = [-1] * n
for i in range(n):
    par = -1
    leg = float('inf')
    for j in range(n):
        if ran[j][0] < ran[i][0] <= ran[i][1] < ran[j][1] and ran[j][1] - ran[j][0] < leg:
            par = j
            leg = ran[j][1] - ran[j][0]
    parent[i] = par

E = [[] for i in range(n)]
for i in range(1, n):
    E[parent[i]].append(i)

def dfs(u):
    table = [0] * 26
    # 文字一つ
    if ran[u][0] == ran[u][1]:
        table[ord(S[ran[u][0]]) - ord('a')] += 1
        return table

    for v in E[u]:
        ene = dfs(v)
        for i in range(26):
            table[i] += ene[i] * ran[v][2]

    return table

ans = dfs(0)
for i in range(26):
    print(chr(i + ord('a')), ans[i])
