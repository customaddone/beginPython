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

# ARC027 B - 大事な数なのでZ回書きまLた。

"""
N桁の数字を覚えて置きたい
大文字アルファベットがそれぞれ0 ~ 9のうちのどれかの数字に対応している

Unionfindとか最大流とか
N <= 18 bit　dpまで狙える

覚えておく数字について何通り考えられるか
10 ** 18通りの数字があるがその中で？
ただし制約がある
候補を絞って全探索

アルファベットと各数字を対応させる通りは10 ** 26通り
4
1XYX
1Z48 の場合
X - Zは同じ
Y - 4は同じ
X - 8は同じ
なのでZ - 8
S1とS2に出てくる文字がどの数字と対応しているかを求めればいい

6
PRBLMB
ARC027 の時

P - A
B - C
L - 0
M - 2
B - 7
B - 7よりC - B - 7
P - AグループとRに対応する数字を求めればいい

UnionFindする
出現した文字のリスト
出現した文字が何の数字か
"""

N = getN()
S1 = input()
S2 = input()
str_c = [0] * 26 # 文字が出現したか
number = [-1] * 26 # どの文字が割り当てられているか
ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

U = UnionFind(26)
# 通りが0の場合もあるが
for i in range(N):
    # 両方文字ならグループ化
    if (S1[i] in ascii_uppercase) and (S2[i] in ascii_uppercase):
        str_c[ord(S1[i]) - ord('A')] = 1
        str_c[ord(S2[i]) - ord('A')] = 1
        U.union(ord(S1[i]) - ord('A'), ord(S2[i]) - ord('A'))
    if not (S1[i] in ascii_uppercase) and not (S2[i] in ascii_uppercase):
        if int(S1[i]) != int(S2[i]): # そもそも数字同士が違う
            print(0)
            exit()

# グループ化し終わったら数字を対応させる
# あるグループにアクセスするときはU.find(i)でアクセスする
# するとグループの代表者が出てきてくれる
# そのグループの代表者にどの文字と対応しているか、先頭の文字かを尋ねる
for i in range(N):
    if (S1[i] in ascii_uppercase) and not (S2[i] in ascii_uppercase): # S1が文字
        str_c[ord(S1[i]) - ord('A')] = 1
        if number[U.find(ord(S1[i]) - ord('A'))] == -1: # 未登録
            number[U.find(ord(S1[i]) - ord('A'))] = int(S2[i])
        else:
            if number[U.find(ord(S1[i]) - ord('A'))] != int(S2[i]): # 矛盾する
                print(0)
                exit()

    if not (S1[i] in ascii_uppercase) and (S2[i] in ascii_uppercase): # S2が文字
        str_c[ord(S2[i]) - ord('A')] = 1
        if number[U.find(ord(S2[i]) - ord('A'))] == -1:
            number[U.find(ord(S2[i]) - ord('A'))] = int(S1[i])
        else:
            if number[U.find(ord(S2[i]) - ord('A'))] != int(S1[i]):
                print(0)
                exit()

first = [0] * 26 # 一番前の数字か
if (S1[0] in ascii_uppercase):
    first[U.find(ord(S1[0]) - ord('A'))] = 1
    if number[U.find(ord(S1[0]) - ord('A'))] == 0: # 一番最初の文字に0が登録されていたら
        print(0)
        exit()

if (S2[0] in ascii_uppercase):
    first[U.find(ord(S2[0]) - ord('A'))] = 1
    if number[U.find(ord(S2[0]) - ord('A'))] == 0:
        print(0)
        exit()

ans = 1
# 未登録の数字については0 ~ 9または1 ~ 9になる可能性がある
for i in range(26):
    if str_c[i] and number[U.find(i)] == -1: # 未登録なら
        if first[U.find(i)]:
            ans *= 9 # 1 ~ 9
            number[U.find(i)] = 10
        else:
            ans *= 10
            number[U.find(i)] = 11

print(ans)

# AtCoder Petrozavodsk Contest 001 D - Forest

"""
森です Unionfind?
森を連結にする最小コスト
制約的に最大流無理

Impossibleの条件
一つ繋ぐごとに頂点が２つ減り、森が一つ減る
森が2個以上でもう繋げなくなったらimpossible

小さい例から考える
7 5
1 2 3 4 5 6 7
3 0
4 0
1 2
1 3
5 6　の時

1 - 2 - 3 - 4 - 5
6 - 7

1と6を繋げばいい
1 - 2
3 - 4 - 5
6 - 7
の場合
motherを一つ決める(例えば1 - 2)
childは3 - 4 - 5, 6 - 7
motherの一番小さい奴とchildの一番小さい奴を消費して連結する
グループ分けする
[1, 2]
[3, 4, 5]
[6, 7] 全部ヒープキュー
小さい2つを消費(ansに加える)
併合

motherは一番でかい奴から！！！
ゆとりのある順に並べる

motherは慎重に決めないといけない
各グループの先頭列をみる
小さい順に使いたい
各グループの先頭は必ず使う
合計で2 * (g_n - 1)頂点いる
g_n - 1については各グループの先頭にしないといけない　他のは？
あとは自分以外のところから自由に　全てmotherの所有物
足すのはg_n - 1回だけでいい

groupの隣同士を併合するだけでいい
要素にグループ番号をつけて前から並べる
unionしてなかったら
motherは決めない

先頭の奴は絶対に使う
あとは小さい順から　自分以外のとこの適当なグループの先頭に繋げてやればよい

UnionFindの問題は先頭とそれ以外　という考え方をする
"""

