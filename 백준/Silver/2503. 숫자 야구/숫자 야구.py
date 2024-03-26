from itertools import permutations

n = int(input())

can = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

for _ in range(n):
    guess, strike, ball = map(int, input().split())
    guess = tuple(str(guess))
    r_cnt = 0
    
    for i in range(len(can)):
        i -= r_cnt
        num = can[i]
        
        s_cnt = 0
        b_cnt = 0
        
        for j in range(3):
            if num[j] == guess[j]:
                s_cnt += 1
            elif num[j] in guess:
                b_cnt += 1
                
        if s_cnt != strike or b_cnt != ball:
            can.remove(num)
            r_cnt += 1
            
print(len(can))