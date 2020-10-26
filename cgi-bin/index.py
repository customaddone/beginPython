def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# ARC126 F - XOR Matching
# d = 2 ** N - 1について
# 1 xor 2 xor... xor dは
# 各桁にフラグが2 * (N - 1)本ずつ立っている（つまり0になる）
# なのでXを抜くとXを構成する部分についてフラグが抜けてXができる

M, K = getNM()

if M == 0 and K == 0:
    print(0, 0)

elif M == 1 and K == 0:
    print(0, 0, 1, 1)

elif M >= 2 and K < 2 ** M:
    ans = []
    for n in range(2 ** M):
        if n != K:
            ans.append(n)
    print(*ans, K, *ans[::-1], K)

else:
    print(-1)

# B - Median Pyramid Easy

"""
頂点にXを書き込む
N段目の順列としてありうるものを示す
・一番都合のいいものを出す
・条件を緩和してみる
・条件が小さい場合を考える
Xがなければ
2 ** (N - 2)を頂点に書けばいい これ以外不可能ってことはない？
N = 4の場合
   4
  345
 23456
1234567
・実験
def cnt(array):
    alta = deepcopy(array)
    while len(alta) > 1:
        l = []
        for i in range(1, len(alta) - 1):
            l.append(sorted([alta[i - 1], alta[i], alta[i + 1]])[1])
        alta = l
    return alta[0]
A = [1, 2, 3, 4, 5]
for i in permutations(A):
    print(i, cnt(i))
X = 2, 3, 4なら可能
同様に N = 4なら 2 ~ 6であれば可能
X = 2の場合 最終的に上がってくるのは2, 2, 3
1, 2がペアで存在する場合はX = 2になる？
上にあげるには？
上げたい数を真ん中で二つ並べることができたら（例:6 4 2 2 3)勝ち確
真ん中に X + 2, X - 1, X, X + 1, X - 2を配置
これを中央の値と入れ替える
"""

def cnt(array):
    alta = deepcopy(array)
    while len(alta) > 1:
        l = []
        for i in range(1, len(alta) - 1):
            l.append(sorted([alta[i - 1], alta[i], alta[i + 1]])[1])
        alta = l
    return alta[0]

N, X = getNM()
ma = 2 * N
mid = ma // 2
if X == 1 or X == ma - 1:
    print('No')
    exit()
print('Yes')

list = [i for i in range(ma - 1, 0, -1)]
ans = [-1] * ma

if (ma - 1) - X > 1 and mid - 2 > 0: # X + 2を入れ替える
    ans[mid - 2] = list.pop(list.index(X + 2))
if X - 2 > 0 and (ma - 1) - mid > 1: # X - 2を入れ替える
    ans[mid + 2] = list.pop(list.index(X - 2))

ans[mid - 1] = list.pop(list.index(X - 1))
ans[mid + 1] = list.pop(list.index(X + 1))
ans[mid] = list.pop(list.index(X))

for i in range(1, ma):
    if ans[i] == -1:
        ans[i] = list.pop()

for i in ans[1:]:
    print(i)

# ARC013 E - Tr/ee

"""
頂点がN個、辺がN - 1本あります
1110
任意の辺を一つ取り除くとサイズ1の連結成分が作れる
任意の辺を一つ取り除くとサイズ2の連結成分が作れる
任意の辺を一つ取り除くとサイズ3の連結成分が作れる
どの辺を一つ取り除いてもサイズ4の連結成分は作れない
サイズ1の連結成分が作れること、サイズnの連結成分は作れないことは自明
サイズiの連結成分が作れるなら、サイズn - iの連結成分が作れる
単純な木構造から考えよう
・パスグラフ
・スターグラフ
・パスグラフ
1(1がN - 1個) + 0になる
・スターグラフ
10...010になる
他のものは作れないか
連結成分iのものが作れる条件、作れない条件
作れない条件が知りたい　単体であれば必ず作れる
（連結成分iが作れ、jが作れない）が成り立たない場合がある？
部分木から考えていく
大きさ2のパスグラフは11
これをrootにつけると 110になる
大きさ3のスターグラフは101
これをrootにつけると1010になる
大きさnのグラフにパス状に/スター状に繋げていくと
1 - 2のグラフに
パス状に3を繋げると 110
スター状に繋げると 110 ここまでは同じ
1 - 2 - 3のグラフに
パス状に繋げると 1110
スター状に繋げると 1010
パスグラフに辺を加えて連結成分jが作れないようにしよう
11010110は作れるか
一方をパスグラフに、一方をスターグラフにする?
1 - 2の状態でスタート
もしS[i] = 1なら親要素にi + 2をつけ、それを親要素にする
もしS[i] = 0なら現在の親要素につける
"""

S = input()
N = len(S)
# この条件を満たしていると木を作ることができる
if S[N - 1] == "1" or S[N - 2] == "0" or S[0] == "0":
    print(-1)
