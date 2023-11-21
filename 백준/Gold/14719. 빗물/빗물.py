import sys

input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

rain = 0

for n in range(1, h+1):
    target = [i for i, value in enumerate(blocks) if value >= n]
    if len(target) > 1:
        for j in range(len(target)-1):
            rain += (target[j+1] - target[j] - 1)

print(rain)