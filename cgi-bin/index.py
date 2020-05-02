# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
n = 14
w = [8, 7, 1, 4, 3, 5, 4, 1, 6, 8, 10, 4, 6, 5]
# 未開発の部分は-1
dp = [[-1] * (n + 1) for i in range(n + 1)]

def rec(l, r):
    # dp[l][r] 区間(l , r)で取り除くことのできるブロックの数
    if dp[l][r] != -1:
        return dp[l][r]

    if abs(l - r) <= 1:
        return 0

    res = 0

    # w[0] - w[13] <= 1 and l + 1 ~ r - 1間のだるまを全て飛ばせる
    # 下でやる区間dpのどこかで反応
    if abs(w[l] - w[r - 1]) <= 1 and rec(l + 1,r - 1) == r - l - 2:
        # rec(l + 1,r - 1)が上の条件を満たすとき res = r - l - 2
        res = r - l
    # 区間dp
    for i in range(l + 1, r):
        res = max(res, rec(l, i) + rec(i, r))
    dp[l][r] = res
    return res
# 便宜上n = 14だけど
print(rec(0, n))
