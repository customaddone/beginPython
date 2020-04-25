# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d
n = int(input())
# 星座
lista = [list(map(int, input().split())) for i in range(n)]
m = int(input())
# 星座候補
listb = [list(map(int, input().split())) for i in range(m)]
# 探索用　b配列のコピー
# 探索時は集合から探すのがポイント
listaltb = []
for i in listb:
    listaltb.append((i[0], i[1]))
# 平行移動量の候補　一つ目の星起点
listmove = []
for i in range(m):
    listmove.append([listb[i][0] - lista[0][0], listb[i][1] - lista[0][1]])
# 星座があるか判定
for move in listmove:
    listjudge = []
    for i in range(n):
        listjudge.append([lista[i][0] + move[0], lista[i][1] + move[1]])
    flag = True
    for i in range(n):
        # listjudgeの要素を集合でまとめ直さないとlistaltb(集合)内にあるかどうか判定されない
        x = listjudge[i][0]
        y = listjudge[i][1]
        if not (x, y) in listaltb:
            flag = False
    if flag:
        print(move[0], end=" ")
        print(move[1])
