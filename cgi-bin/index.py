#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐

# 下のinputの仕方覚える
n, k, x, y = (int(input()) for i in range(4))
print(k * x + max(n - k, 0) * y)
