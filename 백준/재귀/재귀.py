#sum이란 함수에 n을 넣으면 1~n까지의 합을 반환해주는 함수 for문 안쓰고

def sum(n):

    if n == 1:
        return 1

    return n + sum(n-1)

print(sum(5))

#피보나치 수열 재귀로 만들어보자 -> 원래는 반복문이랑 캐시를 만들어야함
#n과 m 만들어보기
#백트래킹
#유투브 쉬운코드
