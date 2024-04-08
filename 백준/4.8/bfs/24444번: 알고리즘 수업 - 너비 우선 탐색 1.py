'''--------------------------------------
  [접근]
    1. 노드 n개 graph 2차원 리스트, 방문기록을 위한 visited 리스트, 방문 순서를 기록할 count=1 생성
    2. 간선 m개 반복하여 양방향 간선 graph에 2차원 간선 생성 후, bfs함수에 시작노드 r 전달
    3. bfs 함수
        3_1: 처음 노드 큐에 넣고 방문기록 남기고 ,count +1
        3_2: 그 다음 큐가 있을 때까지,
        3_3: 큐의 맨 왼쪽값 빼서 정렬 후 그 노드에 연결된 노드 순회
        3_4: 방문한적이 없다면 방문기록 남기고 count +1

  💡 그래프 이론, 그래프 탐색, 정렬, 너비 우선 탐색
--------------------------------------'''

import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0]*(n+1)
count = 1

def bfs(idx):
    global count

    que = deque([idx])
    visited[idx] = count 
    count += 1

    while que:

        current = que.popleft()
        graph[current].sort()  

        for i in graph[current]:
            if not visited[i]: 
                que.append(i)
                visited[i] = count  
                count += 1
                
for i in range(m):
    node, output = map(int, input().split())
    graph[node].append(output)
    graph[output].append(node)

bfs(r)

for i in range(1, len(visited)):
    print(visited[i])
