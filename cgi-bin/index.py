#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

# 0はfalseになる

#map関数はシーケンスの要素一つ一つに関数を実行する
#map(function, sequence_object)
a, b = map(len,input().split())
print(a, b)

original_list = list(range(10))
mapped_list = map(lambda x: x ** 2, original_list)
print(list(mapped_list))
