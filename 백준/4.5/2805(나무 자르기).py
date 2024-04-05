n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree_len = len(tree)
left = 0
right = tree_len-1

while left <= right:
    mid = tree_len // 2
    sum = 0

    for i in range(mid, right):
        

