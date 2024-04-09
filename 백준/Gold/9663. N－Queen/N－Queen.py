def nqueen(idx):
    global cnt
    if idx == n:
        cnt += 1
        return
    else:
        for i in range(n):
            chess[idx] = i
            if isPromising(idx):
                nqueen(idx + 1) 

def isPromising(idx):
    for i in range(idx):
        if chess[idx] == chess[i] or idx - i == abs(chess[idx] - chess[i]):
            return False
    
    return True

import sys

input = sys.stdin.readline
n = int(input())
chess = [0 for _ in range(n)]
cnt = 0

nqueen(0)
print(cnt)