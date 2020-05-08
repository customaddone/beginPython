from collections import defaultdict

def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return imid
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False

N = int(input())
A = [int(input()) for i in range(N)]

lista = set()
for i in A:
    lista.add(i)
# setは勝手にsortしてくれる訳ではない
lista = sorted(list(lista))

listb = []
for i in A:
    listb.append(binary_search_loop(lista, i))
for i in listb:
    print(i)
