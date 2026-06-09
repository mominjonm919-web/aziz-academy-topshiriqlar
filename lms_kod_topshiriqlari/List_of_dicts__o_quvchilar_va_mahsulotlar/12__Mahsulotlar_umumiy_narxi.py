n = int(input())
total = 0
for _ in range(n):
    line = input().split()
    total += int(line[1])
print(total)