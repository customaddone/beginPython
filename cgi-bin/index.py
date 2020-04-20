from operator import mul
from functools import reduce

def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

'''
５行目:5C3 → 5C2にする
６行目:5C5 = 1
７行目:
reduce:第２引数の配列の中身を第１引数の関数で順々に実行していく
mul:i * i + 1
over 5 * 4 * 3
under 3 * 2 * 1
'''
