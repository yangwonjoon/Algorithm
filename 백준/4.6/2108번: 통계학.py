'''---------------------------------------
  [접근]
    num : input 받은 값
    중앙값 : num의 합 / num의 길이를 round(반올림 함수)로 처리
    중앙값 : num을 정렬한 뒤, num을 2로 나눈 몫을 인덱싱
    최빈값 
        1. dic을 생성
        2. num의 요소를 돌며, dic의 key값에 있으면 +1 없으면 = 1
        3. dic의 최대 value 찾고, 최대 value와 같은 dic 요소들을 리스트로 만든 후 정렬
        4. 최대값이 하나면 그 수 반환, 2개이상이면 2번째값반환
    최대값, 최소값차이 중앙값 찾을때 정렬한 num의 처음, 마지막값

  💡 수학, 구현, 정렬
---------------------------------------'''

import sys

input = sys.stdin.readline
n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))
num_len = len(num)

#평균값
a = round(sum(num)/num_len)
#중앙값
num.sort()
b = num[num_len//2]
#최빈값
dic = {}
for i in num:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

max_value = max(dic.values())
max_arr = sorted([k for k,v in dic.items() if v == max_value])
c = 0
if(len(max_arr) > 1):
    c = max_arr[1]
else:
    c = max_arr[0]

#최대값, 최소값차이
d = num[-1] - num[0]

for i in [a,b,c,d]:
    print(i)
