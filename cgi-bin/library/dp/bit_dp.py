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


from sys import exit


import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N = 4
inf = float('inf')

d = [
[0, 2, inf, inf],
[inf, 0, 3, 9],
[1, inf, 0, 6],
[inf, inf, 4, 0]
]

dp = [[-1] * N for i in range(1 << N)]

def rec(s, v, dp):
    if dp[s][v] >= 0:
        return dp[s][v]
    if s == (1 << N) - 1 and v == 0:
        dp[s][v] = 0
        return 0
    res = float('inf')
    for u in range(N):
        if s & (1 << u) == 0:
            res = min(res,rec(s|(1 << u), u, dp) + d[v][u])
    dp[s][v] = res
    return res
# 結局のところ0からスタートしようが1からスタートしようが同じ道を通る
print(rec(0,0,dp))

# ABC054 C - One-stroke Path

N, M = getNM()
dist = [[] for i in range(N + 1)]
for i in range(M):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

cnt = 0

pos = deque([[1 << 0, 0]])

while len(pos) > 0:
    s, v = pos.popleft()
    if s == (1 << N) - 1:
        cnt += 1
    for u in dist[v]:
        if s & (1 << u):
            continue
        pos.append([s | (1 << u), u])
print(cnt)

# N * N の距離の票をあらかじめ作ろう
def counter(sta, K, G):
    # dp[bit][i]これまでに踏んだ場所がbitであり、現在の場所がiである
    dp = [[float('inf')] * K for i in range(1 << K)]
    dp[1 << sta][sta] = 0

    for bit in range(1, 1 << K):
        if not bit & (1 << sta):
            continue
        # s:現在の場所
        for s in range(K):
            # sを踏んだことになっていなければ飛ばす
            if not bit & (1 << s):
                continue
            # t:次の場所
            for t in range(K):
                # tを過去踏んでいない and s → tへのエッジがある
                if (bit & (1 << t)) == 0:
                    dp[bit|(1 << t)][t] = min(dp[bit|(1 << t)][t], dp[bit][s] + G[s][t])

    return min(dp[-1])

# 任意の地点からスタート
def counter(K, G):
    # dp[bit][i]これまでに踏んだ場所がbitであり、現在の場所がiである
    dp = [[float('inf')] * K for i in range(1 << K)]
    for i in range(K):
        dp[1 << i][i] = 0

    for bit in range(1, 1 << K):
        if not bit:
            continue
        # s:現在の場所
        for s in range(K):
            # sを踏んだことになっていなければ飛ばす
            if not bit & (1 << s):
                continue
            # t:次の場所
            for t in range(K):
                # tを過去踏んでいない and s → tへのエッジがある
                if (bit & (1 << t)) == 0:
                    dp[bit|(1 << t)][t] = min(dp[bit|(1 << t)][t], dp[bit][s] + G[s][t])

    return min(dp[-1])

# ARC056 C - 部門分け

N, K = getNM()
V = [getList() for i in range(N)]
diff = sum([sum(v) for v in V]) // 2

dp = [K] * (1 << N) # 固有値k
dp[0] = 0

# 部分集合を作り、その中の任意の2つを選んであれこれする
for bit in range(1 << N):
    o = [i for i in range(N) if bit & (1 << i)]
    n = len(o)
    for i in range(n):
        for j in range(i + 1, n):
            dp[bit] += V[o[i]][o[j]]

# 部分集合についてさらに２つのグループに分ける
for bit in range(1 << N):
    j = bit # 例: 1010(10)
    while j:
        # 1010と0
        dp[bit] = max(dp[bit], dp[j] + dp[bit ^ j])
        j -= 1 # 1010 → 1001 1だけ減らして数字を変える
        j &= bit # 1010 → 1000 実質引き算 同じ要素があるところまで数字を減らす

print(dp[-1] - diff)

# フラグが立ってないところについて最寄りのフラグを教えてくれる
def close(bit, n):
    # n = bit.bit_length()
    res = [[] for i in range(n)]
    build = -1
    not_build = []
    for i in range(n):
        # フラグが立っている
        if bit & (1 << i):
            build = i
            # 右側のフラグについて
            while not_build:
                p = not_build.pop()
                res[p].append(build)
        else:
            # 左側のフラグについて
            if build >= 0:
                res[i].append(build)
            not_build.append(i)

    return res
