import heapq

N,M = map(int, input().split())
A = list(map(lambda x:int(x) * (-1), input().split())) #-1倍してからリストに格納
heapq.heapify(A) #優先度付きキューに変換

for _ in range(M):
    # 一回正に戻して
    max_value = heapq.heappop(A) * (-1) #最大値の取得
    # また負に
    heapq.heappush(A, (max_value // 2) * (-1)) #半額にして-1倍してからキューに戻す

print((-1) * sum(A))