N, M = getNM()
A = getList()
que = [getList() for i in range(M)]

# グループ分け
U = UnionFind(N)
for a, b in que:
    U.union(a, b)

group = [[] for i in range(N)]
for i in range(N):
    group[U.find(i)].append(A[i])
group = [sorted(i) for i in group if len(i) > 0]

if len(group) == 1:
    print(0)
    exit()

g_n = len(group)

ans = 0
l = []

# 先頭の絶対使う奴と二番手以降の遊撃隊に分ける
for i in range(g_n):
    ans += group[i][0]
    while len(group[i]) > 1:
        u = group[i].pop()
        l.append(u)

l.sort(reverse = True)

# 残りの頂点は小さい順
for i in range(g_n - 2):
    if l:
        u = l.pop()
        ans += u
    else:
        print('Impossible')
        exit()
print(ans)

# ABC183 F - Confluence

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.C = [defaultdict(int) for _ in range(n)]
        self.size = [1] * n # サイズの大きさ

    def find(self,x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return

        # サイズに基づいてrootを決める
        if self.size[xRoot] < self.size[yRoot]:
            xRoot, yRoot = yRoot, xRoot

        self.parents[yRoot] = xRoot
        self.size[xRoot] += self.size[yRoot]
        self.size[yRoot] = 0

        # 小さいサイズのものを大きいサイズの方に入れる
        for k,v in self.C[yRoot].items():
            self.C[xRoot][k] += v

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

N, Q = getNM()
tree = UnionFind(N)
C = getList()

# 使いたいときは使ったらいい
for i in range(N):
    tree.C[i][C[i] - 1] += 1

for _ in range(Q):
    q, a, b = getNM()
    if q == 1:
        tree.unite(a - 1, b - 1)
    else:
        r = tree.find(a - 1)
        print(tree.C[r][b - 1])

# ABC049 D - 連結

N, K, L = getNM()
road = [getList() for i in range(K)]
line = [getList() for i in range(L)]

# 道路をやる
R = UnionFind(N)
for p, q in road:
    R.union(p - 1, q - 1)

L = UnionFind(N)
for i in range(N): # 自分がどの道路グループにいるか
    L.C[i][R.find(i)] += 1

for r, s in line:
    L.union(r - 1, s - 1)

# 自分の線路グループL.find(i)にある自分の道路グループR.find(i)の数
ans = [L.C[L.find(i)][R.find(i)] for i in range(N)]
print(*ans)

# ABC173 F - Intervals on Tree
# ある意味Unionfindか
# 新しい頂点を加えると、連結成分が1 - (既にある頂点へのエッジ)の分増える

"""
木の問題
N <= 10 ** 5
辺があると連結するので連結成分の個数が減る
L,RをnC2通り求める
bitは普通に間に合わない

やっぱり分解して考える
小さいのから
L = 1の時
R = 1 ~ N これにO(1)で答える
R = 1
1
R = 2 2は1と繋がってない
1
2 2
R = 3 3は1, 2と繋がっている
1 2 3 1

頂点1は何回数えられるか
頂点1が含まれるのは3回
頂点2が含まれるのは4回
頂点3が含まれるのは3回

木dpとか
前から順にやる？

Rで新しい数を入れると急に結合したりする
数え上げでしょう

ダブった部分を引く
全ての部分木の大きさを求めるのは無理そう
新しい要素は高々２つの要素を繋げるだけ

for i in range(N - 1):
    u, v = getNM()
    if u > v:
        u, v = v, u
    # 前に戻るエッジのみ
    dist[v - 1].append(u - 1)
for i in range(N):
    dist[i].sort()

ans = 0
for i in range(N): # L
    cnt = 0
    for j in range(i, N): # R
        # 範囲外に伸びるエッジは無視
        cnt += 1 - (len(dist[j]) - bisect_left(dist[j], i))
        ans += cnt

これはO(N ** 2)かかる
[[], [], [], [], [2], [], [1, 3, 4], [3], [0, 7], [5, 8]]
累積されていく
何もなければ1 ~ 10の累積で55のはず
しかし控除が累積して1 + 1 + 4(len([2] + len([1, 3, 4]))) + 5 + 7 + 9 = 27あるのでこれを引く
dist[4]の位置にある2はL = 1の時も引っかかる
dist[8]にある0は一回のみ引っかかって被害はN - 8 = 2

エッジが伸びることでいくら減るか
"""

N = getN()
dist = [[] for i in range(N)]
for i in range(N - 1):
    u, v = getNM()
    # 前に行くように
    if u > v:
        u, v = v, u
    dist[v - 1].append(u - 1)

ans = 0
cnt = 0
for i in range(N):
    ans += (i + 1) * (i + 2) // 2
    # distの探索
    for j in dist[i]:
        cnt += (j + 1) * (N - i)

print(ans - cnt)
