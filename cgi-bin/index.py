#https://atcoder.jp/contests/abc134/tasks/abc134_d
n = int(input())
a = [-1] + [int(i) for i in input().split()]
# 影響しないとこからやっていく
# ボール用リスト
b = [0 for i in range(n + 1)]
# [::-1]つけて逆順から
for i in range(1, n + 1)[::-1]:
    tmp = 0
    # i * 2, i * 3...
    # これ覚える
    for j in range(2 * i, n + 1, i):
        # iの倍数のボールを全て足す
        tmp += b[j]
    # もしtmpの合計とa[i]が一致しなかったら
    if tmp % 2 = a[i]:
        # i * 1にボールを入れる
        b[i] = 1
ans=[]
for i in range(N+1):
    if b[i]==1:
        ans.append(str(i))
print(len(ans))
print(" ".join(ans))
