arr = [list(map(int, input().split()))for _ in range(9)]

row = 0 #행
low = 0 #열
num = 0

for row_idx, i in enumerate(arr):
    for low_idx,j in enumerate(i): 
        if(j >= num):
            num = j
            row = row_idx+1
            low = low_idx+1

print(num)
print(row,low)        





