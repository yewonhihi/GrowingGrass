def solution(s):
    answer = True
    stack = []
    
    for cur in s:
        if cur == '(':
            stack.append(cur)
        elif cur == ')':
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()
    
    if len(stack) != 0:
        answer = False

    return answer