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

# ABC006 D - トランプ挿入ソート
n = getN()
lista = [getList() for i in range(n)]

# 最長増加部分列問題 (LIS)の問題
def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)
print(n - lis(lista))

# Donutsプロコンチャレンジ2015 C - 行列のできるドーナツ屋
# LISの応用

N = getN()
H = getList()

# まあBITだろう
# 逆から置くBITではない？
# 累積和？
# 個数だけ求めればいい

# 地点iからは
# i - 1起点の単純増加列
# LIS？
ans = [0] * N
L = []
# 人0 ~ iまでがどのように見えるか これを人i + 1が見る
for i in range(N - 1):
    # もしLの一番小さいやつよりH[i]が大きければ
    while L and L[-1] < H[i]:
        L.pop()
    L.append(H[i])
    ans[i + 1] = len(L)

for i in ans:
    print(i)

# ABC134 E - Sequence Decomposing
N = getN()
A = getArray(N)

def lis(A):
    L = deque([A[0]])
    for a in A[1:]:
        # Lのどの数より小さくければ
        # 繋げられるものがない
        if a <= L[0]:
            L.appendleft(a)
        else:
            # L[bisect_left(L, a) - 1]
            # Lの中のa未満の数字のうちの最大値
            L[bisect_left(L, a) - 1] = a
    return len(L)

print(lis(A))

N = 10
A = [0, 6, 9, 9, 2, 3, 4, 5, 10, 3]

ans = deque([A[0]])
for i in range(1, N):
    # ans[index] A[i]が挟みこめる場所
    # A[0] <= A[i]なら0になる
    # ans[index - 1]: A[i]未満で一番大きい数字
    index = bisect_left(ans, A[i])
    if index == 0:
        ans.appendleft(A[i])
    else:
        # 同じ数が複数ある場合は一番最後の数字が更新される
        ans[index - 1] = A[i]
print(len(ans))

# ABC165 F - LIS on Tree
# 頂点1から頂点kまでの最短パス上
# ルートはO(n)で求められる
N = getN()
A = getList()
query = [getList() for i in range(N - 1)]

dist = [[] for i in range(N)]
for i in range(N - 1):
    a, b = query[i]
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

ignore = [0] * N
ignore[0] = 1
lis = [A[0]]
rec = [0] * N
rec[0] = 1

# 行きがけ帰りがけの要領
def dfs(u):
    global lis
    for i in dist[u]:
        if ignore[i] != 1:
            ignore[i] = 1
            # 巻き戻し用
            plus = 0 # true or false
            change = (0, 0, 0) # true or false, 変更した場所、変更した数値

            if A[i] > lis[-1]:
                lis.append(A[i])
                plus = 1
            else:
                index = bisect_left(lis, A[i])
                change = (1, index, lis[index])
                lis[index] = A[i]
            rec[i] = len(lis)
            dfs(i)
            # 巻き戻す
            if plus:
                lis.pop()
            else:
                lis[change[1]] = change[2]

dfs(0)
for i in rec:
    print(i)

# ACLC1 A - Reachable Towns

N = getN()
Q = [getList() for i in range(N)]
que = deepcopy(Q)
que.sort(key = lambda i:i[1], reverse = True)
que.sort()

# xy座標が共に大きいもの
# 順列になっている？

"""
O(n**2)
U = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if que[i][1] < que[j][1]:
            U.union(i, j)
for i in range(N):
    print(U.count(i))
"""
#　ソート方法はこれでOK
# やらなくていい探索がある　それを減らす
# 4 3
# 4 1
# 4 2
# 3 1
# 3 2
# 1 2 これだけいる

# 4 3 1 2でi < jになるものをペアに
# 1とペアにできるのは2, 3, 4
# 2とペアにできるのは3, 4
# 3は4
# それぞれ右側にあれば

# 6 7 5 3 2 4 1
# グループ１ 6 7
# グループ2 5
# グループ3 3 2 4
# グループ4 1
# どれか１つのグループに属する

U = UnionFind(N + 1)
group = []

for x, y in que:
    # １番目のものは必ずグループのリーダーになれる
    if not group:
        group.append(y)
        continue
    # リーダーが降順に並ぶように
    if y < group[-1]:
        group.append(y)
        continue
    opt = float('inf')
    # グループ再編成
    while group:
        # yより小さいものは全てyが所属するグループに入る
        if y > group[-1]:
            l = group.pop()
            U.union(l, y)
            opt = min(opt, l) # yが所属するグループの中のリーダー　一番最初のものが記録される
        else:
            break
    # リーダー変更
    group.append(opt)

for i in range(N):
    print(U.count(Q[i][1])) # yがiのもののサイズの大きさ　uf.funcはインデックスで呼ばなくてもいい

# ARC091 E - LISDL

"""
最長増加部分列の長さはA　
最長減少部分列の長さはB
使える数字は1 ~ N
一番都合のいいものを探す
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

# ARC126 B - Cross-free Matching

"""
クロスしないようにしないといけない
つまり幅が大きいやつは不利に

多分貪欲
ソートした上でのlis

[1, 3], [3, 1], [3, 3]は2ですか？　違います...
reverseソートしとく
reverseが保たれたままにしとくにはkey = lambda i:i[0]ソートをする
"""

N, M = getNM()
E = [getList() for i in range(M)]
E.sort(key = lambda i:i[0], reverse = True) # Aでソート
E.sort(key = lambda i:i[1]) # Bでソート

o1 = [e[0] for e in E] # Aのlis
E.sort(key = lambda i:i[1], reverse = True) # Bでソート
E.sort(key = lambda i:i[0]) # Aでソート
o2 = [e[1] for e in E] # Bのlis

print(max(lis(o1), lis(o2)))
