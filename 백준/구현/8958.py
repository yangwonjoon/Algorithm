n = int(input())
ox = [input() for _ in range(n)]
stack = 0
result = 0

for i in ox:
    for j in i:
        if(j =='O'):
            stack+=1
            result += stack
        else:
            stack = 0
    print(result)
    result=0
    stack=0
        

