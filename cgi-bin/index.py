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
        # 一番下の桁
        if flag == 0 and st == str(i // 100):
            flag = 1
        # 192 % 100 = 92 92 // 10 = 9
        elif flag == 1 and st == str((i % 100) // 10):
            flag = 2
        elif flag == 2 and st == str(i % 10):
            flag = 3
            break
    if flag == 3:
        cnt += 1
print(cnt)
