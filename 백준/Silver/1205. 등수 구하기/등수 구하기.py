import sys

input = sys.stdin.readline
print = sys.stdout.write

n, new, p = map(int, input().rstrip().split())

result = 1

if n != 0:
    ranking_list = list(map(int, input().rstrip().split()))
    if n == p and ranking_list[-1] >= new:
        result = -1
    else:
        for r in ranking_list:
            if new < r:
                result += 1
            else:
                break

print(str(result))