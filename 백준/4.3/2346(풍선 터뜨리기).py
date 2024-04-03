#덱의 rotate이용
#enumerate로 덱의 인덱스 번호를 주고 맨 앞에꺼를 제거 후 
#결과 리스트에 추가
#num의 값에 따라 rotate로 회전 후 맨앞으로 오게하기

from collections import deque

n = int(input())
q = deque(enumerate(map(int,input().split())))
result = []

while q:

    index,num = q.popleft()
    result.append(index+1) 

    if num>0:
        q.rotate(-(num-1)) #음수, 왼쪽회전
        
    if num<0:
        q.rotate(-num) #양수, 오른쪽 회전

for i in result:
    print(i, end=' ')

