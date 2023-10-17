import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

sushi.extend(sushi[0:k-1])

max_cnt = 0

for i in range(n):
    temp = set(sushi[i:i+k])
    temp.add(c)
    cnt = len(temp)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)