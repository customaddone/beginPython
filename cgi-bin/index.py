# https://atcoder.jp/contests/abc128/tasks/abc128_c
n, m = map(int, input().split())
lista = []
for i in range(m):
    # s:判定に使用するスイッチ
    k, *s, = map(int, input().split())
    lista.append(list(s))
# p:2で割った時の余りが等しいと点灯
# 全てのpについて成り立たせよう
p = list(map(int, input().split()))

#p[0]について成り立たせよう
sumans = 0
# 全ての状態
for bit in range(1 << n):
    # 任意の状態aの中
    # 全ての電球について判定
    for i in range(m):
        sum = 0
        # 電球aについて判定
        for j in lista[i]:
            if bit & (1 << (j - 1)):
                sum += 1
        # 1つの電球でもつかないものがあればbreak
        # breakうまく使おう
        if sum % 2 != p[i]:
            break
    else:
        sumans += 1
print(sumans)
