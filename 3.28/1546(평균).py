N = int(input())

numbers = list(map(int, input().split()))
new_numbers = []

for i in numbers:
    new_numbers.append(i/max(numbers)*100)

print(sum(new_numbers)/N)
