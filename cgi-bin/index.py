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

# エイシング プログラミング コンテスト 2019 D - Nearest Card Game

"""
つまりnim
青木君がXiを指定する
高橋くん→青木くんの順番でAから数字を取っていく
高橋くん: 最も大きい数字を取る
青木くん: Xに最も近い数字を取る　複数あれば小さい方
カードがなくなれば終了　
各Xについて高橋くんが取るカードの合計を求めよ
O(1)でやる　テーブルで累積和とかなんかを前処理してO(1)で参照する
Nが偶数: 高橋くんはN // 2枚のカードを取る
Nが奇数: 高橋くんはN // 2 + 1枚のカードを取る

Xが変化するごとに取るカードがどのように変化するか
5 5
3 5 7 11 13
X = 1の時、近いカードは順に3, 5, 7, 11, 13
つまり高橋くんは13, 11, 7を取る
X = 4の時、近いカードは順に3, 5, 7, 11, 13
X = 9の時、近いカードは順に7, 11, 5, 13, 3
X = 10の時             11,  7,13,  5, 3

X = 10の場合　7,  5, 3...
            11, 13...
高橋くんの取るカードは    13, 11, 7,  5, 3
7と5がスキップされるので、13 + 11 + 3 = 27
高橋くん、青木くんの取る順番がわかれば得点をO(1)でもとめれればいいのだが
13, 11, 7, 5, 3
7, 11, 5, 13, 3 互いにスキップされ合う
高橋くんがiを取るスピードが青木くんより早い、もしくは同じなら取得できる
そうでなければ青木くんが取得する
X = 23の場合
高橋: 13, 11, 7, 5, 3
青木: 13, 11, 7, 5, 3
13 + 7 + 3で23 これを各O(1)で求めたいが
累積和しそうだ
NlogNまでならいける　各XiについてlogNで
青木くんが取る順番は求めなくていい？
高橋くんが取れるどうかだけ？
X = 4からの距離
1, 1, 3, 7, 9: 3 5 7 11 13
X = 5
2, 0, 2, 6, 8: 5 3 7 11 13
X = 6
3, 1, 1, 5, 7: 5 7 3 11 13
X = 7
4, 2, 0, 4, 6: 7 5 3 11 13
X = 8
5, 3, 1, 3, 5: 7 5 11 3 13
X = 9
6, 4, 2, 2, 4: 7 11 5 13 3
スワップしていく？

X = 1の時
3, 5, 7, 11, 13
X = 4の時
5, 7, 11, 13
3
X = 9の時
11, 13
7, 5, 3
Xiから近い順とA[-1]から近い順
3 5 7 11 13
     10  13
bisect_rightでXiでのスタート地点は求められる
Xi-1の時と何が違うか

A1, A3...の合計とA2, A4...の合計を求める
Aは[(高橋と青木が交互に取るゾーン), (青木が取るゾーン), (高橋が取るゾーン)]になる
その境界を求める
"""

N, Q = getNM()
A = getList()
X = getArray(Q)

csum = [0]
for i in range(N):
    csum.append(csum[-1] + A[i])
csum_even = [0]
for i in range(0, N, 2):
    csum_even.append(csum_even[-1] + A[i])
csum_odd = [0]
for i in range(1, N, 2):
    csum_odd.append(csum_odd[-1] + A[i])

#t回でX以下のAのみとなってしまうような最小のtを求める。
def calc_t(X):
    ok = -1
    ng = N + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        aoki = mid // 2
        taka = mid - aoki
        aoki_max = A[-taka]
        aoki_min_index = bisect_left(A, 2 * X - aoki_max)
        if N - taka - aoki_min_index < aoki:
            ng = mid
        else:
            ok = mid

    return ok

