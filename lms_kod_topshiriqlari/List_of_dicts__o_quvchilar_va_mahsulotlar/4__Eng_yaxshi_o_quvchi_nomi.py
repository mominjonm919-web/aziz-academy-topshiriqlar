n = int(input())
max_score = -1
best_name = ""
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score > max_score:
        max_score = score
        best_name = name
print(best_name)