A = set(input().strip().split())
B = set(input().strip().split())
common = A & B 
result = sorted(common)
print(len(result))
for name in result:
    print(name)