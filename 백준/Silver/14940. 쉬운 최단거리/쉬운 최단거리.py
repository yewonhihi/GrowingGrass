import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

land = []

que = deque([])
visited = [[False]*m for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    land.append(temp)
    if 2 in temp:
        target = temp.index(2)
        land[i][target] = 0
        visited[i][target] = True
        que.append((i, target))

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while que:
    nx, ny = que.popleft()
    value = land[nx][ny] + 1
    for dx, dy in direction:
        x = nx + dx
        y = ny + dy
        if 0 <= x < n and 0 <= y < m and not visited[x][y]:
            if land[x][y] == 1:
                que.append((x, y))
                land[x][y] = value
                visited[x][y] = True
            elif land[x][y] == 0:
                visited[x][y] = True

for x in range(n):
    for y in range(m):
        if not visited[x][y] and land[x][y] == 1:
            land[x][y] = -1
        
        print(land[x][y], end=' ')
    
    print("")