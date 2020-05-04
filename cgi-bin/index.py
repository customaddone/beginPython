
n = int(input())
k = int(input())

mod = 10 ** 9 + 7

def cmb(x,y):
    r=1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, mod - 2, mod)) % mod
    return r
# https://mathtrain.jp/tyohukuc
# 重複組み合わせ
# 仕切りの考え方
print(cmb(n + k - 1, k))
