# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B&lang=ja
# 10 ** 9 + 7は素数
# 10 ** 9 + 7とmが互いに素なら使える
# a と z が互いに素のとき
# x == y (mod z)なら
# ax == ay (mod z)
# 10000 == 1924 (mod 2019) * 10 =
# 100000 == 19240 (mod 2019)
# 100000 == 1060 (mod 2019)

m, n = map(int, input().split())
mod = 10 ** 9 + 7
ans = 1
for i in range(n):
    ans *= m
    ans %= mod
print(ans)

# a / b (mod m)の求め方が a * (1 / b (mod m)) % m
# pow(b, m - 2, m)で 1 / b (mod m) が求まる
# k = 64 l = 16のとき
# 64 / 16 = 4 (mod 4)
# 64 * pow(16, 5, 7) % 7 = 4
k, l = map(int, input().split())
mod = 7
print(k * pow(l, mod - 2, mod) % mod)
