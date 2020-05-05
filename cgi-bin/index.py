# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    # これ追加
    def count_group(self):
        return len({self.find(x) for x in range(n)})

n, m = map(int, input().split())
lista = [list(map(int, input().split())) for i in range(m)]

cnt = 0
# 自分以外の道を全て繋いで一つのグループになるか（自分を繋がなくてもグループが一つにまとまるか）
# を調べる
for i in range(m):
    # UnionFindをm回生成する
    U = UnionFind(n)
    # 自分以外の道を全てunionしていく
    for j in range(m):
        if i == j:
            continue
        a, b = lista[j]
        U.union(a - 1, b - 1)
    # 繋ぎ終わったら全体でグループが１つにまとまっているか調べる
    if U.count_group() > 1:
        cnt += 1
print(cnt)
