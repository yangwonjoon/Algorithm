def fact(m):
    result = 1
    if(m > 0):
        result = m * fact(m-1)
        print(result)
    return result

n = int(input())
fact(n)

