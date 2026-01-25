from collections import deque

def predictPartVictory(senate : str) -> str :
    queue_R = deque()
    queue_D = deque()
    

    for i , s in enumerate(senate):
        if s == "R" :
            queue_R.append(i)
        else : 
            queue_D.append(i)
    
    while queue_R and queue_D : 
        r = queue_R.popleft()
        d = queue_D.popleft()

        if r < d : 
            queue_R.append(r + len(senate))
        else  :
            queue_D.append(d + len(senate))
    
    return "Radiant" if queue_R else "Dire"