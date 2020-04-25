n = int(input())
s = input()
lista = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            str = s[i] + s[j] + s[k]
            if not str in lista:
                lista.append(str)
print(len(lista))
