kg = int(input())

INF = 50000
mvp = [INF for _ in range(kg + 1)]

mvp[3] = 1

if kg > 4:
    mvp[5] = 1
    for i in range(6, kg + 1):
        mvp[i] = min([mvp[i], mvp[i-3] + 1, mvp[i-5] + 1])

result = mvp[kg]
if result == INF:
    result = -1

print(result)