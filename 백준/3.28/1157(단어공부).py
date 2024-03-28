words = input()
words = words.upper()

words_dic = {}

for word in words:
    if(word in words_dic):
        words_dic[word] += 1
    else:
        words_dic[word] = 1
        
count = len([k for k,v in words_dic.items() if max(words_dic.values()) == v] )

if count > 1 :
    print('?')
else:
    print(max(words_dic, key=words_dic.get))


#관련 자료(파이썬 딕셔너리 value로 키 찾기) : https://106hht.tistory.com/64
#다른 답 : https://wook-2124.tistory.com/257        

#Counter를 사용해도 될듯
        
