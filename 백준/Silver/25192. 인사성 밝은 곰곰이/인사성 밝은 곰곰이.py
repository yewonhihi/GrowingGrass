import sys

n = int(input())
name_list = set()
count = 0

for _ in range(n):
    chat = str(sys.stdin.readline().strip())
    if chat == 'ENTER':
        name_list.clear()
        continue
    else:
        if chat not in name_list:
            count += 1
            name_list.add(chat)

print(count)