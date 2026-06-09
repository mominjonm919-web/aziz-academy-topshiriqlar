n = int(input().strip())
a = [input().split() for _ in range(n)]
print(max(a, key=lambda x: int(x[1]))[0])