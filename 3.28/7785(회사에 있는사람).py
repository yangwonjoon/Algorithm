n = int(input())
count = []


for i in range(n):
    name, existence =input().split()

    if(existence == "enter"):
        count.append(name)
    
    if(existence == "leave"):
        count.remove(name)

count = sorted(count, reverse=True)

for j in count:
    print(j)


#sort 와 sorted의 차이
#사전이 리스트보다 빠른듯  https://star7sss.tistory.com/398
#리스트 remove는 시간복잡도가 별로 안좋다