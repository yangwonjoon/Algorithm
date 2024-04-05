# sum함수: 리스트를 받아서 리스트의 요소들을 다 더한값을 반환
# 1. 입력받아서 리스트 정렬
# 2. 정렬한 리스트를 낮은 별로 슬라이싱하여 sum 함수에 전달 반환값은 최종값으로 저장


def a(num):

    sum=0
    for i in num:
        sum += i

    return sum

n = int(input())
time = list(map(int, input().split()))
time.sort()

b = 0

for i in range(len(time)):
    b += a(time[:i+1])
    
print(b)
    

#좋아보이는 코드

# import sys
# read = sys.stdin.readline

# N = int(read().rstrip())
# ARR = [*map(int, read().rstrip().split(' '))]

# ARR.sort()
# prev = 0
# answer = []
# for num in ARR:
#   answer.append(prev + num)
#   prev += num

# print(sum(answer))    

