n = int(input())
min_score = float('inf')
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score < min_score:
        min_score = score
print(min_score)