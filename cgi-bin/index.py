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
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ABC167 F - Bracket Sequencing

"""
カッコ列の生成
(をホールドする
)が来たら消す
これで全てなくなるか
Sを好きな順で並べる
(:0, ):1とする
どの0についても、
自身より右側にある1の数 >= 自身より左側にある0の数
どの1についても
自身より左側にある0の数 >= 自身より右側にある1の数
効率的な並べ方は？
0の右側をみる、1の左側をみる
N = getN()
S = [[0 if s == '(' else 1 for s in input()] for i in range(N)]
for i in permutations([i for i in range(4)]):
    opt = []
    for j in range(4):
        opt.append(S[i[j]])
    if not (opt[0][0] == 1 or opt[-1][-1] == 0):
        print(i, opt)
Si内部でまず処理できる　何個余分が残るか
0がn個残り、1がm個残る
[[0, 0], [6, 0], [0, 6], [0, 0]]これをうまいこと行くように並べる
[[1, 1], [0, 0]]
これは左側に1があり、右側に0があるという感じになる
1の処理 → 0の処理になる
0がでかい順、1が小さい順
内部で消していいのかな
思ったよりNoの数が多いのか
ソートの仕方に問題
[2, 0],[0, 1],[0, 1],[0, 1],[50, 2]みたいなのに対処できない
なんとかして
1の個数が0のものから0を回収する
"""

N = getN()
S = [[0 if s == '(' else 1 for s in input()] for i in range(N)]

al = []
for s in S:
    zero = 0
    one = 0
    for i in range(len(s)):
        if s[i] == 0:
            zero += 1
        else:
            if zero > 0:
                zero -= 1 # 相殺
            else:
                one += 1
    al.append([zero, one])

# plusの区間はhpが増加し、minusの区間は減少する
plus = []
minus = []
hp = 0
for a in al:
    if a[1] == 0:
        hp += a[0]
    else:
        if a[0] >= a[1]:
            plus.append(a)
        else:
            minus.append(a)

plus.sort(key = lambda i:i[1]) # 吸収しやすい順
minus.sort(reverse = True)
plus += minus

for z, o in plus:
    if hp < o:
        print('No')
        exit()
    else:
        hp -= o
    # 0の処理
    hp += z

if hp == 0:
    print('Yes')
else:
    print('No')
    # ABC167 F - Bracket Sequencing

"""
カッコ列の生成
(をホールドする
)が来たら消す
これで全てなくなるか
Sを好きな順で並べる
(:0, ):1とする
どの0についても、
自身より右側にある1の数 >= 自身より左側にある0の数
どの1についても
自身より左側にある0の数 >= 自身より右側にある1の数
効率的な並べ方は？
0の右側をみる、1の左側をみる
N = getN()
S = [[0 if s == '(' else 1 for s in input()] for i in range(N)]
for i in permutations([i for i in range(4)]):
    opt = []
    for j in range(4):
        opt.append(S[i[j]])
    if not (opt[0][0] == 1 or opt[-1][-1] == 0):
        print(i, opt)
Si内部でまず処理できる　何個余分が残るか
0がn個残り、1がm個残る
[[0, 0], [6, 0], [0, 6], [0, 0]]これをうまいこと行くように並べる
[[1, 1], [0, 0]]
これは左側に1があり、右側に0があるという感じになる
1の処理 → 0の処理になる
0がでかい順、1が小さい順
内部で消していいのかな
思ったよりNoの数が多いのか
ソートの仕方に問題
[2, 0],[0, 1],[0, 1],[0, 1],[50, 2]みたいなのに対処できない
なんとかして
1の個数が0のものから0を回収する
"""

N = getN()
S = [[0 if s == '(' else 1 for s in input()] for i in range(N)]

al = []
for s in S:
    zero = 0
    one = 0
    for i in range(len(s)):
        if s[i] == 0:
            zero += 1
        else:
            if zero > 0:
                zero -= 1 # 相殺
            else:
                one += 1
    al.append([zero, one])

# plusの区間はhpが増加し、minusの区間は減少する
plus = []
minus = []
hp = 0
for a in al:
    if a[1] == 0:
        hp += a[0]
    else:
        if a[0] >= a[1]:
            plus.append(a)
        else:
            minus.append(a)

plus.sort(key = lambda i:i[1]) # 吸収しやすい順
minus.sort(reverse = True)
plus += minus

for z, o in plus:
    if hp < o:
        print('No')
        exit()
    else:
        hp -= o
    # 0の処理
    hp += z

if hp == 0:
    print('Yes')
else:
    print('No')
    
# ARC120 D - Bracket Score 2

"""
括弧の対応が取れている = 常に(の個数 >= )の個数　かつ (の個数 = )の個数
最大値を求める問題

一番理想的なのは？
a1 < a2 < a3 < a4の場合 a1-a4, a2-a3のペアでもa1-a3, a2-a4のペアでもポイントは同じ
つまり2Nを小さいN個,大きいN個に分けて、小さい-大きいのペアをN個作れればそれが理想

Aを小さいN個、大きいN個でcolorする
あとは普通の括弧列の作り方と一緒

括弧の作り方
前からN個を探索する
一番近くをペアにする
"""

N = getN()
A = getList()
psu = [[A[i], i] for i in range(2 * N)]
psu.sort()

jud = [-1] * (2 * N)
for i in range(N):
    jud[psu[i][1]] = 0
    jud[psu[i + N][1]] = 1

q = []
ans = [''] * (2 * N)
for i in range(2 * N):
    if len(q) == 0:
        q.append([jud[i], i])
    else:
        if q[-1][0] ^ jud[i]:
            ans[q.pop()[1]] = '('
            ans[i] = ')'
        else:
            q.append([jud[i], i])

print(''.join(ans))
