#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

# 0はfalseになる

# lambda式（無名関数)
def func(x, y, z):
    return x + y + z

print(func(2, 3, 4))

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))
