#!/usr/bin/python
# coding: UTF-8
col = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ifを後ろに繋げることでfilterできる
col2 = [row[0] for row in col if row[0] % 2 == 0]
print(col2)
