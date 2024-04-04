# 1. 카드에서 최소 힙 2개를 뺀 뒤 더한 값을 2번 카드 리스트에 더함
# 2. m번 반복
# 3. sum


from heapq import heapify, heappop, heappush
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))

for _ in range(m):
    heapify(num)
    min1 = heappop(num)
    min2 = heappop(num)
    minSum = min1+min2

    heappush(num, minSum)
    heappush(num, minSum)

print(sum(num))



