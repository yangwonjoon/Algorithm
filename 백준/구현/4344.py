n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

for i in score:
    average = sum(i[1:]) / len(i[1:])
    high_score = [j for j in i[1:] if j > average]
    percentage = len(high_score) / len(i[1:]) * 100
    print(f"{percentage:.3f}%")
