

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

# ABC189 C - Mandarin Orange

N = getN()
A = getList()
A = [[A[i], i] for i in range(N)]
A.sort()

ans = 0
check = [0] * N
U = UnionFind(N)

while A:
    now = A[-1][0]
    index = []
    # 同じ数を引き終わるまで引き続ける
    while A and A[-1][0] == now:
        val, ind = A.pop()
        index.append(ind)
        check[ind] = 1

    # uniteする
    for ind in index:
        # 左側と
        if ind > 0 and check[ind - 1] == 1:
            U.union(ind - 1, ind)
        # 右側と
        if ind < N - 1 and check[ind + 1] == 1:
            U.union(ind, ind + 1)

    # 計算
    for ind in index:
        ans = max(ans, now * U.size(ind))

print(ans)

# 技術室奥プログラミングコンテスト#4 Day2
# E - 引きこもり

N, M, Q = getNM()
E = [getList() for i in range(M)]
E.sort(reverse = True, key = lambda i:i[2])
query = getArray(Q)

U = UnionFind(N)
d = [float('inf')] * (10 ** 5 + 7)
d[1] = 0
que = []
for i in range(N):
    heappush(que, [1, i])

# 混ぜこぜでqueにぶち込んで取り出すときにそれが正しいか判定する
while E:
    now = E[-1][2]
    al = []
    # 抜き取る
    while E and E[-1][2] == now:
        a, b, c = E.pop()
        U.union(a - 1, b - 1)
        al.append([a - 1, b - 1])
    # 判定
    for a, b in al:
        heappush(que, [U.size(a), a])
        heappush(que, [U.size(b), b])

    # 正規のやつを引くまで
    while que[0][0] != U.size(U.find(que[0][1])):
        heappop(que)
    d[que[0][0]] = min(d[que[0][0]], now)

for i in range(len(d) - 2, -1, -1):
    d[i] = min(d[i], d[i + 1])

for q in query:
    if d[q] == float('inf'):
        print('trumpet')
    else:
        print(d[q])

# ABC181 F - Silver Woods

"""
二分探索　っぽいが
半径をrに設定した時にクリアできるか

幅200の道がある
釘がある
釘をうまく避けてゴールに行けるか

釘が少ないケース、釘が一直線なケースを考える
釘が1本なら
上下どちらかの幅が大きい方が答え
釘2本　真上にできる場合は
3つある幅のうち一番大きいやつ
真左にある場合は上下どちらかの幅が大きい方
左上にある場合は
点ABとの距離、上下の幅のうち大きいやつ
釘3本
ルートによって無視していい釘が出てくる
平面走査するか x = iを突破できるか

上下xだけ内側に線を引く
各釘から半径xの円を描く
隙間は残っているか
隙間がなくなるケース
どうやって判定する
円と円の間を通過するか確かめるか
考えるのは2点間
x1 ~ x2を通過できるか
釘によって三角形ができるけど、その三角形に入れるかどうか

接触するなら円弧の反対側まで被害が広がる
まず2つの円が交わる点を計算する
ひし形になる
二つの円の中心から垂直に

接する　場合は通れる　誤差はちょっとであればOKぽいので

上下の直線を結べてしまったらout
"""

N = getN()
P = [getList() for i in range(N)]

# ユークリッド距離を求める
def euc(px1, py1, px2, py2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)

def f(x):
    U = UnionFind(N + 2)
    line1 = N
    line2 = N + 1
    for i in range(N):
        # 点と直線の判定
        x1, y1 = P[i]
        if 100 - y1 < 2 * x:
            U.union(i, N)
        if y1 - (-100) < 2 * x:
            U.union(i, N + 1)
        # 点同士の判定
        for j in range(i + 1, N):
            x2, y2 = P[j]
            if euc(x1, y1, x2, y2) < 2 * x:
                U.union(i, j)

    return not U.same(line1, line2)

ok = 0
ng = 10 ** 12

while ng > ok + 10 ** -10:
    # mid二つ
    mid = (ok + ng) / 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)

# 典型90 068 - Paired Information（★5）O(N + Q)解
# マージテクを使う

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

    # サイズが小さい方が大きい方に統合されるように改造
    def unite(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return

        # サイズに基づいてrootを決める
        # サイズが同じ場合はx += yになる
        if self.size[xRoot] < self.size[yRoot]:
            xRoot, yRoot = yRoot, xRoot

        self.parents[yRoot] = xRoot
        self.size[xRoot] += self.size[yRoot]
        self.size[yRoot] = 0

# UFはサイズの確認をするだけ　値の更新はソラで
N = getN()
Q = getN()
U = UnionFind(N + 1)
d = [0] * (N + 1) # i ~ i + 1間の距離を求める
l = [0] * (N + 1) # 基準点からの相対値

for _ in range(Q):
    t, x, y, v = getNM()
    if t == 0:
        if U.same(x, y):
            continue
        d[x] = v # dを書き込み
        l_size, r_size = U.size[U.find(x)], U.size[U.find(y)] # 左側と右側とでサイズの比較をする

        # 左側を更新
        if l_size < r_size:
            # l[x]を新しく記入
            l[x] = d[x] - l[y]
            # 左のl_size - 1個を右から順に更新
            for i in range(1, l_size):
                l[x - i] = d[x - i] - l[x - i + 1]

        # 右側を更新
        else:
            # l[y]を新しく記入
            l[y] = d[y - 1] - l[x]
            # 右のr_size - 1個を左から順に更新
            for i in range(1, r_size):
                l[y + i] = d[y + i - 1] - l[y + i - 1]

        U.unite(x, y)
    # 求値
    else:
        # 同じグループ内になければ
        if not U.same(x, y):
            print('Ambiguous')
        else:
            if abs(y - x) % 2 == 0: # 距離が偶数の場合
                print(l[y] - (l[x] - v))
            else: # 距離が奇数の場合
                print(l[y] + (l[x] - v))
