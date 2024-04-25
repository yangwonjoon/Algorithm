'''--------------------------------------
  [접근]
    1. 최대한 많은 회의를 넣기 위하여 1)회의 종료 시간 , 2) 회의 시작 시간 순으로 정렬
    2. 0시부터 시작하여 반복문을 돌며 종료시간보다 회의 시작 시간이 크거나 같으면 시간을 늘려나감
    3. count 하고 count값 반환

  💡 그리디, 정렬
--------------------------------------'''
import sys

input = sys.stdin.readline
n = int(input())
meetings=[]

for _ in range(n):
    a, b = map(int,input().split())
    meetings.append((a,b))

meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

start= 0
count = 0

for meeting in meetings:
    if(start <= meeting[0]):
        start = meeting[1]
        count += 1

print(count)

