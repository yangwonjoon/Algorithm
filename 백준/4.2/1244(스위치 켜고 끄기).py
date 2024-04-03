def turn(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0

switch_num = int(input())
switch = list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    sex, num = map(int, input().split())
    
    if sex == 1:        
        for i in range(1, switch_num+1):
            if i % num == 0:
                turn(i - 1)
    
    if sex == 2:
        index = num - 1
        turn(index)
        i = 1
        while num - i >= 1 and num + i <= switch_num:
            if switch[index + i] == switch[index - i]:
                turn(index + i)
                turn(index - i)
            else:
                break
            i += 1
    
for i in range(switch_num):
    print(switch[i], end='')
    if (i + 1) % 20 == 0: 
        print()
    else:  
        print(' ', end='')