for x in X:
    t = calc_t(x)
    s = csum[N] - csum[N - (t + 1) // 2]

    if N % 2 == 0:
        s += csum_odd[(N - t) // 2]
    else:
        s += csum_even[(N - t + 1) // 2]
    print(s)

# CODE FESTIVAL 2015 予選A D - 壊れた電車

"""
N両編成 M人の整備士
隣に行くのに1分かかる
全ての車両を周回するのにかかる時間は

それぞれについて境界値を求める問題
一方通行するのとジグザグに行くの２パターンある
二分探索したい k分でどこまで周回できるか
振った方が有利なのか

出来る限り右の車両を点検する
絶対にこの人にしか周回できない場所を考える
絶対に誰にもいけない左端があればout
"""

N, M = getNM()
X = getArray(M)

def judge(x):
    now = 0
    for i in range(M): # 2 ~ N番目の人について
        # now + 1番目を点検しないといけない
        # 左側にいくつ進まないといけないか
        want = max(0, X[i] - (now + 1)) # そこまで行かないといけない
        if want > x: # 時間が足りない場合False
            return False
        else:
            # 左行って右行くか、右行って左行くかどちらか大きい方
            now = max(now, X[i], X[i] + max(x - 2 * want, (x - want) // 2))

    return now >= N # 最後まで整備できたか

ok = 2 * (10 ** 9 + 7)
ng = -1 # 0回の周回でいい場合もある

while ok - ng > 1:
    mid = (ok + ng) // 2

    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)

# 京都大学プログラミングコンテスト 2020 E - Sequence Partitioning

"""
Aをいくつかの部分列に分割する　幾つでもいい
選んだ区間dのスコアは(区間内におけるbの最初の値) + (区間内におけるcの最後の値) + (区間内のaの総和)
D = {d1, d2...}の最小値を最大化せよ

N <= 10 ** 5
dpする？
区間をi個に分割する　を探索する？

まずは全探索、貪欲で考える
Aのみの最小値の最大化は？
1 2 3 とかの場合は1つにまとめる
-3 1 2 3の場合も一つにまとめる

-3 -2 -1 とかの場合は分解する
-3 -2 -1 7 の場合はそのまま　合計がプラスになるならひとまとまりの方がいい

dp[i]: iまでで区切った時、ここまで分割した時の最小値
dp[i] = min(dp[i - 1] + D[i-1:i], dp[i - 2] + D[i-2:i]...)
これまでのdpの最小値だけならセグ木でいいがDが...
更新できるものだけでいい

小さすぎる数が出てくる　それは見なくていい
dp[i]が小さかったら新しい区間の数が何であろうと関係なくdp[i]の数字がopt
なので新しい数字を引っ張ってくるとしても0からor今までで一番大きいdpがあるindexからのみ

dp + 二分探索で求める x以上にすることができるか
"""

def f(x):
    p = B[0] # C[-1]に接続するpを決める
    for i in range(1, N):
        # p + C[i] >= xならp ~ iまで繋げる
        # つなげる場合は一番大きなB[i]をpにする
        # pの候補は ①Cに繋いだ時にxを超えるか（緩く）
        # 　　　　　②その中でも一番大きなB[i](こだわる)
        if p + C[i] >= x and p < B[i]:
            p = B[i]
    if p + C[-1] >= x:
        return True
    else:
        return False

N = getN()
A = [0] + getList()
B = getList()
C = [0] + getList()

for i in range(N):
    A[i + 1] += A[i]

# p + C[-1]するときにいい感じに累積が取れる
# A[r] - A[l - 1]がしたいので、Bは右に一つずらす
for i in range(N):
    B[i] -= A[i]

for i in range(N + 1):
    C[i] += A[i]

ok = -1
ng = 2 * 10 ** 20

while abs(ng - ok) > 1:
    m = (ok + ng) // 2
    if f(m - 10 ** 20):
        ok = m
    else:
        ng = m

print(ok - 10 ** 20)

# ARC021 C - 増築王高橋君

"""
愚直にやるとN^K回かかるが
4
3
10 3
12 4
15 5
コストが一番小さいものを選択すればいい
ヒープキュー使ってKlogN
que = []
for i in range(N):
    a, d = getNM()
    heappush(que, [a, d])

ans = 0
for i in range(K):
    o_a, o_d = heappop(que)
    ans += o_a
    heappush(que, [o_a + o_d, o_d])

こいつをKの線形時間にする
queの遷移を考える
10 [[12, 4], [15, 5], [30, 3]]
22 [[15, 5], [30, 3], [48, 4]]
37 [[30, 3], [48, 4], [75, 5]]
67 [[48, 4], [75, 5], [90, 3]]
先頭部分はもう一つ先を超えない程度の回数繰り返せるが
一番大きいやつは当分使わない
que[0]を最大にする、抜くを繰り返す

各要素は抜きつ抜かれつを繰り返す
ある程度までワープしてもいいんじゃないか
ターゲットを決める　そこまでフルに足す
"""

K = getN()
N = getN()
que = [getList() for i in range(N)]

# どのあたりまで足し合わせようか
def f(target):
    cnt = 0
    sum_cost = 0
    for i in range(N):
        a, d = que[i]
        count = ((target - a) + d - 1) // d
        cnt += count

    return cnt

ok = max([i[0] for i in que]) # 下限はaの最大値
ng = 10 ** 9 + 7

# にぶたん
while abs(ng - ok) > 1:
    m = (ok + ng) // 2
    if f(m) < K:
        ok = m
    else:
        ng = m

opt = f(ok)
ans = 0

# 復元
if opt < K:
    for i in range(N):
        a, d = que[i]
        count = ((ok - a) + d - 1) // d
        K -= count
        ans += a * count + d * (count * (count - 1) // 2)
        que[i] = [a + d * count, d]

# あとは愚直
new_que = []
for i in range(N):
    a, d = que[i]
    heappush(new_que, [a, d])

for i in range(K):
    o_a, o_d = heappop(new_que)
    ans += o_a
    heappush(new_que, [o_a + o_d, o_d])

print(ans)

# ABC200 Patisserie ABC 2

"""
i + j
2 ~ N + 1までが j - 1個
N + 2 ~ 2Nまでが N - 1 ~ 1個(2N - j + 1)

パラメータv以下の数字はいくつあるかは二分探索で求められる

パラメータv以下の数字がいくつあるかが求められた
N = 2の時f(4) = 4
        f(5) = 7より パラメータが5のところに求める値がある

パラメータがvのもののうち綺麗さがjのものはいくつあるか
また二分探索が
これも求まる
パラメータがvで綺麗さがiのものを探る
これを美味しさの順に並べる
"""

def f1(x):
    res = 0
    # i + jのそれぞれについて
    # 2は1個、3は2個...
    for i in range(2, 2 * N + 1):
        # jは確定できない
        if x <= i:
            break
        if i <= N + 1:
            res += min(N, x - i) * (i - 1)
        else:
            res += min(N, x - i) * (2 * N - i + 1)

    return res

# パラメータがxのもので綺麗さがy以下のものの個数
# 残りのj + kの組み合わせがいくつあるか
# j = 1から数えていく
def f2(x, y):
    res = 0
    for i in range(1, y + 1):
        left = x - i
        if left <= 0 or 2 * N < left:
            continue
        if left <= N + 1:
            res += left - 1
        else:
            res += 2 * N - left + 1

    return res

N, K = getNM()
ok = -1
ng = 3 * N + 1

# パラメータが決まる ok + 1
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if f1(mid) < K:
        ok = mid
    else:
        ng = mid

ans1 = ok + 1
K -= f1(ok)

# 綺麗さの値がわかる ok + 1
ok = -1
ng = N + 1
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if f2(ans1, mid) < K:
        ok = mid
    else:
        ng = mid

ans2 = ok + 1
K -= f2(ans1, ok)

# あとは並べる
l = []
for j in range(1, N + 1):
    if 1 <= ans1 - ans2 - j <= N:
        l.append([ans2, j, ans1 - ans2 - j])
print(*l[K - 1])
