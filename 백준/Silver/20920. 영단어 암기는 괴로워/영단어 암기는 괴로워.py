import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().rstrip().split())

dic = dict()

for _ in range(n):
    word = input().rstrip()
    l = len(word)
    if l >= m:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

for word, cnt in sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0])):
    print(word + "\n")