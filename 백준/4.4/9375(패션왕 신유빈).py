# 1. input 받음
# 2. 옷의 type이 dictionary에 있다면 outfits[type] +=1
# 2_1. 옷이 type이 dictionary에 없으면 outfits[type]=1
# 3. 최종적으로 dictionary에 옷의 type 별 갯수가 나옴
# 4. 경우의 수는 (type의 갯수 + 1(옷을 안입는 경우))*(type의 갯수 + 1(옷을 안입는 경우)) ... - 1(옷을 다입는 경우)

t = int(input()) 

for _ in range(t):
    n = int(input()) 
    outfits={}
    result = 1
    for _ in range(n):
        name, type = input().split()
        if type in outfits:
            outfits[type] +=1
        else:
            outfits[type] = 1

    for i in outfits:
        result *= (outfits[i]+1)

    print(result-1)