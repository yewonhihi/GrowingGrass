def solution(m, n, puddles):
    loc = [[1 for _ in range(m)] for _ in range(n)]
    
    for x, y in puddles:
        if x == 1: # 바깥쪽 웅덩이
            for i in range(y-1, n):
                loc[i][0] = 0
        elif y == 1:
            for i in range(x-1, m):
                loc[0][i] = 0
        else: # 안쪽 웅덩이
            loc[y-1][x-1] = 0
    
    for x in range(1, m):
        for y in range(1, n):
            if loc[y][x] == 0: # 웅덩이
                continue
                
            loc[y][x] = loc[y-1][x] + loc[y][x-1]
            
    return loc[n-1][m-1] % 1000000007