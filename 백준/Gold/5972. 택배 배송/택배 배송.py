import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [float("inf")] * (n + 1)
q = []

heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for b, c in graph[now]:
        cost = distance[now] + c
        if cost < distance[b]:
            distance[b] = cost
            heapq.heappush(q, (cost, b))

print(distance[n])