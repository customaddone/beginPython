# https://www.ioi-jp.org/joi/2006/2007-ho-prob_and_sol/2007-ho.pdf#page=5
n = int(input())
lista = []
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    lista.append((x, y))
# 早くしろ
listb = set(lista)

for i in range(n):
    for j in range(i + 1, n):
        # 要素抽出のため配列は残しておく
        px1, py1 = lista[i][0] - (lista[i][1] - lista[j][1]), lista[i][1] + (lista[i][0] - lista[j][0])
        px2, py2 = lista[j][0] - (lista[i][1] - lista[j][1]), lista[j][1] + (lista[i][0] - lista[j][0])
        # setにするとリスト内探索がクソ早くなる
        if (px1, py1) in listb and (px2, py2) in listb:
            matl = (px1 - px2) ** 2 + (py1 - py2) ** 2
            ans = max(ans, matl)
print(ans)
