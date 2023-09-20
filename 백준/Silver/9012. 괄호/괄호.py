import sys

n = int(input())
result = []


for _ in range(n):
    count = 0
    par_str = str(sys.stdin.readline().strip())
    for s in par_str:
        if s == '(': count += 1
        if s == ')': count -= 1
        if count < 0:
            break
    if count == 0: result.append('YES')
    else: result.append('NO')


print(*result, sep='\n')