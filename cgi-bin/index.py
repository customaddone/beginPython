import sys

class LCA(object):
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.go = [] # 行きがけ
        # self.go_dict = {}
        self.back = [] # 帰りがけ
        self.back_dict = {}
        self.bfs()
        self.doubling()

    def bfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def dfs(self, u, p):
        # self.go_dict[u] = len(self.go)
        self.go.append(u)
        for v in E[u]:
            if v != p:
                self.dfs(v, u)
        self.back_dict[u] = len(self.back)
        self.back.append(u)

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):  # depthの差分だけuを遡らせる
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v: return u  # 高さ揃えた時点で一致してたら終わり

        for i in range(self.logn - 1, -1, -1):  # そうでなければ上から二分探索
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

    def distance(self, u, v):
        return lca.depth[u] + lca.depth[v] - 2 * lca.depth[lca.get(u, v)]

    # dfsの帰りがけ順の列があれば深さが深い順に各頂点をマージする方法を教えてくれる
    # [[マージ元1, マージ元2, マージ先],...]
    def unite(self, ar):
        # dfsの行きがけ順にソート
        v_l = [[self.back_dict[v - 1], v - 1] for v in ar]
        v_l.sort(reverse = True)
        bef = []
        aft = [v[1] for v in v_l] # popできるよう逆にする
        res = []

        while len(aft) > 1:
            now = aft.pop()
            while bef and lca.depth[lca.get(bef[-1], now)] >= lca.depth[lca.get(now, aft[-1])]:
                res.append([bef[-1], now]) # 記録1 マージ元
                now = lca.get(bef.pop(), now) # nowとbef[-1]を統合して新しい点を作成
                res[-1].append(now) # 記録2 マージ先

            # 一旦保留
            bef.append(now)

        # 残った奴をマージしていく
        now = aft[0]
        while bef:
            res.append([bef[-1], now])
            now = lca.get(bef.pop(), now) # nowとbef[-1]を統合して新しい点を作成
            res[-1].append(now)

        return res

N = int(input())
E = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

lca = LCA(E)
lca.dfs(0, -1)
Q = int(input())

for _ in range(Q):
    k, *v = list(map(int, input().split()))
    cnt = 0
    for a, b, _ in lca.unite(v):
        cnt += lca.distance(a, b)
    print(cnt)
