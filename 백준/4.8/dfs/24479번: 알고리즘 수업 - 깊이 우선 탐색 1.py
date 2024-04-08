'''--------------------------------------
  [접근]
    1. 노드 n개 graph 2차원 리스트, 방문기록을 위한 visited 리스트, 방문 순서를 기록할 count=1 생성
    2. 간선 m개 반복하여 양방향 간선 graph에 2차원 간선 생성 후, dfs함수에 시작노드 r 전달
    3. def 함수
        3_1: 이미 방문기록이 있는 노드면 리턴
        3_2: 없으면 방문 기록을 삽입(count), 노드 오름 차순 정렬
        3_3: 노드에서 갈 수 있는 다른 노드를 반복하며 방문기록이 없다면 count+=1 하고 def 함수 재귀

    [문제점]
    1. dfs함수안에서 오름차순 sort정렬한것 -> 정답
    2. 그래프를 생성할 때 오름차순 sort하여 생성한건 -> 오답
    3. graph, visited, count 순서, 출력값 다 똑같음(나머진 다 똑같음)
    3. 왜??????????(꽂혀서 시간 많이 썻는데도 이유를 모르겠다..? 이유 아시는분)

  💡 그래프 이론, 그래프 탐색, 정렬, 깊이 우선 탐색
--------------------------------------'''
## 1) dfs함수안에서 sort -> 정답
import sys

sys.setrecursionlimit(10**9)

def dfs(idx):
    
    global count
    if visited[idx]:
        return

    visited[idx] = count
    graph[idx].sort() ## ----> sort

    # print('graph:',graph)
    # print('visitied:',visited)
    # print('count:',count)
    
    for i in graph[idx]:
        
        if visited[i] == 0:  
            count += 1
            dfs(i)    

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0]* (n+1)
count =1

for i in range(m):
    node, output = map(int,input().split())
    graph[node].append(output)
    graph[output].append(node)
    
dfs(r)

for i in range(1, n+1):
    print(visited[i])  

# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4
# 1 6

# graph: [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
# visitied: [0, 1, 0, 0, 0, 0]
# count: 1
# graph: [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
# visitied: [0, 1, 2, 0, 0, 0]
# count: 2
# graph: [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
# visitied: [0, 1, 2, 3, 0, 0]
# count: 3
# graph: [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
# visitied: [0, 1, 2, 3, 4, 0]
# count: 4


# gpt의 대답
# 1) DFS 함수 내에서 정렬 (정답 코드)
# dfs 함수 내에서 각 노드의 인접 리스트를 정렬합니다. 이는 노드를 방문할 때마다 해당 노드의 인접 노드를 오름차순으로 탐색하게 만듭니다.
# 재귀적으로 dfs를 호출할 때마다 해당 노드의 인접 리스트가 정렬되어, 탐색 순서가 일관되게 유지됩니다.
# 이 방식은 노드의 인접 리스트가 동적으로 변경되거나, 특정 조건에 따라 다르게 탐색해야 하는 경우 유용합니다.
# 2) 그래프 생성 시 정렬 (오답 코드)
# 그래프를 생성할 때 각 노드의 인접 리스트를 정렬합니다. 그러나 이후에 dfs를 수행할 때 추가적인 정렬이 이루어지지 않습니다.
# 문제는, 노드를 추가하면서 바로 정렬을 하면, 모든 간선 정보가 입력된 후의 최종 정렬 상태가 아니라는 점입니다. 즉, 모든 노드를 연결한 후에는 일부 노드의 인접 리스트가 예상한 오름차순이 아닐 수 있습니다.
# 예를 들어, 노드 3을 처리하는 도중 노드 2와 연결되는 간선이 추가되면, 노드 2의 인접 리스트에 노드 3이 추가되고 바로 정렬됩니다. 그러나 이후에 노드 2에 더 낮은 번호의 노드가 연결될 경우, 최종적인 인접 리스트의 순서가 달라질 수 있습니다.
# 결론
# 따라서, 정답 코드에서는 dfs 호출 시 각 노드의 인접 리스트를 정렬함으로써, 노드를 탐색하는 순서가 문제에서 요구한 대로 일관되게 유지됩니다. 반면, 오답 코드에서는 노드 추가 시점의 정렬로 인해 최종적인 탐색 순서가 요구사항과 다를 수 있어, 정확한 결과를 얻지 못합니다. 문제의 요구사항에 따라 노드를 탐색하는 순서가 중요할 수 있으므로, 이러한 정렬 시점의 차이가 정답과 오답을 결정집니다.