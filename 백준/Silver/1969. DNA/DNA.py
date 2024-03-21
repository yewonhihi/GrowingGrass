from collections import Counter

n, m = map(int, input().split())
dna = []
answer = ""
distance = n * m

for _ in range(n):
    dna.append(list(input().strip()))

dna = list(map(list, zip(*dna)))

for i in range(m):
    temp = dna[i]
    letter, cnt = sorted(Counter(temp).items(), key=lambda x:(-x[1], x[0]))[0]
    answer += letter
    distance -= cnt

print(answer)
print(distance)