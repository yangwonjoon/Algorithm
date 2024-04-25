from collections import deque

n, k = map(int, input().split())

MAX = 10 ** 5
visited = [0] * (MAX + 1)

def bfs(s):
    que = deque()
    que.append(s)

    while que:
        current = que.popleft()
        if current == k:
            return visited[k]
        for i in (current+1, current-1, current * 2):
            if 0 <= i <= MAX and not visited[i]: 
              visited[i] = visited[current] + 1
              que.append(i)

print(bfs(n))