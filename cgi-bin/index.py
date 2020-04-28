# https://www.ioi-jp.org/joi/2007/2008-ho-prob_and_sol/2008-ho.pdf#page=6
import bisect
from array import array

n, m = map(int, input().split())
p =[int(input()) for i in range(n)]
p.append(0)
lista = array("i")
ans = 0

# 蟻本のくじ引き問題まんま
for i in range(n + 1):
    for j in range(i, n + 1):
        lista.append(p[i] + p[j])
# mがとても小さいときm - lista[i]がマイナスになる
# bisect.bisect_right(lista, m - lista[i]) - 1となりlista[-1] = listaの一番大きい数字になる
# ため、listaの先頭に小さい数字を挟む
lista.append(-10**9)
lista = sorted(lista)
for i in range(len(lista)):
    # bisect_rightは重複があった場合に右側のインデックスを取ってくれる
    # lista = [6, 12, 17, 18, 18, 23, 24, 28, 29, 30]
    # i = 17のとき
    # bisect_right(lista, i) = 3
    # lista[bisect.bisect_right(lista, m - lista[i]) - 1] = 17
    # これがbisect_leftだと12になってしまう
    ans = max(ans, lista[i] + lista[bisect.bisect_right(lista, m - lista[i]) - 1])
print(ans)
