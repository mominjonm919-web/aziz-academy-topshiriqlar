s = input().strip()
name, n = s.split()
n = int(n)
print((name + " ") * (n - 1) + name)