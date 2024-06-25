a,b = map(int, input().split())
num = list(map(int, input().split()))
# num = num[:a]

for i in num:
    if(i < b):
        print(i)