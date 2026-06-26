n = int(input())
s = {input().split()[0]for _ in range(n)}
print(["NO","YES"][input()in s])