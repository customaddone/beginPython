def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

Q = getN()
que = [getList() for i in range(Q)]

"""
回文である 01010 偶数と奇数に分けられるかも
長さN 転倒数K
転倒数　各1について、その1より右にある0の数の総和
01010 転倒数3
考えるのはN / 2まででいい
i番目に1を置く
左側の1: 今まで置いた0の数 + (今から置いていく0の数 * 2)
右側の1: 今まで置いた0の数
合計:今まで置いた0の数 * 2 + 今から置いていく0の数
= 0の数の合計 * 2

通りの数を考える
dp? 数え上げcombo?
Kの作りかたを考える
0と1の数がわかればどうなる
0 * 0, 1 * 3 111111 (0)
0 * 1, 1 * 2 110011(4), 101101(4), 011110(4)
0 * 2, 1 * 1 100001(4), 010010(4), 001100(4)
0 * 3, 1 * 0 000000 (0)

どのタイミングで0を置くかは関係ない
0と1の組み合わせにより転倒数の個数が決まる
転倒数は1の数 * 0の数（n - 1の数）* 2 2i(n - i) = k
2i ** 2 - 2ni + k = 0
これは偶数の場合
奇数の場合は
最後の一つが0か1か
0の時
各1について転倒数 0の数の合計 * 2 + 1
総和 1の数 * 0の数（n - 1の数） * 2 + 1の数
i(n - i) * 2 + i
i(2n - 2i + 1) = k
2i ** 2 - (2n - 1)i + k = 0
1の時
各1について転倒数 0の数の合計 * 2
+ 中央の1について0の数
総和 1の数 * 0の数（n - 1の数） * 2
2i(n - i) + (n - i)= k
"""

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

# a + b = n
# a * b = kとなるa, bを求める
def binary_combo(n, k):
    left = 0
    right = int(math.sqrt(k)) + 1
    while left <= right:
        mid = (left + right) // 2
        if mid * (n - mid) == k:
            return mid # aの値がかえる(b = n - a)
        elif mid * (n - mid) < k:
            left = mid + 1
        else:
            right = mid - 1
    return False

def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b ** 2 - 4 * a * c) ** (1 / 2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

for n, k in que:
    if k == 0:
        print(2)
        continue
    if n % 2 == 0:
        if k % 2 != 0:
            print(0)
            continue
        res = 0
        n //= 2
        x1, x2 = solv_quadratic_equation(2, -2 * n, -k)
        if isinstance(x1, float) and x1.is_integer() and x1 > 0:
            res += cmb(n, int(x1))
        if isinstance(x2, float) and x2.is_integer() and x2 > 0:
            res += cmb(n, int(x2))
        print(res)
    else:
        res = 0
        n //= 2
        # 中央は0
        x1, x2 = solv_quadratic_equation(2, -(2 * n + 1), k)
        if isinstance(x1, float) and x1.is_integer() and x1 > 0:
            res += cmb(n, int(x1))
        if isinstance(x2, float) and x2.is_integer() and x2 > 0:
            res += cmb(n, int(x2))
        # 中央は1
        x1, x2 = solv_quadratic_equation(2, -(2 * n - 1), k - n)
        if isinstance(x1, float) and x1.is_integer() and x1 > 0:
            res += cmb(n, int(x1))
        if isinstance(x2, float) and x2.is_integer() and x2 > 0:
            res += cmb(n, int(x2))

        print(res)
