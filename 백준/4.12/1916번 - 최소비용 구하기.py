'''--------------------------------------
  [접근]
    #풀긴했는데 예제의 다익스트라 함수 그래도 인용, 오늘 시간되면 다시 보자?

  💡 그래프 이론, 데이크스트라, 최단 경로
--------------------------------------'''

from heapq import *
import sys

def dijikstra(graph, start):

    INF = float('inf')

    dist = [INF] * len(graph) # 그래프 모든 값 inf
    dist[start] = 0 # start값만 0

    q = [(0, start)]
    
    while q:
        cost, idx = heappop(q)
        print('dist', dist)
        print('graph' ,graph)
        print('q', q,'cost', cost,'idx', idx)
        if dist[idx] < cost:
            continue
        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(q, (dist[adj], adj))

    return dist

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

print(dijikstra(graph, start)[end])

# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5