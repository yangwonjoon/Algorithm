'''--------------------------------------
  [접근]안품

  💡 자료 구조, 스택
--------------------------------------'''

import sys

input = sys.stdin.readline
n = int(input())

stack = []
result = 0

for _ in range(n):
    x,y = map(int, input().split())

    while len(stack)>0 and stack[-1] >y:
        result+=1
        stack.pop()

    if len(stack)>0 and stack[-1] == y:
        continue
    stack.append(y)

while len(stack)>0:
    if stack[-1] >0:
        result+=1
    stack.pop()

print(result)