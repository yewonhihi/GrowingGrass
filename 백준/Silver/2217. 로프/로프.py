n = int(input())
weight = []

for _ in range(n):
    weight.append(int(input()))

weight.sort()

for i in range(n):
    weight[i] *= n - i

print(max(weight))