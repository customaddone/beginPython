import math
import itertools
n = int(input())
lista = []
anslist = 0
for i in range(n):
    x, y = map(int, input().split())
    lista.append([x, y])
# permutasion 引数１つのみ
# len(lista)!通り出る
for i in itertools.permutations(lista):
    for j in range(n - 1):
        anslist += math.sqrt((i[j + 1][0] - i[j][0]) ** 2 + (i[j + 1][1] - i[j][1]) ** 2)
        #if i != j:
            #print([lista[i], lista[j]])
            #anslist += math.sqrt((lista[j][0] - lista[i][0]) ** 2 + (lista[j][1] - lista[i][1]) ** 2)
# math.factorial 階乗
print(anslist / math.factorial(n))
