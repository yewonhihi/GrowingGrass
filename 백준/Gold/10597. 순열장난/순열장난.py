import sys

input = sys.stdin.readline

numbers = input().strip()
n = len(numbers)
cnt = n

if n > 9:
    cnt = (n - 9) // 2 + 9

result = []
        
def kriii(idx):
    if idx == n:
        print(' '.join(result))
        exit(0)
    
    k = numbers[idx]
    if k not in result and k != '0':
        result.append(k)
        kriii(idx + 1)
        result.pop()
    
    k = numbers[idx:idx+2]
    if k[0] != '0' and k not in result and int(k) <= cnt:
        result.append(k)
        kriii(idx + 2)
        result.pop()

kriii(0)