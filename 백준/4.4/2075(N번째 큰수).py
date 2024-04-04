# 1. n*n 2차원 배열을 리스트로 받음
# 2_1. 힙의 길이가 5가 넘지 않는다면 힙에 숫자를 넣음 계속
# 2_2. 힙의 길이가 5가 되면 요소를 힙의 최솟값과 비교하여 클 때 최솟값과 교체
# 3. 그럼, 작은 값은 계속 없어지고 최상위 5개가 힙에 남고 그 중 최소 힙 출력

from heapq import heappush, heappop
from sys import stdin

input = stdin.readline
n = int(input())

heap=[]

for i in range(n):
    num = list(map(int,input().split()))
    for j in num:
        if len(heap) < n:
            print(heap)
            heappush(heap, j)
        else:
            if j > heap[0]:
                heappop(heap)
                heappush(heap, j)
    print(heap)
