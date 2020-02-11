#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print M[0]

# 各一段目の配列の２つめの要素を取り出す
# 全ての要素に対してforが適用される
col1 = [row[1] for row in M]
print col1

col2 = [row[0] for row in M]
print col2

col3 = [object[1] for object in M if object[1] % 2 == 0]
print col3

# 対角に要素を取り出す
col4 = [M[i][i] for i in [0, 1, 2]]
print col4

col5 = [c * 2 for c in 'spam']
print col5
