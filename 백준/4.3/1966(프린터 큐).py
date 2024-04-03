# que에서 max 값과 첫값 제거 후 저장
# 첫값이 베스트 아니면 뒤로 보냄
# 찾으려 하는 값 index -1

#n번씩 반복하여 
from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    que =  deque(list(map(int, input().split())))

    count = 0
    while que:
        best = max(que) 
        front = que.popleft() 
        m -= 1 

        if best == front: 
            count += 1
            if m < 0: 
                print(count) 
                break

        else:   
            que.append(front)
            if m < 0 : 
                m = len(que) - 1 

# 6 0
# 1 1 9 1 1 1



            