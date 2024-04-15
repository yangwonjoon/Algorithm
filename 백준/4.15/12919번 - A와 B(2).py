import sys
input = sys.stdin.readline

s=list(input().rstrip())
t=list(input().rstrip())
result =0

def dfs(t):
    global result
    if t==s:
        result =1
        return

    if len(t)==0:
        result=0
        return
    
    if t[-1]=='A':
        dfs(t[:-1]) 

    if t[0]=='B': 
        dfs(t[1:][::-1]) 

dfs(t)
print(result)
