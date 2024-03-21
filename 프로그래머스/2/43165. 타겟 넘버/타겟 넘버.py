def solution(numbers, target):
    n = len(numbers)
    global answer
    answer = 0
    
    if target == sum(numbers):
        return 1
    
    def dfs(i, total):
        global answer
        if i == n:
            if total == target:
                answer += 1
        else:
            dfs(i+1, total + numbers[i])
            dfs(i+1, total - numbers[i])
    
    dfs(0,0)
    
    return answer