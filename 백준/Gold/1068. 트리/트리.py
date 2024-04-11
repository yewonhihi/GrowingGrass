import sys

input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
delete = int(input())
root = 0

tree = [[] for _ in range(n)]
leaf = 0

for i in range(n):
    p = parents[i]
    if p == -1:
        root = i
    elif i != delete:
        tree[p].append(i)

def dfs(node):
    global leaf
    
    if len(tree[node]) == 0:
        leaf += 1
    else:
        for i in tree[node]:
            dfs(i)

if delete != root:
    dfs(root)

print(leaf)