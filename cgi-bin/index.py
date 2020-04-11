def rec_memo(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec_memo(i + 1, j)
    else:
        # 次の商品を取った場合の最大値と取らない場合の最大値を比べる
        res = max(rec_memo(i + 1, j), rec_memo(i + 1, j - w[i]) + v[i])
        print([i, j, res])

    dp[i][j] = res
    return res

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]

W = 5
dp = [[0] * (W + 1) for i in range(n + 1)]  # メモ化テーブル
# i = 3 5余した状態での最大値は2（最後の商品をとった場合）
# i = 3 2余した状態での最大値は2
# i = 2 5余した状態での最大値は6
print(rec_memo(0, W))
