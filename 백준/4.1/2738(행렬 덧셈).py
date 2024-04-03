N, M = map(int, input().split()) #N=3 ,M=3

arr1 =[list(map(int, input().split())) for _ in range(N)]
arr2 =[list(map(int, input().split())) for _ in range(N)]

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j]+arr2[i][j], end=' ')
    print()