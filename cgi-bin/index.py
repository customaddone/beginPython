#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

D = { 'a': 1, 'b': 2, 'c': 3}

Ks = D.keys()
print Ks
Ks.sort() #sortは破壊的メソッド　戻り値はなし
print Ks

for key in Ks: print key, '=>', D[key]
