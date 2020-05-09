# 組み合わせの数を求める
# → DP?
# but 重複無しで３つの数を選び
# 一つ目の数i,二つ目の数jを決めると3つ目はx - i - j になる
# x - i - j がj ~ xの中にあるか
# 選択する数が二つなら二重ループでいける

N, X = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        k = X - i - j
        if j < k <= N:
            ans += 1
print(ans)
# 1 ~ Nから○個選んでXを作る問題はだいたいDP
# 個数制限あり部分和問題再帰
# 個数制限亜ありの場合再帰でやるとややめんどい
N, X = map(int, input().split())
lista = [i for i in range(1, N + 1)]
dp = [[0] * (X + 1) for i in range(N)]
ans = 0
# 引数にplusが増える
def rec_memo(i, plus, sum):
    global ans
    if i == N or plus == 3:
        if plus == 3:
            ans += (sum == X)
    elif X - sum < lista[i]:
        rec_memo(i + 1, plus, sum)
    else:
        rec_memo(i + 1, plus, sum)
        rec_memo(i + 1, plus + 1, sum + lista[i])
rec_memo(0, 0, 0)
print(ans)
