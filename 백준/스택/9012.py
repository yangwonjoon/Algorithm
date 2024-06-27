n = int(input())
arr = [list(input()) for _ in range(n)]

for i in arr:
    result = []
    is_balanced = True  
    for j in i:
        if j == '(':
            result.append(j)
        else:
            if len(result) == 0:
                print('NO')
                is_balanced = False
                break
            result.pop()
    if is_balanced:
        if len(result) == 0:
            print('YES')
        else:
            print('NO')