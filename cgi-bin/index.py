# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2199&lang=jp
n, m = map(int, input().split())
# コードブック
listc = [int(input()) for i in range(m)]
# 入力信号
listx = [int(input()) for i in range(n)]

dp = [[float('inf')] * 256 for i in range(n + 1)]
dp[0][128] = 0
# 数字を0~255内で丸める関数
def pulse(n):
    if n <= 0:
        return 0
    elif 255 <= n:
        return 255
    else:
        return n
# 信号の数
# ループの数を１とか２にして刻んでいって不具合を探す
for i in range(n):
    # 信号の数値
    for j in range(256):
        # コードブックの数
        for k in range(m):
            index = pulse(j + listc[k])
            dp[i + 1][index] = min(dp[i + 1][index], dp[i][j] + (listx[i] - index) ** 2)
print(min(dp[-1]))
