# #예제의 스택 판별 함수 이용
# )가 나올때 ( 제거하고 
# )가 나올때 stack리스트에 비어있으면 falsy 반환
# 아니면 truty 반환

def stack(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    return not stack


t = int(input())
arr = [input() for _ in range(t)]

for i in arr:
    if stack(i):
        print('YES')
    else:
        print('NO')



