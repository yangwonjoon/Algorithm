#계속 런타임 오류

import sys

N = int(sys.stdin.readline())
word_N =[sys.stdin.readline().strip() for i in range(N)]
word_N_set = set(word_N)

M = int(sys.stdin.readline())
word_M =[sys.stdin.readline().strip() for i in range(M)]
word_M_set = set(word_M)
word_M = list(word_M_set-word_N_set)

result = ''

question_index = word_N.index('?')
before_question = word_N[question_index-1][-1]
after_question = word_N[question_index+1][0]

if(question_index==0):
    for k in word_M:
        if(k[0] == after_question):
            result = k
elif(question_index== len(word_N)-1):
    for k in word_M:
        if(k[-1] == before_question):
            result = k
else:
    for k in word_M:
        if(k[0] == before_question and k[-1] == after_question):
            result = k

print(result)

