import sys

input = sys.stdin.readline

n, total = map(int, input().split())

drive = [i for i in range(total+1)]
shortcuts = []

for _ in range(n):
    way = tuple(map(int, input().split()))
    shortcuts.append(way)

shortcuts.sort(key=lambda x:x[1])

for start, end, length in shortcuts:
    if end > total:
        continue

    if drive[start] + length < drive[end]:
        gap = drive[end] - (drive[start] + length)

        for cur in range(end, total+1):
            drive[cur] = drive[cur] - gap

print(drive[total])