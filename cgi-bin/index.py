# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja
# 個数制限なし重複ありナップサック
n, w = map(int, input().split())
val = []
wei = []
for i in range(n):
    v1, w1 = map(int, input().split())
    val.append(v1)
    wei.append(w1)
dp = [0] * (w + 1)
# 個数制限解除のためiが消える
def rec_memo(j):
    if dp[j]:
        return dp[j]
    res = 0
    for r in range(n):
        if wei[r] <= j:
            res = max(res, rec_memo(j - wei[r]) + val[r])
    return res
print(rec_memo(w))
