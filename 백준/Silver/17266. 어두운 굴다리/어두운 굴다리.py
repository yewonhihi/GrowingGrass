import sys
import math

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
location = list(map(int, input().rstrip().split()))

between = []

between.append(location[0])
between.append(n - location[-1])

for i in range(m-1):
    between.append(math.ceil((location[i+1]-location[i])*0.5))

print(str(max(between)))