#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

D = { 'food': 'Spam', 'quantity': 4, 'color': 'pink' }

print D['food']

# quantityに対応する要素に１を加える
print D['quantity'] + 1

# 現在存在しないキーを指定して入れることもできる
M = {}
M['name'] = 'bob'
M['job'] = 'dev'
M['age'] = 40
print M
