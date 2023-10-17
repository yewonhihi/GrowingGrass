import sys
from collections import deque

input = sys.stdin.readline

cursor_left = deque(list(input().rstrip()))
cursor_right = deque()

n = int(input().rstrip())

for _ in range(n):
    action = input().rstrip()
    if action == 'L':
        if len(cursor_left) != 0:
            cursor_right.appendleft(cursor_left.pop())
    elif action == 'D':
        if len(cursor_right) != 0:
            cursor_left.append(cursor_right.popleft())
    elif action == 'B':
        if len(cursor_left) != 0:
            cursor_left.pop()
    else:
        do, word = action.split(" ")
        cursor_left.append(word)

print("".join(cursor_left+cursor_right))