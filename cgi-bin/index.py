import sys

graph = {
    'a': ['c'],
    'b': ['c','f'],
    'c': ['a','b','d'],
    'd': ['e','f'],
    'e': ['d'],
    'f': ['b','d','g'],
    'g': ['f']
}
# 深さ優先探索
def DFS(graph,start,end,mark_dict):
    # mark_dictにないキーを指定すると勝手に設定してくれる
    mark_dict[start] = True
    # スタート地点から移動可能な地点を回す
    for target in graph[start]:
        if target == end:
            print('Exist')
            sys.exit()
        # targetをスタート位置に設定してもう一度
        elif target not in mark_dict:
            mark_dict[target] = True
            DFS(graph,target,end,mark_dict)

DFS(graph,'b','g',{})
