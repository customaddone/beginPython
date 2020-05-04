# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d
# H, W 土地の広さ
# K 家建築費用
# V 所持金
H, W, K, V = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

# Aより一回り大きいサイズ
S = [[0] * (W + 1) for i in range(H + 1)]

for i in range(H):
    for j in range(W):
        # 上のAによる増分 + 左のAによる増分を足し合わせてる
        S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + A[i][j]

# 細かく関数を設定
def calc(y1, y2, x1, x2):
    return S[y2][x2] - S[y1][x2] - S[y2][x1] + S[y1][x1]

ans = 0
# i1, i2は縦の大きさ(i2 - i1)
for i1 in range(H):
    for i2 in range(i1 + 1, H + 1):
        # j1, j2は横の大きさ
        # i1, i2を決定した時条件の許す限りj1, j2を動かして大きくする
        j2 = 0
        for j1 in range(W):
            j2 = max(j2, j1)
            while j2 < W and calc(i1, i2, j1, j2 + 1) + (i2 - i1) * (j2 + 1 - j1) * K <= V:
                j2 += 1
            ans = max(ans, (i2 - i1) * (j2 - j1))
print(ans)
