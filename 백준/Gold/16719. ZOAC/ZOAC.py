letters = list(input().strip())

n = len(letters)
turns = []

def find(cur, turns):
    target = sorted(cur)[0]
    turns.append(target)
   
    c_index = cur.index(target)
    
    left = cur[:c_index]
    right = cur[c_index+1:]
        
    if len(right) != 0:
        find(right, turns)
    
    if len(left) != 0:
        find(left, turns)

find(letters, turns)
turns.reverse()

for i in range(n-1, 0, -1):
    temp = letters.copy()
    for x in turns[0:i]:
        temp.remove(x)
        
    print(''.join(temp))

print(''.join(letters))