else:
    for i in range(N - 1):
        if S[i] != S[N - i - 2]:
            print(-1)
            exit()
    ans = []
    parent = 1 # 現在のparent
    for i in range(N - 1):
        if S[i] == "1":
            # パスグラフ状
            ans.append([parent, i + 2])
            parent = i + 2 # parent変更
        else:
            # スターグラフ状
            ans.append([parent, i + 2])
    for i in ans:
        print(i[0], i[1])

# ARC091 E - LISDL

"""
最長増加部分列の長さはA　
最長減少部分列の長さはB
使える数字は1 ~ N
一番都合のいいものを探す
構築問題は場合分けしてそれぞれの場合の最も都合がいいものをとる
A + B > N + 1ならダメっぽい
A + B = Nの場合
2 3 5 + 5 4
2 3 1 5 4
1を適当な所に置けば良い
A + B = N + 1の場合は簡単
N = 5
A, B = 3, 3
3 4 5 + 5 2 1
3 4 5 2 1
A + B < N の場合
いらないものを適当に置けば
いいのでは？
N = 5
A, B = 2, 2 は無理 A + B <= 4は無理
2 3 + 3 1 (4, 5はいらない)
2 3 1 + 4 5
(5, 6, 3, 1, 4, 2)
4 5 6 1 2 3
def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)
for i in permutations([1, 2, 3, 4, 5, 6, 7]):
    if lis(i) + lis(list(reversed(i))) <= 5:
        print(lis(i), lis(list(reversed(i))), i)
相方を2にした場合の下限は(N + 1) // 2 ?
5なら3 2
6なら3 2
7なら4 2
8なら4 2
3 4 5 + 5 2
3 4 5 1 2
4 5 6 + 6 3
4 5 6 1 2 3
4 5 6 7 + 6 3
4 5 6 7 1 2 3
細かく区切ればもっといける
N = 16なら
[13 14 15 16] [9 10 11 12] [5 6 7 8] [1 2 3 4]
A = 4, B = 4
A * B >= Nであれば作れる
LISはグループで分割しよう！！！
"""

N, A, B = getNM()

# mainの長さが半分より下ならout
if A * B < N or N + 1 < A + B:
    print(-1)
    exit()

if A == 1:
    if B == N:
        print(*[i for i in range(N, 0, -1)])
    else:
        print(-1)
    exit()

if B == 1:
    if A == N:
        print(*[i for i in range(1, N + 1)])
    else:
        print(-1)
    exit()

# グループ内の要素の数がA,グループの数がB
res1 = [i + 1 for i in range(N - A, N)]
res2 = []
L = [i + 1 for i in range(N - A - 1, -1, -1)] # 残りN - A個

# 残りN - A個をB - 1個で分割する
ind = (N - A) // (B - 1)
for i in range(B - 1):
    opt = []
    for j in range(ind + (i < (N - A) % (B - 1))):
        u = L.pop()
        opt.append(u)
    res2.append(opt)

res2 = list(reversed(res2))

ans = res1
for i in range(B - 1):
    ans += res2[i]

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)

# print(lis(ans), lis(list(reversed(ans))))
print(*ans)

# Tenka1 Programmer Beginner Contest D - Crossing

"""
1 ~ Nまでの部分集合のうち任意のものを選んで
・1 ~ Nのうちどの整数もどれか2つの組の中に含まれる
・どの２つの部分集合についても共通する数字が１つのみ
N = 3
2個 1 2
2個 3 1    1 3でもいい
2個 2 3

第１条件
2N個の数字を使う
K = N, |Si| = 2にしたらOKではないか？
1 2
2 3
3 4
4 1 みたいに
N = 4だとNoになる？
2 3と4 1が共通項を持たない
他のK - 1個について共通項がちょうど一つ 自身の要素を他のk - 1個に配分する
|S1| = k - 1でなければならない
K * (K - 1) = 2Nならいける
その場合
1 ~ Nについて
N = 6 (k = 4 |Si| = 3)
1 ~ 6を均等に配分
1 2 3
1 4 5
2 4 6
3 6 5

1 2 3 4
1 5 6 7
2 5 8 9
3 6 8 10
4 7 9 10
L字型に敷き詰める要領で
第１のL字 k - 1が2つ　1番目横　他縦
第２のL字 k - 2が2つ　2番目横　他縦
1 2 3 4
5 6 7
8 9
10 +
      1
    5 2
  8 6 3
109 7 4 ピラミッド状に
"""

N = getN()
k = math.floor(math.sqrt(2 * N)) + 1
if k * (k - 1) != 2 * N:
    print('No')
    exit()

ans = [[] for i in range(k)]
# 縦のピラミッド
L = [i + 1 for i in range(N - 1, -1, -1)]
for i in range(k - 1):
    for j in range(k - i - 1):
        u = L.pop()
        ans[i].append(u)

# 横のピラミッド
L = [i + 1 for i in range(N - 1, -1, -1)]
for i in range(k - 1):
    for j in range(k - i - 1):
        u = L.pop()
        ans[j + i + 1].append(u)

print('Yes')
print(len(ans))
for i in range(len(ans)):
    print(len(ans[i]), *ans[i])
