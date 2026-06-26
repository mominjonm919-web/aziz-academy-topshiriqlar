students = set()
n = int(input().strip())
for _ in range(n):
    line = input().split()
    for name in line[2:]:
        if name:
            students.add(name)
print(len(students))