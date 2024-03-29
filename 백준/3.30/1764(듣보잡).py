#set
#sort, sorted 차이?

N, M = map(int,input().split())

word_N=[]
word_M=[]

for i in range(N+M):
    if(i<N):
        word_N.append(input())
    else:
        word_M.append(input())

word_M=set(word_M)
word_N=set(word_N)
result= list(word_M.intersection(word_N))
result=sorted(result)

print(len(result))
for j in result:
    print(j)