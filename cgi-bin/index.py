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
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ARC021 B - Your Numbers are XORed...

"""
2 010 + 4 100 = 6 110
3 0011 + 12 1100 = 15 1111

元のA:{A1, A2...}を知りたい
Bi = Ai xor Ai+1
Bi+1 = Ai+1 xor Ai+2
Bi xor Bi+1 = Ai xor Ai+1 xor Ai+1 xor Ai+2
B1 xor B2 xor...Bn-1 = Ai xor An ?
Bn = An xor A1

B1 xor B2 xor...Bn = A1 xor A1 = 0 ?
該当する数列が存在するならこれは成立つ
B1 ^ A1 = A2
B2 ^ A2 = B2 ^ (B1 ^ A1) = A3
"""

L = getN()
B = getArray(L)

now = B[0]
for i in range(1, L):
    now ^= B[i]

if not now:
    # A1は辞書順最小なので0に
    a = 0
    for i in range(L):
        print(a)
        a ^= B[i]
else:
    print(-1)

# ABC098 D - Xor Sum 2
# 連続する区間の長さを答える　尺取り

N = getN()
A = getList()

l, ans, xo, total = 0, 0, 0, 0

for r in range(N):
    xo ^= A[r]
    total += A[r]

    # xo == totalになるまでA[l]で引き続ける
    while xo < total:
        xo ^= A[l]
        total -= A[l]
        l += 1

    ans += r - l + 1

print(ans)

# 第五回ドワンゴからの挑戦状 B - Sum AND Subarrays

"""
N <= 1000
連続部分列は全て取り出せる
どうやってK個を選ぶか

optを達成できるか
bit数が大きい方が絶対正義
とにかく大きいbitを立てる
"""

N, K = getNM()
A = getList()

l = []
for i in range(N):
    now = 0
    for j in range(i, N):
        now += A[j]
        l.append(now)

flag = 0 # フラグを強化していく

# フラグiが建っているものを集める
for i in range(60, -1, -1):
    opt = flag | (1 << i)
    cnt = 0
    for j in range(len(l)):
        if l[j] & opt == opt:
            cnt += 1
    if cnt >= K:
        flag |= (1 << i)

print(flag)


# ABC117 D - XXOR
"""
K以下
Kを使えば最強でない？
7 ^ 1 = 6 7 ^ 6 = 1 7 ^ 3 = 4となり弱い
i桁目についていくつフラグが立つか
Kが1ならA内の0の数だけ
Kが0ならA内の1の数だけ

とにかく大きいフラグを建てたい

1: 001
6: 110
3: 011

2 ** 2桁目について 0のが多いので立てる
2 ** 1桁目について 1のが多いので立てない
・フラグは強化していく方針　なるべく大きいフラグを立てる
・なるべくフラグは建てない　cnt > N // 2の時
"""

N, K = getNM()
A = getList()

flag = 0
ans = 0
for bi in range(62, -1, -1): # bitは最大60ぐらいやればいい
    cnt = 0
    for i in range(N):
        cnt += (not A[i] & (1 << bi))
    if cnt > N // 2 and flag + 2 ** bi <= K: # フラグを立てる
        flag += 2 ** bi
        ans += (cnt * 2 ** bi)
    else:
        ans += ((N - cnt) * 2 ** bi)

print(ans)

