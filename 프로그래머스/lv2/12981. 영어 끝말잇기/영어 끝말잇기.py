def solution(n, words):
    answer = [0, 0]
    word_set = []
    turn = 1
    
    for i in words:
        
        if turn == 1:
            word_set.append(i)
            turn += 1
            continue
            
        if words[turn-2][-1] != i[0]:
            break
            
        if i in word_set:
            break
        
        word_set.append(i)
        turn += 1

    if turn != len(words) + 1:
        answer[0] = turn % n if turn % n != 0 else n
        answer[1] = turn // n if answer[0] == n else turn // n + 1
    
    return answer