#DFS는 한 노드에서 인접한 노드에서 갈 수 있는 노드들을 모두 탐색한 뒤, 다른 인접한 노드를 탐색하기 시작하는 탐색 방법입니다.

#스택이용
def dfs(idx):
    stack = []
    stack.append(idx)
    while stack:
        print('graph',graph)
        print('stack', stack)
        current = stack.pop()
        print(f"{current} 방문!")
        visited[current] = True
        print(visited)
        for adj in graph[current]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True

# #재귀
# def dfs(idx):
#     if visited[idx]: # 방문한 노드는 다시 방문할 필요가 없어요
#         return
#     visited[idx] = True # 이 노드를 방문 처리할게요
#     print(graph)
#     print(f"{idx} 방문!")
#     print(visited)
#     for i in graph[idx]: # 주변 노드들에 대해 하나씩 탐색을 시도해요
#         dfs(i)



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

dfs(1)
