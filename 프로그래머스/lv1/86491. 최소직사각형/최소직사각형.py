def solution(sizes):
    max_1 = 0
    max_2 = 0
    
    for w, h in sizes:
        max_1 = max(max_1, max(w, h))
        max_2 = max(max_2, min(w, h))
    
    answer = max_1 * max_2
    
    return answer