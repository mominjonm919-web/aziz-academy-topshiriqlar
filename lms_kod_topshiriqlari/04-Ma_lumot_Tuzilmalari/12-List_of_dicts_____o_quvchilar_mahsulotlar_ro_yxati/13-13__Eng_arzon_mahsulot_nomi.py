n = int(input())
items = [input().split() for _ in range(n)]
print(min(items, key=lambda x: int(x[1]))[0])