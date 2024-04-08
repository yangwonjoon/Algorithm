## 2) 그래프 만들 때 sort -> 바로 오답
import sys

sys.setrecursionlimit(10**9)

def dfs(idx):
    
    global count
    if visited[idx]:
        return

    visited[idx] = count

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
    graph[node].sort()   ## ---> sort
    graph[output].sort()  ## ---> sort
    
dfs(r)

for i in range(1, n+1):
    print(visited[i])

#graph: [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]
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



