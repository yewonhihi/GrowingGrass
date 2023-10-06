import sys

m = int(sys.stdin.readline().rstrip())
S = set()

def check(s, x):
    if x in s:
        return 1
    else:
        return 0

for _ in range(m):
    temp = list(sys.stdin.readline().rstrip().split())
    if len(temp) == 2:
        act, num = temp[0], int(temp[1])
        if act == 'add':
            S.add(num)
        elif act == 'remove':
            if check(S, num) == 1:
                S.remove(num)
        elif act == 'check':
            print(check(S, num))
        elif act == 'toggle':
            if check(S, num) == 1:
                S.remove(num)
            else:
                S.add(num)
    else:
        act = temp[0]
        if act == 'all':
            S.update([i for i in range(1, 21)])
        elif act == 'empty':
            S.clear()