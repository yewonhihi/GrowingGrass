import sys

n = int(sys.stdin.readline().rstrip())
drink = list(map(int, sys.stdin.readline().rstrip().split()))

print(sum(drink) / 2 + max(drink) / 2)