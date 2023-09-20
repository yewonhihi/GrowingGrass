import sys
from collections import deque

n = int(input())
ex = sys.stdin.readline().rstrip()
value = []
q = deque()

for i in range(n):
    value.append(input())

for e in ex:
    if e in ('*', '+', '/', '-'):
        num1 = q.pop()
        num2 = q.pop()
        result = eval(str(num2)+e+str(num1))
        q.append(result)
    else:
        num = value[ord(e) - 65]
        q.append(num)

print(f'{q.pop():.2f}')