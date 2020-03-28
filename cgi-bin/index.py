# Xについて、2~Xの範囲で割り切れる数があるか調べる
# なければelseに飛んでprint break
X = int(input())
while True:
    for x in range(2,X):
        if X%x==0:
            break
    else:
        print(X)
        break
    X += 1
