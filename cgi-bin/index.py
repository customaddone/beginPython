# https://atcoder.jp/contests/abc106/tasks/abc106_d
# 区間が出る問題は累積和を疑おう
N, M, Q = map(int, input().split())

# l から rまで行く鉄道の数
lr = [[0 for i in range(N + 1)] for j in range(N + 1)]
# l から r以前のどこかまで行く鉄道の数
imos = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    l, r = map(int, input().split())
    lr[l][r] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        imos[i][j] = imos[i][j-1] + lr[i][j]
res = []
for i in range(Q):
    ans = 0
    p, q = map(int, input().split())
    # imos[p][q]: pからq以前のどこかまで
    # imos[p + 1][q]: p + 1からq以前のどこかまで...
    for i in range(p, q + 1):
        ans += imos[i][q]
    res.append(ans)

for row in res:
    print(row)
