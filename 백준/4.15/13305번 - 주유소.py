'''--------------------------------------
  [접근]
    1. 도시별 주유 가격, 이동 거리를 담는다
    2. 첫번째 도시의 주유가격을 min_price에 담고, n-1번 반복문을 돌며 도시별 주유가격이 min_price보다 작으면 주유가격을 갱신해줌
    3. result에 담는다

  💡 그리디
--------------------------------------'''

import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
result=0
min_price = prices[0]

for i in range(n - 1):
    if min_price > prices[i]:
        min_price = prices[i]
    result += min_price * distances[i]

print(result)
