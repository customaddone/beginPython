import bisect

n = int(input())
m = int(input())
lista = []
k = [i for i in range(1,1000)]
for i in k:
    for j in k:
        lista.append(i + j)
for i in lista:
    # リストを伸ばしてbisect
    # m - (i + j) を満たすものが(i + j)の集合の中にあるか
    if bisect.bisect_left(lista, m - i):
        print(True)
        break
else:
    print(False)
