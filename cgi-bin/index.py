n = int(input())
list = []
digit = 7
i = 0
while n != 0:
    list.insert(0, str(n % digit))
    n //= digit
    i += 1
print(''.join(list))
