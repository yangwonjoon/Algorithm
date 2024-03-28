#입력 ababc

S = input()
answer = []
for i in range(len(S)):
    for j in range(i,len(S)):
        answer.append(S[i:j+1])

print(len(set(answer)))