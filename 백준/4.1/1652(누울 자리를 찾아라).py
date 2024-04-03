def rotate(arr):
    n = len(arr)
    rotated_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_arr[j][n - 1 - i] = arr[i][j]
    return rotated_arr

N = int(input())
arr = [list(input()) for _ in range(N)]
low_arr = rotate(arr)

row_count = 0
low_count = 0 
room = 0

for i in arr:
    for j in i:
        if(j == '.'):
            room += 1
        if(j == 'X'):
            if(room >=2):
                row_count +=1
            room =0
    if(room >= 2):
        row_count +=1
    room = 0

for i in low_arr:
    for j in i:
        if(j == '.'):
            room += 1
        if(j == 'X'):
            if(room >=2):
                low_count +=1
            room =0
    if(room >= 2):
        low_count +=1
    room = 0

print(row_count, low_count)