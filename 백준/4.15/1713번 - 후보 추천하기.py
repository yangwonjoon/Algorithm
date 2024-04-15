'''--------------------------------------
  [접근]
    1. dict -> result == {key : [추천수, time]}
    2. 후보자가 result에 있으면 추천수 +1
    3. 후보자가 result에 없으면
        3_1. 틀에 걸려있는 후보자 공간이 남으면 key 추가
        3_2. 틀에 걸려있는 후보자 공간이 없으면 1)추천수 2)time 낮은수를 기준으로 result에서 제거 후 추가

  💡 구현, 시뮬레이션
--------------------------------------'''

import sys
input = sys.stdin.readline

n = int(input())
num = int(input())
students = list(map(int, input().split()))
result = {}
time = 0  

for student in students:
    if student in result:
        result[student][0] += 1    
    else:
        if len(result) < n:
            result[student] = [1, time]
        else:
            min_result = min(result.items(), key=lambda x: (x[1][0], x[1][1]))
            del result[min_result[0]]  
            result[student] = [1, time]  
    time += 1 

students = sorted(result.keys())
print(*students)