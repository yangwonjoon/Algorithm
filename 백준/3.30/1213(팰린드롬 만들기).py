#짝수면 AABB -> ABBA
#홀수면 

import collections

word = input()
check_word = collections.Counter(word)

count = 0
result = ''
mid = ''

#홀수 2개일때
for key, value in list(check_word.items()):
    if value % 2 == 1:
        count += 1
        mid = key

        if count >= 2: 
            print("I'm Sorry Hansoo")
            exit()

#반짜른거
for key, value in sorted(check_word.items()): 
    result += (key * (value // 2)) 

print(result + mid + result[::-1])



    
