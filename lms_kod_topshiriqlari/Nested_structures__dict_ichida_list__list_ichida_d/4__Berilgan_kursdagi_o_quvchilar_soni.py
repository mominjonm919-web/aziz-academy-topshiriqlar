d = {}
for _ in range(int(input())):
    s = input().split()
    d[s[0]] = int(s[1]) if len(s) > 1 else 0
print(d.get(input().strip(), 0))