# ABC121 D - XOR World
A, B = getNM()
# bit1桁目のフラグの個数
# 周期は2 ** 1
# 0と1が交互に
# bit2桁目のフラグの個数
# 周期は2 ** 2
flags1 = [0] * 61
flags2 = [0] * 61
# 1 ~ nまでに各桁のフラグが何本立つか計算する関数
def bitflag(n, flaglist):
    if n > 0:
        for i in range(1, 61):
            split = 2 ** i
            flag1 = (n // split) * (split // 2)
            flag2 = max(n % split + 1 - (split // 2), 0)
            flaglist[i] += flag1 + flag2
# 1 ~ A - 1について（Aは範囲に入っているため）
bitflag(A - 1, flags1)
bitflag(B, flags2)
for i in range(61):
    flags2[i] -= flags1[i]
ans = 0
# 奇数ならフラグが立つ
for i in range(61):
    if flags2[i] % 2 != 0:
        ans += 2 ** (i - 1)
print(ans)

# ABC147 D - Xor Sum 4

N = getN()
A = getList()
# Aの各数字の（２進数における）各桁ごとに分解して排他的論理和を求める
# 例
# 3
# 1 2 3 →
# 1, 10, 11
# 2 ** 0の桁について(1 ^ 2) 1 ^ 0 = 1,(1 ^ 3) 1 ^ 1 = 0,(2 ^ 3) 0 ^ 1 = 1
# 2 ** 1の桁について 0(1の2 ** 1の桁は0) ^ 1 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0
# 各桁について2 ** iの桁が1の数字の選び方 * 2 ** iの桁が0の数字の選び方 * 2 ** iを
# 足し合わせる
lista = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            lista[i][1] += 1
        else:
            lista[i][0] += 1
for i in A:
    splitbit(i)
ans = 0
for i in range(61):
    ans += ((lista[i][0] * lista[i][1]) * (2 ** i)) % mod
print(ans % mod)

# ARC021 B - Your Numbers are XORed...
L = getN()
B = getArray(L)
B_xor = B[0]
for i in range(1, L - 1):
    B_xor ^= B[i]

# B_xor ^ a1(aの最後) ^ a1 == Bの最後なら成立
# この時aがどんな値であろうと条件が成立する
if B_xor == B[-1]:
    now = 0
    print(now)
    # a2 = B1 ^ a1
    # a3 = B2 ^ a2
    for j in range(L - 1):
        now = B[j] ^ now
        print(now)
else:
    print(-1)

# Tenka1 Programmer Contest D - IntegerotS

"""
Aのbitの総和がK以下になるように整数を集める
ナップサック問題っぽいがAもBもおおきい
貪欲に行く
Kを超えた場合でも、他のでフラグを消せればいい

まず全部足し、フラグを抜いていく？
dpっぽいが2 ** 30の30を使う？
フラグの数が奇数か偶数か

bitwise or どちらかのビットが1なら1、そうでなければ0
一度立てたフラグは消えない

Kの各bitについて
フラグを立てるか立てないか
0 のbitlengthは0
1 のbitlengthは1 (右から1番目に最初のフラグが立っている)
2 のbitlengthは2
3 のbitlengthは2

[0, 0, 8, 4, 0, 0, 0,
むやみにフラグを立てないように

K = 101にどう従っていくか
1本目を1にするなら それ以降の条件にも従ってもらう

Kと比べた時に何本目まで従っているか
K = 101
a = 10の場合左から2番目が従えてない
[[3, 3, 1], [4, 4, -1], [2, 5, 1]]

別に30回回していい
一本目のKについて
立てるなら
Kにフラグが立ってなかったら
立ててはいけない

K以下の値の2進数換算は
Kのi番目の1のフラグを1 → 0にし、それ以下を自由にしたもの　である
フラグの数が多い方がいいので
整数を集めてできる数をXとすると
K = 11010の場合は
X = 01111, 10111, 11001 を見ていけばいい
足してXになる数を求めればいい

K以下の〜について
最も有利な条件を並べてそれぞれで計算
"""

N, K = getNM()
que = [getList() for i in range(N)]

ans = 0
# 足すとKのフラグになる
opt = 0
for a, b in que:
    if K | a == K:
        opt += b
ans = max(ans, opt)

# 足すとXのフラグになる
for i in range(31, 0, -1):
    opt = 0
    if K & (1 << i): # フラグが立っていれば
        X = (K ^ (1 << i)) | ((2 ** i) - 1) # 1 << iのフラグを消す + それ以下を全て1に
        for a, b in que:
            if X | a == X: # フラグの本数が変わらなければ
                opt += b

        ans = max(ans, opt)

print(ans)

# ZONE F - 出会いと別れ

"""
ワープゲートを作る
Nは2の冪乗　0 ~ N - 1 完全二分木
AはN以下　a ^ bがどれかに引っかかるとNG

4 1
3 の場合
1 ^ 2 = 3であるため作れない

0, 1... についてペアの結び方が必ず一つはある
他の全てと結ぶとどのようなxor ができるだろう

0: 1 ~ N - 1そのまま
1: 0(0), 11(10), 10(11), 101(100),
結べる限りどんどん繋いでいく 各O(1)で

N^2解は
0と結べるものを結ぶ　結んだものについてさらに結べるものと結んでいく
0と結べるもの　がO(1)でパッと出れば
ある共通の属性を持つものは結べるものが似てくるのでは

ヒープキュー とか使うかも
小さい方か大きい方から順にやるか

0とN - 1は重要
Aiがない惑星は0と繋げるし、N - Ai - 1にない惑星はN - 1と繋げる
0 1 2 3 4 5 6 7
7 6 5 4 3 2 1 0 どちらか一方がなければ繋げる

頂点を出すごとにリストAに操作を加えて
小さい順から順番に？
必ず相手がいる状態に

あれば繋げる

逆にないAiで結べるペアは？

1個しか結べない　が半分以上あればout
残ってるものを探索する

全域木になる条件： 0とiが繋がるか
Aじゃないやつの集合をaとすると
0 ^ a1: 0とa1が繋がる
0 ^ (a1 ^ a2): 0と(a1 ^ a2)が繋がる
つまり a内の要素をxorして1 ~ N - 1まで全ての数字を作れるなら
0からいくつかの数字を経由してiに繋げる
逆に数字を作れないなら0からiへのルートはない

a内の数字を使って全ての要素を作れるか
2 ** nの位置にフラグがあればそこをつけたり消したりできる
最高次が2**nのものを探す
なくても上の次数2つを相殺させればrankが一つ下のを作れるから
"""

N, M = getNM()
ok = [1] * N
for A in getList():
    ok[A] = False
base = [] # 元の数字
elim = [] # 消す用

# Aiではないもの小さい順に全て試す
for x in range(1, N):
    if not ok[x]:
        continue
    y = x
    for b in elim:
        # 小さい数字を使ってフラグを消していく
        # 立っているフラグが消えるならy ^ bが選ばれる
        y = min(y, y ^ b)
    # 最上位のフラグが残ってるなら xをbaseとして利用できる
    if y:
        base.append(x)
        elim.append(y)

def lg(x):
    return x.bit_length() - 1

if len(base) != lg(N):
    exit(print(-1))

# 0から順に繋いでいく
xor = 0
for x in range(1, N):
    print(xor, end=' ')
    # base[i]: 2 ** iを担当するx
    xor ^= base[lg(x & -x)] # x & -x: xの一番下のフラグ
    print(xor)

# # codeforces round735
# C

# xorしたもののmex
# xorをそれぞれ求めていく
# nが固定になっている　連続するものなので
# O(1)で求めないと
# N ^ i は全て違う数になる

# 0が作れるか
# i以下が全て存在するか
# N > Mなら0は作れない　答えば0
# 2^i ~ 2^i+1の値を全て作れるか
# n = 1010 で ~ 1111を全て作りたい
# 5を作りたい場合 i = 15である必要がある
# 10??で 0 ~ 3は全て作れる 最大は1011 mを超えているか
# 1???で 0 ~ 7は全て作れる 最大は1111
# ????で 0 ~ 15は全て 最大は1111 mを超えているか

# 超えていない場合　2^i ~ 2^i+1の間に作れない数字があり、探索が始まる
# 1011 ○　1111 xの場合
# 1100 ~ 1111にmがある
# 小さい順から探索していく

# bitの問題は2^i ~ 2^1+1でグルーピングしていく
# 2^i以下を作れるかで判定していく
# (これまで立てたフラグ | N) | ((1 << i) - 1)(111...)がM以下なら
# res | (1 << i) 以下の数字は全て作れる

T = getN()
for i in range(T):
    N, M = getNM()
    res = 0
    for i in range(32, -1, -1):
        if (res | N) | ((1 << i) - 1) <= M:
            res |= (1 << i)
    print(res)
