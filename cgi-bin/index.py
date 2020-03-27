n = int(input())
time = []
x_axis = []
y_axis = []
ans = 'Yes'
for _ in range(n):
    t, x, y = map(int, input().split())
    time.append(t)
    x_axis.append(x)
    y_axis.append(y)
if (x_axis[0] + y_axis[0] - time[0]) % 2 != 0 or time[0] < x_axis[0] + y_axis[0]:
    ans = 'No'
for i in range(n - 1):
    fortime = abs(time[i + 1] - time[i])
    distance = abs(x_axis[i + 1] - x_axis[i]) + abs(y_axis[i + 1] - y_axis[i])
    if (fortime - distance) % 2 != 0 or fortime < distance:
        ans = 'No'
print(ans)
