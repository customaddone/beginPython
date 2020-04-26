#https://atcoder.jp/contests/abc002/tasks/abc002_4
n, m = map(int, input().split())
lista = [list(map(int, input().split())) for i in range(m)]
maxans = 0

"""
5 3
5人の議員と3つの人間関係がある
1 2
2 3
1 3
[[1, 2], [2, 3], [1, 3]]
議員1と2が知り合い
議員2と3が知り合い
議員1と3が知り合い
1と2と3が知り合い = 111
101と110と011がある
"""
listalta = set([(1 << (i[0] - 1)) | (1 << (i[1] - 1)) for i in lista])
# n, n - 1の順に
# nCrの議員の選び方を全探索
# もし条件が適合していればそのrが正解
# という方法もある

# 全ての状態
for bit in range(1 << n):
    # 状態a 01001
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            # 任意の2箇所について1を立てる
            # judge:01001と00101の共通部分 = 00001
            judge = bit & ((1 << i) | (1 << j))
            # judgeに1が２つ立っているか
            if judge == ((1 << i) | (1 << j)):
                # 立っていればそれがlistaltaにあるか
                if not judge in listalta:
                    # 1つでもなければFalse
                    flag = False
    if flag:
        ans = bin(bit).count("1")
        maxans = max(maxans, ans)
print(maxans)
