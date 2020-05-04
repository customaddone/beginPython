# https://www.ioi-jp.org/joi/2009/2010-ho-prob_and_sol/2010-ho.pdf#page=2
# MLE対策
import sys
def input(): return sys.stdin.readline()[:-1]

n, m = map(int, input().split())
lista = [int(input()) for i in range(n - 1)]
listb = [int(input()) for i in range(m)]
listsum = [0]

for i in range(n - 1):
    # 宿場街1からの距離
    listsum.append(listsum[i] + lista[i])

now = 0
sum = 0
for i in listb:
    # 逆行する時はマイナスになるのでabsする
    # modを忘れるな
    sum += (abs(listsum[now + i] - listsum[now]) % (10 ** 5))
    now += i
print(sum % (10 ** 5))
