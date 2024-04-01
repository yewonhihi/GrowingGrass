import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

cnt = 0

if boxes[0] > cranes[0]:
    print(-1)
else:
    while(boxes):
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            
            for b in boxes:
                if b <= c:
                    boxes.remove(b)
                    break
                
        cnt += 1
    
    print(cnt)