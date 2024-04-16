import sys

input = sys.stdin.readline

n = int(input())
village = []
people = 0

for _ in range(n):
    x, a = map(int, input().split())
    village.append((x, a))
    people += a

village.sort(key = lambda x : x[0])

cnt = 0
for x, a in village:
    cnt += a
    if cnt >= people/2:
        print(x)
        break