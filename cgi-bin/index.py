from bisect import bisect_left
n = int(input())
lista = [int(input()) for i in range(n)]

def lis(A):
    L = [A[0]]
    for a in A[1:]:
        # Lの末尾よりaが大きければ増加部分を拡張できる
        if a > L[-1]:
            # 前から順にLに追加していく
            L.append(a)
        else:
            """
            [3]
            [3, 7]
            末尾より小さい数字が来た場合は適当にすっ飛ばす
            末尾を小さくできる場合のみ末尾を交換する
            [3, 4]
            [1, 4]
            [1, 4]
            [1, 4, 6]
            """
            L[bisect_left(L, a)] = a
    # Lの配列の長さは求まる
    # Lの中身はデタラメ
    return len(L)
print(lis(lista))
