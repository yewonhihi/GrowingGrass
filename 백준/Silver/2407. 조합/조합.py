n, m = map(int, input().split())
up = 1
down = 1

for i in range(m):
    up *= n-i
    down *= (i+1)

print(int(up // down))