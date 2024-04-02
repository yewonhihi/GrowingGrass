import sys

input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))
gap = []

for i in range(n-1):
    gap.append(heights[i+1] - heights[i])
    
gap.sort()
cost = 0

for i in range(n-m):
    cost += gap[i]

print(cost)