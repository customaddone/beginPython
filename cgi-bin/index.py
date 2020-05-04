# https://atcoder.jp/contests/abc034/tasks/abc034_c
w, h = map(int, input().split())
mod = 10 ** 9 + 7

def cmb(x,y):
    r=1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, mod - 2, mod)) % mod
    return r

print(cmb(w + h - 2, h - 1))
