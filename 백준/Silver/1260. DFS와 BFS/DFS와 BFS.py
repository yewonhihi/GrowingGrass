from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=" ")
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)
            
visitedD = [False] * (n+1)
visitedB = [False] * (n+1)

def bfs(graph, v, visited):
    q = deque([v])
    visitedB[v] = True
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, v, visitedD)
print("")
bfs(graph, v, visitedB)