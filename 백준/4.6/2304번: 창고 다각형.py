'''---------------------------------------
  [접근]
    기둥을 x축 순으로 정렬 
    최대 높이전까지 돌면서 다음 기둥이 현재보다 높으면
    result에 현재의 면적을 계산해서 더해주고 높이를 다음 기둥으로
    아니면 그냥 현재면적을 더해준다. 
    뒤에서부터도 똑같이 진행한다.

  💡 자료 구조, 브루트포스 알고리즘, 스택
---------------------------------------'''

n = int(input())

lst = []
result = 0
for i in range(n) :
    a,b = map(int,input().split())
    lst.append([a,b])
lst.sort()

i = 0
for l in lst :
    if l[1] >result :
        result = l[1]
        idx = i
    i += 1
height = lst[0][1]

for i in range(idx) :
    if height < lst[i+1][1] :
        result += height * (lst[i+1][0]-lst[i][0])
        height = lst[i+1][1]
    else :
        result += height * (lst[i+1][0] - lst[i][0])
height = lst[-1][1]

for i in range(n-1, idx, -1) :
    if height < lst[i-1][1] :
        result += height * (lst[i][0]-lst[i-1][0])
        height = lst[i-1][1]
    else :
        result += height * (lst[i][0] - lst[i-1][0])

print(result)