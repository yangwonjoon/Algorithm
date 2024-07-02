import sys

input = sys.stdin.readline
str = list(input().rstrip())
bomb = list(input().rstrip())
result = []

for i in bomb:
    for j in str:
        if j != i:
            result.append(j)

print(result)