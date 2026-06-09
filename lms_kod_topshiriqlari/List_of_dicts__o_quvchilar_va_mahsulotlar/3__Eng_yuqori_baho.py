n = int(input())
max_score = 0
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score > max_score:
        max_score = score
print(max_score)