n = 10
p = [[3, 7], [2, 8]]
lista = [0] * (n + 1)
# for i in p:
    # for j in range(i[0], i[1] + 1):
        # lista[j] += 1
# print(lista)
listb = [0] * (n)
for i in p:
    listb[i[0] - 1] += 1
    listb[i[-1] - 1] -= 1
listc = [0]
for i in range(n - 1):
    listc.append(listb[i] + listc[i])
print(listc)
