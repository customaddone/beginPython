n = int(input())
s = input()
cnt = 0

one = [0 for i in range(10)]
two = [0 for i in range(100)]
thr = [0 for i in range(1000)]

#1 ~ 1000内でsの各文字についてループする
#1 ~ 1000を全通り調べる
for i in range(1000):
    flag = 0
    # iが1から1000までのループ、stが入力した数字の一部
    for st in s:
        if flag = 0 and s == str(i // 100):
            flag = 1
        # 192 % 100 = 92 92 // 10 = 9
        elif flag == 1 and s == str((i % 100) // 10)):
            flag = 2
        elif flag == 2 and s == str(i % 10):
            flag = 3
            break
    if flag == 3:
        ans += 1
"""
#[0]224から回してできるのは
#0[2]24から回してできるのは.,..
for st in s:
    # tinがインデックス、tisが実際の数字
    for tin, tis in enumerate(two):
        if tis == 1:
            # '92' + '2' = 922
            # thr[922] += 1
            thr[int(str(tin) + st)] = 1

    for oin, ois in enumerate(one):
        # ②①の次のループで2つ目に繋げる数字も決めとく
        if ois == 1:
            # '0' + '2' = 02
            # two[2] = 1
            two[int(str(oin) + st)] = 1
    # ①stを+=1する
    # ③②と同時にまた新しい1桁目を+=1する
    one[int(st)] = 1

print(sum(thr))
"""

"""
def my_index(l, x, default=-1):
    if x in l:
        return l.index(x)
    else:
        return default

for i in range(10):
    indexi = my_index(s, str(i))
    if indexi >= 0:
        for j in range(10):
            indexj = my_index(s[indexi + 1:], str(j))
            if indexj >= 0:
                for k in range(10):
                    indexk = my_index(s[indexi + indexj + 2:], str(k))
                    if indexk >= 0:
                        cnt += 1
print(cnt)
"""
