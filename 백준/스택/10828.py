def switch(value):
    if value[0] == "push":
        result.append(value[1])
    elif value[0] == "top":
        if(len(result) == 0):
            print(-1)
        else:
            print(result[-1])
    elif value[0] == "pop":
        if(len(result) == 0):
            print(-1)
        else:
            b = result.pop()
            print(b)
    elif value[0] == "size":
        print(len(result))
    elif value[0] == "empty":
        if(len(result) == 0):
            print(1)
        else:
            print(0)
    

n = int(input())
arr = [input().split() for _ in range(n)]
result = []

for i in arr:
    switch(i)
