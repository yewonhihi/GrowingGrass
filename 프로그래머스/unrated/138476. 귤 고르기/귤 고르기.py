from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = k
    i = 0
    
    counter = Counter(tangerine).most_common()
    while (count > 0):
        count -= counter[i][1]
        answer += 1
        i += 1
        
    return answer