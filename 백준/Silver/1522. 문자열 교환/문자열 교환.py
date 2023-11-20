import sys

input = sys.stdin.readline

letters = list(input().strip())

n = len(letters)
count = float("inf")
a_count = letters.count("a")

letters.extend(letters[0:a_count-1])

for i in range(n):
    target = letters[i:i+a_count]
    count = min(count, target.count("b"))

print(count)