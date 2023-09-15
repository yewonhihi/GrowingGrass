def d(n):
    num = n
    answer = n
    while(num > 0):
        temp = num % 10
        num //= 10
        answer += temp
        
    return answer

x = [0 for _ in range(10001)]
x[0] = 1

for i in range(1, 10001):
    temp = d(i)
    if temp <= 10000:
        x[temp] = 1
            
for i in range(1, 10001):
    if x[i] == 0:
        print(i)
