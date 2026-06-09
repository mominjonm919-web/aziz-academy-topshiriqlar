n = int(input())
count = 0
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score > 80:
        count += 1
print(count)