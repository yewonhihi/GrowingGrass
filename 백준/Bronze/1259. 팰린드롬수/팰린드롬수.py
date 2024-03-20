numbers = []
answers = []

while True:
    n = int(input())
    if n == 0:
        break
    numbers.append(str(n))

for num in numbers:
    n = len(num)
    answer = "yes"
    
    for i in range(n // 2):
        if num[i] != num[n - i - 1]:
            answer = "no"
            break
            
    answers.append(answer)

for ans in answers:
    print(ans)