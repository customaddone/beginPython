#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

# 0はfalseになる
x = 9
y = 5
if x < 10:
    def times(x, y):
        return x * y
else:
    def times(x, y):
        return x + y

print(times(x, y))
