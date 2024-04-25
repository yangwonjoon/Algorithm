'''--------------------------------------
  [접근]

  💡 자료 구조, 그리디 알고리즘, 우선순위 큐
--------------------------------------'''

from heapq import heapify, heappush, heappop
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    chapter = list(map(int,input().split()))
    heapify(chapter)
    result = 0 


    while len(chapter) > 1:
        temp = 0
        num1 = heappop(chapter)
        num2 = heappop(chapter)
        temp = num1 + num2
        result += temp
        heappush(chapter, temp)

    
    print(result)