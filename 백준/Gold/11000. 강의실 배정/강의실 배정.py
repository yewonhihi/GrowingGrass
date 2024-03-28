import heapq
import sys

input = sys.stdin.readline

n = int(input())

timetable = []

for _ in range(n):
    s, t = map(int, input().split())

    heapq.heappush(timetable, (s, t))

rooms = []

while(timetable):
    s, t = heapq.heappop(timetable)
    
    if rooms and rooms[0] <= s:
        heapq.heappop(rooms)
        
    heapq.heappush(rooms, t)
        
print(len(rooms))