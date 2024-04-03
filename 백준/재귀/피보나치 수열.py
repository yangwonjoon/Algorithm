#1 1 3 4 7 11

def pibonacci(n):

    if(n == 1):
        return 1

    return pibonacci(n-2)+pibonacci(n-1)

print(pibonacci(10))