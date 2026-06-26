n = int(input())
a = [input().split() for _ in range(n)]
a.sort(key = lambda x: int(x[1]))
for x in a: print(*x)