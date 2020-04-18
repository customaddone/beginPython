class UnionFind():
    def __init__(self, n):
        # print(uf)
        # 0: [0, 2]
        # 1: [1]...
        self.n = n
        # print(uf.parents)
        # [-1, -1, -1, -1, -1, -1]
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

        # 親に格納された要素の個数をプラス
        self.parents[x] += self.parents[y]
        # 移動先
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 経路格納
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
        
