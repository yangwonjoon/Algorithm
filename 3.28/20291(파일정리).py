N = int(input())
extension_dic = {}

for i in range(N):
    name, extension = input().split('.')

    if(extension in extension_dic):
        extension_dic[extension] += 1
    else:
        extension_dic[extension] = 1

extension_dic = dict(sorted(extension_dic.items()))

for key, value in extension_dic.items():
    print(key, value)

#사전 정렬 https://codechacha.com/ko/python-sorting-dict/ -> 리스트로 반환됨
#dict으로 래핑하면 튜플이 올바른 구조일때 dict으로 바뀜
    
#사전으로 래핑 안하고 푼거 -> https://tmdrl5779.tistory.com/132