from copy import deepcopy
n = 5
x = 9

lista = [i for i in range(1, n + 1)]
def dfs(i, numbers):
    if len(numbers) == 3:
        print(numbers)
        return sum(numbers) == x
    elif i == n:
        return 0
    newnumbers = deepcopy(numbers)
    newnumbers.append(lista[i])
    return dfs(i + 1, numbers) + dfs(i + 1, newnumbers)
print(dfs(0, []))
