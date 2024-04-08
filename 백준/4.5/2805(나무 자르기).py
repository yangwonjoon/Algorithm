'''---------------------------------------
  💡 이분 탐색,정렬
---------------------------------------'''

n, m = map(int, input().split())
trees = list(map(int,input().split()))
trees.sort()

left = 0 
right = len(trees) - 1  #3

while left <= right:
    mid = (left+right) // 2  
    sum = 0

    for i in range(mid, len(trees)+1 ):
        sum += (trees[i]-trees[mid])
    
    if sum == m:
        print(trees[mid])
        exit()
    elif sum < m:
        right = mid
    else:
        left = mid




