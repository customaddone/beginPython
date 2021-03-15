# mod不使用ver
def cmb_1(n, r):
    r = min(n - r, r)
    if (r < 0) or (n < r):
        return 0

    if r == 0:
        return 1

    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

# 10
print(cmb_1(5, 3))

# mod使用ver
# nが大きい場合に
def cmb_2(x,y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, mod - 2, mod)) % mod
    return r

# 10
print(cmb_2(5, 3))

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod
# 120
print(cmb(10, 3))

lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

# 階乗
def factorial(n, r):
    if (r < 0) or (n < r):
        return 0
    return fact[n] * factinv[n - r] % mod

# print(factorial(5, 3))

# 重複組み合わせ
# 10個のものから重複を許して3つとる
print(cmb_1(10 + 3 - 1, 3))

# modが素数じゃない時
def cmb_compose(n, k, mod):
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, k + 1):
            # nCk = n - 1Ck - 1 + n - 1Ck
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod

    return dp[n][k]

print(cmb_compose(10, 3, 50))

n = 7
r = 4

# n個の数字をr個に分割する方法
# nCr通り出ます
def comb_pow(i, array, n, r):
    global cnt
    if i == r:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = -1
    if len(array) > 0:
        last = array[-1]

    for j in range(last + 1, n):
        new_array = array + [j]
        comb_pow(i + 1, new_array, n, r)

comb_pow(0, [], n, r)

po = 3
expo = 2

# po ** expoでループ
# po^expo通り出ます
def four_pow(i, array, p, e):
    global cnt
    if i == e:
        print(array)
        return
    for j in range(p):
        new_array = array + [j]
        four_pow(i + 1, new_array, p, e)
four_pow(0, [], po, expo)

n = 7
r = 4

# n個の数字を重複を許してr個に分割する方法
# nHr通り出ます
def comb_pow(i, array, n, r):
    global cnt
    if i == r:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = -1
    if len(array) > 0:
        last = array[-1]

    for j in range(last, n):
        new_array = array + [j]
        comb_pow(i + 1, new_array, n, r)

comb_pow(0, [], n, r)
