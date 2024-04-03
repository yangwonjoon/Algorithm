#for문 없이 재귀로

def sum(n):

    if n == 1:
        return 1

    return n + sum(n-1)

print(sum(5))


5+4+3+2+1