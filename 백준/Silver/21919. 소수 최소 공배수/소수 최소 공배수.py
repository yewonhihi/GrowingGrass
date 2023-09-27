import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

max_A = max(A)
prime_list = [1 for _ in range(max_A + 1)]

for i in range(2, max_A + 1):
    for j in range(i*2, max_A + 1, i):
        if prime_list[j] == 1:
            prime_list[j] = 0

result = 1
result_set = set()

for a in A:
    if prime_list[a]:
        if a not in result_set:
            result_set.add(a)
            result *= a

if result == 1:
    result = -1

print(result)