# from itertools import permutations

# N, M = map(int, input().split())

# a = list(permutations(range(1, N + 1), M))

# for i in a:
#     for j in i:
#         print(j, end=' ')

N, M = map(int, input().split())
result = []

# def backtrack():
#     # 출력 조건
#     if len(result) == M:
#         print(' '.join(map(str, result)))
        
#     for i in range(1, N + 1):
#         if i not in result: 
#             result.append(i)
#             backtrack()
#             result.pop()
            
# backtrack()

n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
