from collections import deque

# t = int(input())

# for _ in range(t):
n = int(input())

now = map(int, input().split())
next = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

que = deque()

 # 시계방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]