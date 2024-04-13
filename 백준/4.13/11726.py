import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*1001
arr[1]=1
arr[2]=2

for i in range(3,n+1):
  arr[i] = (arr[i-1]+arr[i-2])%10007

print(arr[n])


# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [0,1,2]

# for i in range(len(arr),n+1):
#     arr.append(arr[i-1]+arr[i-2])

# print(arr[n]%10007)