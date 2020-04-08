n = int(input())
a = list(map(int, input().split()))
counter = 0
# 問題文、怪文書すぎて好き
for i in a:
    while True:
        if i % 2 == 0:
            i -= 1
            counter += 1
            continue
        elif i % 3 == 2:
            i -= 1
            counter += 1
            continue
        else:
            break
print(counter)
