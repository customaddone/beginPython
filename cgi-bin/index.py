#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

# 0はfalseになる
from functools import reduce

counters = [1, 2, 3]
print(list(map((lambda x: x + 10), counters)))

# filter 特定の条件に合うものだけを抽出する
print(list(filter((lambda x: x > 2), counters)))

# reduce 順繰りに実行していくもの
# rangeは0からスタート
# range(1, 5)は[1, 2, 3, 4]
ren = reduce((lambda x, y: x * y), range(1, 5))
print(ren)
