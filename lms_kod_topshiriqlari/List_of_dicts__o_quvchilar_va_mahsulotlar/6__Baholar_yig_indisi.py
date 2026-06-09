n = int(input())
total = 0
for _ in range(n):
    name, score = input().split()
    score = int(score)
    total += score
print(total)