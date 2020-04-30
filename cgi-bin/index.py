n = int(input())

first, *a, result = map(int, input().split())
lista = list(a)
listsum = [0]
for i in range(n - 2):
    listsum.append(lista[i] + listsum[i])
# aの1 / 2 + first = resultになればいい
target = sum(lista) // 2 + (result - first) // 2

dp = [[0] * (target + 1) for i in range(n - 1)]
dp[0][0] = 1
# 最初と最後を取り除いているのでn - 2
for i in range(n - 2):
    for j in range(target + 1):
        # プラス要素:first + j(今まで選択した数の合計)
        # マイナス要素: listsum[i] - j
        # first + j - (listsum[i] - j)が0未満だったり20を越えればドボン
        if 2 * j < listsum[i] - first:
            dp[i][j] = 0
        if 2 * j > 20 + listsum[i] - first:
            dp[i][j] = 0
        # あとは普通の個数制限あり重複なしナップサックdp
        if lista[i] <= j:
            dp[i + 1][j] = dp[i][j - lista[i]] + dp[i][j]
        else:
            dp[i + 1][j] =  dp[i][j]
print(dp[n - 2][target])
