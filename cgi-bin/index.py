# https://atcoder.jp/contests/abc142/tasks/abc142_d
import math
# 公倍数を列挙する
def make_divisors(m, n):
    divisors = []
    numi = min(m, n)
    numa = max(m, n)
    for i in range(1, int(math.sqrt(numi)) + 1):
        if numi % i == 0:
            # 18 = 2 * 9 の2の方
            if numa % i == 0:
                divisors.append(i)
            # √nで無い数についてもう一個プラス
            # 18 = 2 * 9 の9の方
            if i != numi // i and numa % (numi // i) == 0:
                divisors.append(numi // i)
    return sorted(divisors)

a, b = map(int, input().split())
lista = make_divisors(a, b)
listb = [1]
# listaの先頭の１を削除
lista.pop(0)
# エラストテネスの篩の要領
# 先頭の数をlistbに追加
# 先頭の数＋先頭の数の倍数を削除
# これをlistaが消滅するまで繰り返す
while len(lista) > 0:
    listb.append(lista[0])
    lista = [i for i in lista if i % lista[0] != 0]
print(len(listb))
