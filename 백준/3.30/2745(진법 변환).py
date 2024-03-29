#ZZZZZ 36

n, b= input().split()
n = n[::-1]
b = int(b)


if(n[0].isdigit()):
    first = int(n[0])

if(n[0].isalpha()):
    first = int(ord(n[0]))-55

result=0

for i in range(len(n)):
    result += first*(b**i)

print(result)


#이거 왜 안됨?
