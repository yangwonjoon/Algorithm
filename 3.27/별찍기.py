#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

#입력: 5
#출력
# *
# **
# ***
# ****
# *****

a = input()

for i in range(int(a)):
    print('*'*(i+1))