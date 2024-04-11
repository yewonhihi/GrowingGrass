import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]
q = deque()

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent[1] = 0
q.append(1)

while q:
    cur = q.popleft()
    for i in tree[cur]:
        if not parent[i]:
            parent[i] = cur
            q.append(i)
 
for i in range(2, n+1):
    print(parent[i])   