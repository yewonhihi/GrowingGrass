def ans_1(n): # 문항 인덱스 번호
    return n % 5 + 1

def ans_2(n):
    if n % 2 == 0: return 2
    if n % 8 == 1: return 1
    if n % 8 == 3: return 3
    if n % 8 == 5: return 4
    if n % 8 == 7: return 5

def ans_3(n):
    if n % 10 in [0, 1]: return 3
    if n % 10 in [2, 3]: return 1
    if n % 10 in [4, 5]: return 2
    if n % 10 in [6, 7]: return 4
    if n % 10 in [8, 9]: return 5
    
def solution(answers):
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        answer = answers[i]
        if answer == ans_1(i): count[0] += 1
        if answer == ans_2(i): count[1] += 1
        if answer == ans_3(i): count[2] += 1
        
    max_count = max(count)
    
    return [i+1 for i in range(3) if count[i] == max_count]