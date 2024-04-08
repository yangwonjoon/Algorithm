def bfs(idx):
    from collections import deque
    queue = deque()
    queue.append(idx)
    visited[idx] = True

    while queue:

        print('queue', queue)
        print('graph', graph)
        print('visitied',visited)

        idx = queue.popleft()
        print(f"{idx} 방문!")

        for i in graph[idx]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프 초기 설정
n = 5
graph = [[] for  _ in range(n + 1)]
graph[1].append(2)
graph[1].append(4)
graph[2].append(4)
graph[4].append(1)
graph[4].append(5)
graph[5].append(3)
visited = [False] * (n + 1)

print('graph', graph)
print('visitied',visited)

bfs(1)
