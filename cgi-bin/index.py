#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
# https://qiita.com/KoyanagiHitoshi/items/32dc42d8c5ee75339e54

# iは使わなくていい（ただ繰り返しをするためのi）()
n, k, x, y = [int(input()) for i in range(4)]
# ここのmaxの使い方覚える
print(n * x + max(n - k, 0) * y)
