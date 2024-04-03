n = int(input())
tower = list((map(int,input().split())))
stack=[]
result=[]

for i in range(len(tower)):
    tall=tower[i]

    if stack: 
        while stack and stack[-1][1] <= tall:
            stack.pop()
    
    if stack:       
        result.append(stack[-1][0]+1)
        stack.append([i,tall])
    else:
        stack.append([i,tall])
        result.append(0)  

# 5
# 6 9 5 7 4