import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
num = []

for _ in range(n):
    temp = int(sys.stdin.readline().rstrip())
    num.append(temp)

num.sort()

num1 = round(sum(num) / n)
num2 = num[n // 2]

counter = Counter(num).most_common()
num3 = 0
    
if len(counter) == 1:
    num3 = counter[0][0]
        
elif counter[0][1] == counter[1][1]:
    num3 = counter[1][0]
        
else:
    num3 = counter[0][0]

num4 = max(num) - min(num)

print(num1)
print(num2)
print(num3)
print(num4)