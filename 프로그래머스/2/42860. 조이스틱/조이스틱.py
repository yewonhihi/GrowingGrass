def solution(name):
    cursor = float('inf')
    cnt = 0 # 알파벳 조작 개수
    target = []
    
    for i, j in enumerate(name):
        o = ord(j)
        cnt += min(o - 65, 91 - o) # A: 65, Z: 90
        
        if o != 65:
            target.append(i)
    
    n = len(name)
    
    if len(target) == n: # A가 없을 때
        return cnt + n - 1
    
    if len(target) == 0: # A만 있을 때
        return 0

    cursor = min(cursor, target[-1])
    cursor = min(cursor, n - target[0])
    
    for i in range(len(target) - 1):
        cursor = min(cursor, 2 * target[i] + (n - target[i+1]))
        cursor = min(cursor, target[i] + 2 * (n - target[i+1]))

    return cnt + cursor