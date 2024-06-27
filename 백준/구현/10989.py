import sys

input = sys.stdin.read
n = int(input())
num = [int(input()) for _ in range(n)]
num_arr = [0] * 10001

for i in num:
    num_arr[i]+=1

for i in range(len(num_arr)):
    for _ in range(num_arr[i]):
        print(i)

        

import sys
input = sys.stdin.readline

#계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

#각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1
  
#arr에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)