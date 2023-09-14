from collections import deque

def solution(priorities, location):
    answer = []
    dq = deque(priorities)
    index_q = deque(i for i in range(len(priorities)))
    
    while(len(dq) > 0):
        p = dq.popleft()
        i = index_q.popleft()
        if len(dq) > 0:
            if max(dq) > p:
                dq.append(p)
                index_q.append(i)
                continue
            
        answer.append(i)
        
    return answer.index(location) + 1